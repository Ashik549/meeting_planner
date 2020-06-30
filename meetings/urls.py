from django.urls import path

from .views import detail, rooms, new

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('rooms', rooms, name="rooms"),
    path('new', new, name="new")
]
