import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .inference import predict_image, weights_loaded

def landing(request):
    return render(request, 'detector/landing.html')

def index(request):
    context = {
        'weights_loaded': weights_loaded
    }
    
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        
        # Save the uploaded file
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        file_path = fs.path(filename)
        
        # Run inference
        result = predict_image(file_path)
        
        context['uploaded_file_url'] = uploaded_file_url
        context['result'] = result
        
    return render(request, 'detector/index.html', context)
