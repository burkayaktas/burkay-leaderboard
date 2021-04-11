"""project URL Configuration

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
from django.contrib import admin
from django.urls import path
from board import views
from api.views import user_api_view, leaderboard_api_view, leaderboard_country_api_view, user_create_api_view, score_submit_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('user/profile/<int:user_id>', user_api_view, name="user_profile"),
    path('leaderboard/', leaderboard_api_view),
    path('leaderboard/<country>', leaderboard_country_api_view, name="leaderboard_country"),
    path('user/create/', user_create_api_view),
    path('score/submit/', score_submit_api_view),
]
