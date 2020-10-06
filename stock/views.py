from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def order(request):
    return render(request, 'frontend/order.html')

def contact(request):
    return render(request, 'frontend/contact.html')
    
