from django.shortcuts import render

# Create your views here.

# Vist de la pagina principal
def index(request):
    return render(request, 'home/index.html')

# Vista de la pagina de contacto
def contacto(request):
    return render(request, 'home/contacto.html')

