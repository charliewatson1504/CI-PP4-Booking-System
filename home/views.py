from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def classes(request):
    return render(request, 'home/classes.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')