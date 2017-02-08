from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    number = 6
    retobj = render(request, 'index.html', {'number': number})
    print('Hello?')
    return retobj

def index2(request):
    #return render
    return HttpResponse('Hello ' + request.path, 'text', 200)
