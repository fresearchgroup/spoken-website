from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'api/foss/(?P<fid>[0-9a-z]+)/tutorials/$', views.TutorialDetailList.as_view()), 
  url(r'api/foss/$', views.ContributorRoleList.as_view()), 
  url(r'api/tutorial/(?P<tid>[0-9]+)/scripts/$', views.ScriptCreateAPIView.as_view()),
  url(r'api/tutorial/(?P<tid>[0-9]+)/scripts/docs/$', views.ScriptDocumentCreateAPI.as_view()),
  url(r'api/tutorial/(?P<tid>[0-9]+)/scripts/(?P<script_detail_id>[0-9]+)/$', views.ScriptCreateAPIView.as_view()),
  url(r'api/scripts/(?P<script_detail_id>[0-9]+)/comments/$', views.CommentCreateAPIView.as_view()),
  url(r'api/scripts/(?P<script_detail_id>[0-9]+)/reversions/$', views.ReversionListView.as_view()),
  url(r'', views.index, name='home'),
]
