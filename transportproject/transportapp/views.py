from django.shortcuts import render
from . models import place
from . models import guys

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=guys.objects.all()
    return render(request, "index.html", {'result': obj, 'ans': obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request, "about.html", {'result': res})