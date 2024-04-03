from django.urls import path
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [

    # These are not being used
    path('command', views.Command.as_view(), name='command'),
    path('lmcommand', views.LMCommand.as_view(), name='lmcommand'),

    # These are for the experiment
    path('action', views.Action.as_view(), name='action'),
    path('experiment_info', views.ExperimentInfo.as_view(), name='experiment_info'),

    # These are the only ones we are using
    path('gmcommand', views.GMCommand.as_view(), name='gmcommand'),
    path('stats/', include('academy_assistant.stats.urls')),
]




urlpatterns = format_suffix_patterns(urlpatterns)







