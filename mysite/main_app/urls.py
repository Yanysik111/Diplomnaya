from django.urls import path
from .views import index, save_text, delete_text



urlpatterns = [
    path('', index, name='index'),
    path('save-text/', save_text, name='save_text'),
    path('delete-text/<int:pk>/', delete_text, name='delete_text'),
]

