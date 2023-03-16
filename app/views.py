from django.shortcuts import render

# Create your views here.


def conditions(request):
    d={'a':10,'b':9,'c':8}
    return render(request,'condition.html',d)

def forloop(request):
    d={'name':'KING'}
    return render(request,'loop.html',d)