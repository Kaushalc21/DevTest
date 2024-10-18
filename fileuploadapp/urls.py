from django.urls import path
from . import views  # Ensure you import your views

urlpatterns = [
    path('', views.upload_file, name='upload'),  # Root URL routing to upload_file
    path('upload/', views.upload_file, name='upload'),  # Optional: Keep this if you want /upload to work too
    path('success/', views.success, name='success'),  # Success view pattern
]
