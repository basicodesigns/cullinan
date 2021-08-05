from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('cottages/add/', views.addCottage),
    path('cottages/', views.getAllCottages),
    path('cottages/<int:pk>/', views.getCottageById),
    path('cottages/<int:pk>/update/', views.updateCottageById),
    path('cottages/<int:pk>/delete/', views.deleteCottageById),

    path('rooms/add/', views.addRoom),
    path('rooms/', views.getAllRooms),
    path('rooms/<int:pk>/', views.getRoomById),
    path('rooms/<int:pk>/update/', views.updateRoomById),
    path('rooms/<int:pk>/delete/', views.deleteRoomById),
]
