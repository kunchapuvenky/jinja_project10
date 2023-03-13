from django.shortcuts import render

# Create your views here.


def jinja_1(request):
    d={'name':'Lohith','age':2}
    return render(request,'jinja_1.html',context=d)