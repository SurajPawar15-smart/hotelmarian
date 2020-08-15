from django.shortcuts import render
from django.http import HttpResponse
def about(request):
   return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def elements(request):
    return render(request, 'elements.html')
def index(request):
    return render(request, 'index.html')
def main(request):
    return render(request, 'main.html')
def rooms(request):
    return render(request, 'rooms.html')
def services(request):
    return render(request, 'services.html')
def single_blog(request):
    return render(request, 'single_blog.html')


