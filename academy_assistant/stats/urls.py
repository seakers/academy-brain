from django.urls import path, include

from . import views

urlpatterns = [

    # This is used for estimating the user ability parameter when they answer a question
    path('updatemodel', views.UpdateModel.as_view(), name='updatemodel'),


    # These are not used for the ability parameter updates
    path('updatemodeltid', views.UpdateModelTID.as_view(), name='updatemodeltid'),
    path('adaptivequestion', views.AdaptiveQuestion.as_view(), name='adaptivequestion'),
]