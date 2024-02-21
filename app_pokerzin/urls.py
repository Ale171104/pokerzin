from django.urls import path


from .views import PlayerAPIView

    
urlpatterns = [
    path('players/', PlayerAPIView.as_view(), name = 'players'),
]


    


