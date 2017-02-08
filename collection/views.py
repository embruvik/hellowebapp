from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ro = render(request, 'index.html')
    print('Hello?')
    return ro

def index2(request):
    #return render
    return HttpResponse('Hello ' + request.path,'text',200)
