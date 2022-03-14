from django.urls import include,path
from . import views

urlpatterns = [
   path('',views.master,name='master'),
   path('courses',views.courses,name='courses'),
]