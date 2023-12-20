# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from django.contrib import messages

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('success_page')
        else:
            print(form.errors)
    else:
        form = UploadForm()

    return render(request, 'sihapp/index.html', {'form': form})


def submit_data(request):
    if request.method == 'POST':
        # Your logic for handling form submission goes here
        # ...

        # Example: If the form submission is successful, redirect to a success page
        return redirect('/')  # Make sure you have a 'success_page' URL pattern

    # If the request method is not POST, you may want to handle it differently
    # For example, you might want to render a form page again.
    return HttpResponse("Method not allowed", status=405)  # Example response for GET requests
