from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def item(request):
    return render(request, 'main/item.html')
