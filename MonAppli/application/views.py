from django.shortcuts import render

# Create your views here.


def acceuil(request):
    return render(request, "my-site-7.html")

def competences(request):
    return render(request, "compétences.html")

def contact(request):
    return render(request, "contact.html")

def formations(request):
    return render(request, "formations.html")

def experiences(request):
    return render(request, "experiences.html")

def garde(request):
    return render(request, "363-3632989_remote-sensing.jpg")
