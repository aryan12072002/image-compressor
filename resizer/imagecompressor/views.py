from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import CompressedImage
from PIL import Image
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from PIL import Image
import os

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            image = form.save()
            # Compress the image
            compress_image(image.image.path)
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def compress_image(image_path):
    # Open the original image
    with Image.open(image_path) as img:
        # Set the output path for the compressed image
        output_path = image_path  # Overwrite original image, change if needed
        
        # Compress the image
        img.save(output_path, format='JPEG', quality=70, optimize=True)

def image_list(request):
    images = CompressedImage.objects.all()
    return render(request, 'image_list.html', {'images': images})


def download_image(request, image_id):
    image = get_object_or_404(CompressedImage, id=image_id)
    # Open the image file
    with open(image.image.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{image.image.name.split("/")[-1]}"'
        return response
    
def delete_image(request, image_id):
    image = get_object_or_404(CompressedImage, id=image_id)
    # Delete the image file from the file system
    if os.path.isfile(image.image.path):
        os.remove(image.image.path)
    # Delete the image record from the database
    image.delete()
    return redirect('image_list')