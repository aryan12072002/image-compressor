from django.urls import path
from .views import upload_image, image_list,download_image,delete_image

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
    path('download/<int:image_id>/', download_image, name='download_image'),
    path('delete/<int:image_id>/', delete_image, name='delete_image'),
]


