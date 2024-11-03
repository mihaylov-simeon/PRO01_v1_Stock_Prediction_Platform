from django.shortcuts import render

def index(request):
    return render(request, 'data_collection_frontend/index.html')