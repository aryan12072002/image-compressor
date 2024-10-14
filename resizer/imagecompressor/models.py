from django.db import models
from django.core.files import File
from PIL import Image as PilImage
import io
from django.db import models

class CompressedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
