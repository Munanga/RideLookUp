from django.shortcuts import render, reverse
from django.views.generic import ListView,CreateView
from django.db.models import Q
from AppAuto.models import Vehicle
from AppAuto.forms import VehicleModelForm,ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from AppAuto import serializers
from rest_framework import status


@api_view(['GET','POST'])
def vehicle_list(request):
    if request.method == 'GET':
        queryset = Vehicle.objects.all()
        serialize = serializers.VehicleSerializer(queryset,many=True)
        return Response(serialize.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




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
        form = VehicleModelForm()
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

    context = {"query": query, "q_set": queryset, "check": check}
    return render(request,'search.html',context)


class Index(ListView):
    template_name = 'index.html'
    queryset = Vehicle.objects.all()
    context_object_name = 'data_set'


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            form_content = request.POST.get('text', '')

            send_mail(
                'Contact',
                form_content,
                contact_email,
                ['jackslaighter@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'contact.html', context)


class about(ListView):
    template_name = 'about.html'
    queryset = Vehicle.objects.all()


def delete(request, url_id):
    item_to_delete = Vehicle.objects.get(id=url_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')


def purchase(request, url_id):
    # i = get_object_or_404(id=url_id)
    item_to_purchase = Vehicle.objects.get(id=url_id)
    context = {"item_to_purchase":item_to_purchase}
    return render(request,'purchase_car.html',context)


def email_sent(request):
    return render(request,'email_sent.html',{})


class bob(ListView):
    template_name = 'bob.html'
    queryset = Vehicle.objects.all()






