from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # to send text
    # return HttpResponse("this is teext on index page without html file")
    return render(request, 'app1/index.html')    # to render html
