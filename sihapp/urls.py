from .views import index
from django.urls import path,include
from django.urls import path
from .views import upload_image
urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_image, name='upload_image'),

]



urlpatterns = [
    # Add other URL patterns as needed
]