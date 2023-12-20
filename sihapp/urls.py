# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),  # Assuming this is your homepage
    path('submit/', views.submit_data, name='submit_data'),

]
