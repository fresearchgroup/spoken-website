from django.shortcuts import render
from creation.models import ContributorRole,TutorialDetail,User
from .models import Scripts,ScriptDetails,Comments
from .serializers import ContributorRoleSerializer,TutorialDetailSerializer,ScriptsDetailSerializer,ScriptsSerializer,CommentsSerializer,ReversionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework_jwt.settings import api_settings
from reversion.models import Version
import os
from django.core.files.storage import FileSystemStorage
from bs4 import BeautifulSoup
import time

def index(request):
  jwt_payload_handler  =  api_settings.JWT_PAYLOAD_HANDLER
  jwt_encode_handler  =  api_settings.JWT_ENCODE_HANDLER
  payload  =  jwt_payload_handler(request.user)
  token  =  jwt_encode_handler(payload) 
  return render(request, 'scriptmanager/index.html', {'token': token})


class ContributorRoleList(generics.ListAPIView):
  def get_queryset(self):
      return ContributorRole.objects.filter(user = self.request.user)
  serializer_class  =  ContributorRoleSerializer


class TutorialDetailList(generics.ListAPIView):
  serializer_class = TutorialDetailSerializer

  def get_serializer_context(self):
    return {"lang": self.kwargs['lid'],"user":self.request.user}
    
  def get_queryset(self):
    if ContributorRole.objects.filter(user  =  self.request.user,foss_category  =  self.kwargs.get('fid')).exists():
      return TutorialDetail.objects.filter(foss  =  self.kwargs.get('fid')).order_by('order')
    else:
      return None

class ScriptCreateAPIView(generics.ListCreateAPIView):
  serializer_class = ScriptsDetailSerializer

  def get_queryset(self): 
    script = Scripts.objects.filter(tutorial = int(self.kwargs['tid']),user = self.request.user)
    return ScriptDetails.objects.filter(script = script)
  
  def scriptsData(self, html,script):
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find("table") 
    details=[]
    count=-1
    for row in table.find_all('tr'):
      count+=1
      columns=row.find_all('td')
      try:
        details.append({"order": count,"cue": str(columns[0]),"narration": str(columns[1]),"script":script.pk})
      except:
        continue
    details.pop(0)
    return details
      
  def create(self, request,tid):
    details=[]
    try:
      tutorial=TutorialDetail.objects.get(pk = int(self.kwargs['tid']))
      if not  Scripts.objects.filter(user  =  self.request.user,tutorial=tutorial).exists():
        script  =  Scripts.objects.create(tutorial = tutorial,user = self.request.user)
      else:
        script  =  Scripts.objects.get(tutorial = tutorial,user = self.request.user)

      type=request.data['type']
      if(type=='form'):
        details = request.data['details']

      elif(type=='file'):
        myfile=request.FILES['docs']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        file=os.getcwd()+'/media/'+filename
        os.system('libreoffice --convert-to html '+file)
        html_file=os.path.splitext(os.getcwd()+'/'+filename)[0]+'.html'
        time.sleep(.4)  #time to convert the file to html
        html = open(html_file,'r')
        details=self.scriptsData(html,script)
        os.system('rm '+ file + ' '+html_file)

      serialized  =  ScriptsDetailSerializer(data  =  details,many  =  True) #inserting a details array without iterating
      if serialized.is_valid():
        serialized.save()
        return Response({'status': True},status = 201)
    except:
      return Response({'status': False},status = 400) 


  def patch(self,request, tid):
    try:
      tutorial=TutorialDetail.objects.get(pk = int(self.kwargs['tid']))
      script_details  =  self.request.data
      Scripts.objects.get(tutorial = tutorial,user = self.request.user)

      script  =  ScriptDetails.objects.get(pk = (script_details['id']))
      serializer  =  ScriptsDetailSerializer(script, data = script_details)
      if serializer.is_valid():
        serializer.save()
      return Response({'status': True},status = 200)
    except:
      return Response({'status': False},status = 400) 


  def delete(self,request,tid,script_detail_id):
    try:
      tutorial=TutorialDetail.objects.get(pk = int(self.kwargs['tid']))
      script  =  Scripts.objects.get(tutorial = tutorial,user  =  self.request.user)

      ScriptDetails.objects.get(pk = int(self.kwargs['script_detail_id']),script = script).delete()
      if not ScriptDetails.objects.filter(script_id = script.pk).exists(): 
       script.delete()
      return Response({'status': True},status = 202) 
    except:
      return Response({'status': False},status = 400) 


class CommentCreateAPIView(generics.ListCreateAPIView):
  serializer_class=CommentsSerializer

  def get_queryset(self):
    try:
      script_detail=ScriptDetails.objects.get(pk=int(self.kwargs['script_detail_id']))
      return Comments.objects.filter(script_details = script_detail).order_by('created')
    except:
      return None


  def create(self,request,script_detail_id):
    try:
      script_data=ScriptDetails.objects.get(pk=script_detail_id)
      Comments.objects.create(comment=request.data['comment'],user=self.request.user,script_details=script_data)
      return Response({'status': True},status = 202)
    except:
      return Response({'status': False},status = 400)


class ReversionListView(generics.ListAPIView):
  serializer_class = ReversionSerializer

  def get_queryset(self):
    try:
      script_detail=ScriptDetails.objects.get(pk=int(self.kwargs['script_detail_id']))
      reversion_data = Version.objects.get_for_object(script_detail)
      data = []
      for i in reversion_data:
        result=i.field_dict
        result.update({"date_time":i.revision.date_created,"reversion_id":i.revision.pk,"user":i.revision.user})
        data.append(result)
      return ReversionSerializer(data,many=True).data
    except:
      return None
