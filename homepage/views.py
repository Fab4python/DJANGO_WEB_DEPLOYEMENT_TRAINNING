from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'homepage/index.html')

def health_check(request):
    return JsonResponse({'status': 'healthy', 'message': 'Django app is running'})
