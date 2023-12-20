from django.shortcuts import render

def index(request):
    return render(request, 'sihapp/index.html')
    

# views.py
from django.shortcuts import render, redirect
from .forms import ImageUploadForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded image here, e.g., save it to the database or process it
            # You can access the image file using form.cleaned_data['image']

            # Redirect to a success page or do something else
            return redirect('success_page')
    else:
        form = ImageUploadForm()

    return render(request, 'sihapp/index.html', {'form': form})
