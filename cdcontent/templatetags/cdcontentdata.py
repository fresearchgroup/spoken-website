from django.contrib.auth.models import User
from django.conf import settings
from creation.models import *
from django import template
import os

register = template.Library()

def get_foss_name(foss, key):
    return foss[key]['foss']

def get_lang_details(foss, key):
    data = ''
    for lang_key, lang_detail in foss[key]['langs'].iteritems():
        data += '<option value="' + str(lang_key) + '">' + lang_detail + '</option>'
    return data

def get_srt_files(tr):
    data = ''
    k = tr.video.rfind(".")
    new_srtfile = tr.video[:k] + '.srt'
    if tr.language.name != 'English':
        if os.path.isfile(settings.MEDIA_ROOT + 'videos/' + str(tr.tutorial_detail.foss_id) + '/' + str(tr.tutorial_detail_id) + '/' + new_srtfile.replace(tr.language.name, 'English')):
            data += '<track kind="captions" src="./' + new_srtfile.replace(tr.language.name, 'English') + '" srclang="en" label="English" />'
    if os.path.isfile(settings.MEDIA_ROOT + 'videos/' + str(tr.tutorial_detail.foss_id) + '/' + str(tr.tutorial_detail_id) + '/' + new_srtfile):
        data += '<track kind="captions" src="./' + new_srtfile + '" srclang="en" label="' + tr.language.name + '" />'
    return data

register.filter('get_foss_name', get_foss_name)
register.filter('get_lang_details', get_lang_details)
register.filter('get_srt_files', get_srt_files)