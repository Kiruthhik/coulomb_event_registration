from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('events/',views.events,name='events'),
    path('participant_register/',views.participant_register,name='participant_register'),
    path('teammate_register/',views.teammate_register,name='teammate_register'),
    path('event_detail/<int:id>/',views.event_detail,name='event_detail'),
    path('profile/edit/', views.complete_profile, name="complete_profile"),
]