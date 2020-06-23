from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'key1':'Hello World','key2':122 }
    return render(request,'third_app/index.html',context_dict)


def other(request):
    return render(request,'third_app/other.html')


def relative(request):
    return render(request,'third_app/relative_url.html')
