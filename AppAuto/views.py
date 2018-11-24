from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.db.models import Q
from AppAuto.models import Vehicle
from AppAuto.forms import VehicleModelForm,ContactForm
from django.http import HttpResponseRedirect

# Create your views here.

# class Index(ListView):
#     template_name = 'index.html'
#     context_object_name = 'Vehicles'

def create(request):
    if request.method == "POST":
        form = VehicleModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = VehicleModelForm
    context = {"form":form}
    return render(request,'create.html',context)


def search(request):
    query = request.GET.get('q')
    queryset = []
    check = []
    if request.method == "GET":
        if query:
            queryset = Vehicle.objects.filter(Q(name__iexact=query)|
                                              Q(name__icontains=query)
                                              )
            check = queryset.exists()

    context = {"query":query,"q_set":queryset,"check":check}

    return render(request,'search.html',context)

class index(ListView):
    template_name = 'index.html'
    queryset = Vehicle.objects.all()
    context_object_name = 'data_set'

class contact(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

class about(ListView):
    template_name = 'about.html'
    queryset = Vehicle.objects.all()
    
def delete(request,url_id):
    item_to_delete = Vehicle.objects.get(id=url_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/search/')






