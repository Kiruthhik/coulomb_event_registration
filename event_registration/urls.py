from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('events/',views.events,name='events'),
    path('event_detail/<int:id>/',views.event_detail,name='event_detail'),
    path('profile/edit/', views.complete_profile, name="complete_profile"),
]