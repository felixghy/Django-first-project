"""advcbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,re_path
from . import views

app_name = 'basic_app'

urlpatterns = [
    #
    # path('',views.index),
    # path('base',views.base),
    #path('',views.CBView.as_view())
    path('', views.IndexView.as_view()),
    path('list/', views.SchoolListView.as_view(),name='list'),
    path('list/<int:pk>', views.SchoolDetailView.as_view(),name='sch_detail'),
    path('create/', views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(),name='delete'),
    # path('register/<int:pk>', views.UserRegisterView.as_view(),name='register'),
    #path('userList/<int:pk>', views.UserListView.as_view(),name='user_list'),
    #re_path(r'^(?P<pk>[-\w]+/$)', views.SchoolDetailView.as_view()),
     path('register/',views.register,name='register'),
     path('createStudent1/', views.StudentCreateView.as_view(),name='createStudent'),
     path('deleteStudent/<int:pk>', views.StudentDeleteView.as_view(),name='student_delete'),
     path('studentDetails/<int:pk>', views.StudentDetailView.as_view(),name='student_detail_URL'),
     path('studentList/',views.StudentListView.as_view(),name='student_list'),
     path('login/',views.user_login,name='login_NS'),
     path('logout/',views.user_logout,name='logout'),


]
