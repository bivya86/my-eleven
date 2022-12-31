from django.shortcuts import render

# Create your views here.

def impossible(request):
    return render(request,'impossible.html')