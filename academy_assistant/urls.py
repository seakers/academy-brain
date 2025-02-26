from django.urls import path
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('command', views.Command.as_view(), name='command'),
    path('lmcommand', views.LMCommand.as_view(), name='lmcommand'),
    path('transcribe', views.TranscribeAudio.as_view(), name='transcribe_audio'),
    path('text_to_speech', views.TextToSpeech.as_view(), name='text_to_speech'),
    path('explain_slide', views.ExplainSlide.as_view(), name='explain_slide'),
    path('gmcommand', views.GMCommand.as_view(), name='gmcommand'),
    path('action', views.Action.as_view(), name='action'),
    path('experiment_info', views.ExperimentInfo.as_view(), name='experiment_info'),
    path('stats/', include('academy_assistant.stats.urls')),
]




urlpatterns = format_suffix_patterns(urlpatterns)







