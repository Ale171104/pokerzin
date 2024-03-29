"""
URL configuration for project_pokerzin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app_pokerzin.views import PlayerAPIView, PlayerPutDeleteAPIView, GameAPIView,GamePutDeleteAPIView , PlayerHasGameAPIView, PlayerHasGamePutDeleteAPIView



urlpatterns = [
    path('api/v1/player/', PlayerAPIView.as_view(), name = 'player'),
    path('api/v1/player/<int:pk>/', PlayerPutDeleteAPIView.as_view(), name = 'player_put_delete'),
    
    path('api/v1/game/', GameAPIView.as_view(), name = 'game'),
    path('api/v1/game/<int:pk>/', GamePutDeleteAPIView.as_view(), name = 'game_put_delete'),
    
    path('api/v1/playerhasgame/', PlayerHasGameAPIView.as_view(), name = 'playerhasgame'),
    path('api/v1/playerhasgame/<int:pk>/', PlayerHasGamePutDeleteAPIView.as_view(), name = 'playerhasgame_put_delete'),
    
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    
]
