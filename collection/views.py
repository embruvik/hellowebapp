from django.shortcuts import render
from django.http import HttpResponse
from collection.models import Thing

# Create your views here.
def index(request):
    things = Thing.objects.all()
    retobj = render(request, 'index.html', {'things': things,})
    print('Hello?')
    return retobj

def index2(request):
    #return render
    return HttpResponse('Hello ' + request.path, 'text', 200)

def thing_detail(request, slug):
    thing = Thing.objects.get(slug=slug)

    return render(request, 'things/thing_detail.html', {'thing': thing,})
    
