from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import FileUploadForm

def handle_uploaded_file(file):
    fs = FileSystemStorage()
    fs.save(file.name, file)

def main(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            handle_uploaded_file(uploaded_file)
            return JsonResponse({'status': 'success', 'file_name': uploaded_file.name})
        else:
            return JsonResponse({'status': 'error'})
    else:
        form = FileUploadForm()
    return render(request, 'main.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

def intro(request):
    return render(request, 'intro.html')

# Create your views here.
