from django.shortcuts import render, redirect
from django.http import HttpResponse

from collection.forms import ThingForm
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

def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)
    # set the form we are using
    form_class = ThingForm

    # if we are coming to this view from a submitted format
    if request.method == 'POST':
        # grab data form the submitted form and apply to the format
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail',slug=thing.slug)
    else:
        #otherwise just create the form
        form = form_class(instance=thing)
    
    retobj = render(request,'things/edit_thing.html', {'thing': thing, 'form': form,})
    return retobj

