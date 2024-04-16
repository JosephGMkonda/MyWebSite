from django.urls import path
from . import views


urlpatterns = [

   path('',views.HomeView, name="home"),
   path('projects',views.ProjectView, name="projects"),
   path('resume',views.ResumeView, name="resume"),
   path('contact',views.ContactView, name="contact"),
  
   
   

]