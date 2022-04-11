"""homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from .views import TestListView, TestDetail, IndexPhotosListView, PublicationListView, PublicationYearsListView, PublicationsMembersListView, IntroduceUsListView, AlumniMsListView, AlumniPhDListView, OurLabTopicListView

urlpatterns = [
    path('get-api/', TestListView.as_view()),
    path('get-api/<int:pk>/', TestDetail.as_view()),
    path('get-api/photos/', IndexPhotosListView.as_view()),
    path('get-api/publication/', PublicationListView.as_view()),
    path('get-api/publication/year', PublicationYearsListView.as_view()),
    path('get-api/publication/members', PublicationsMembersListView.as_view()),
    path('get-api/introduce', IntroduceUsListView.as_view()),
    path('get-api/introduce/category', IntroduceUsListView.as_view()),
    path('get-api/introduce/Alumni/Ms', AlumniMsListView.as_view()),
    path('get-api/introduce/Alumni/PhD', AlumniPhDListView.as_view()),
    path('get-api/topic', OurLabTopicListView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls'))
]
