from django.http.response import JsonResponse
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from get_your_resources.forms import OrderResource
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import OrderHospital, OrderResource,OrderPharmacy, Ordervacc,OrderStock,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout 
from django.views.generic import TemplateView

from django.contrib import messages

from .filters import *

from .models import *
def dashboard(request):
    data = Resource.objects.all()
    context = {
        'data': data ,
    }
    return render(request, 'get_your_resources/dashboard.html',context)

def registerPage(request):
    if request.user.is_authenticated:
       form= CreateUserForm()
       if request.method == 'POST':
          form=CreateUserForm(request.POST)
       if form.is_valid():
          form.save()
          user=form.cleaned_data.get('username')
          messages.success(request,'Profile successfully created for '+ user)

          return redirect('login')
    else:
        return redirect('dashboard')

    context={'form':form}
    return render(request,'get_your_resources/register.html',context)

def loginPage(request):
    if request.method == 'POST':
       username= request.POST.get('username')
       password= request.POST.get('password')

       user=authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request,user)

       return redirect('dashboard')

    context={}
    return render(request,'get_your_resources/login.html',context)    

def Logoutuser(request):
   logout(request)
   return redirect('login')

def hospital(request):
    hospitals=Hospital.objects.all()
    myFilter= HospitalFilter(request.GET, queryset=hospitals)
    hospitals=myFilter.qs
    #x=Hospital.objects.aggregate(Sum('Shots_per_day'))
    x = Hospital.objects.all().aggregate(Sum('Shots_per_day')).get('Shots_per_day__sum')
    context={'hospitals': hospitals,'myFilter':myFilter,'x':x}
    return render(request,'get_your_resources/hospital.html',context)

def resources(request):
    resources=Resource.objects.all()
    myFilter= ResourceFilter(request.GET,queryset=resources)
    resources=myFilter.qs
    context={'resources': resources , 'myFilter':myFilter}
    return render(request,'get_your_resources/resources.html',context)

def pharmacy(request):
    pharmacies=Pharmacy.objects.all()

    myFilter= PharmacyFilter(request.GET,queryset=pharmacies)
    pharmacies=myFilter.qs
    contexts={'pharmacies': pharmacies,'myFilter':myFilter}
    return render(request,'get_your_resources/pharmacy.html', contexts)


def industry(request):
    Industries=Industry.objects.all()
    return render(request,'get_your_resources/industry.html',{'Industries': Industries})



    
def vaccination_centre(request):
    v=vaccination_center.objects.all()

    myFilter= VaccinationFilter(request.GET,queryset=v)
    v=myFilter.qs
    x =vaccination_center.objects.all().aggregate(Sum('Shots_per_day')).get('Shots_per_day__sum')
    context={'v':v,'myFilter':myFilter,'x':x}
    return render(request,'get_your_resources/vaccination_center.html',context)
   
def stockist(request):
    if request.user.is_authenticated: 
      S=Stockist.objects.all()
      myFilter= StockistFilter(request.GET, queryset=S)
      S=myFilter.qs
    else:
        return render(request,'get_your_resources/test.html')
    context={'myFilter':myFilter,'S':S}
    return render(request,'get_your_resources/Stockist.html', context)

def plasma_donors(request):
    plasma_donors=Plasma_Donor.objects.all()

    myFilter= PlasmaFilter(request.GET, queryset=plasma_donors)
    plasma_donors=myFilter.qs
    context={'myFilter':myFilter,'plasma_donors':plasma_donors}
    return render(request,'get_your_resources/Plasma_donors.html',context)
    

def pharm_res(request , pk_test):
    P_id=Pharmacy.objects.get(id=pk_test)
    pharm_res= P_id.pres.all()
    myFilter= PharmresFilter(request.GET, queryset=pharm_res)
    pharm_res=myFilter.qs
    context={'P_id': P_id ,'pharm_res' : pharm_res,'myFilter':myFilter}
    return render(request,'get_your_resources/pharm_res.html', context)

def vac_res(request , pk_test):
    Vc_id=vaccination_center.objects.get(id=pk_test)
    vcres= Vc_id.vres.all()
    myFilter= VacresFilter(request.GET,queryset=vcres)
    vcres=myFilter.qs
    context={'Vc_id': Vc_id , 'vcres' : vcres,'myFilter':myFilter}
    return render(request,'get_your_resources/vac_res.html', context)

def s_res(request , pk_test):
       Stockist_id=Stockist.objects.get(id=pk_test)
       sress= Stockist_id.Sres.all()
       myFilter= StockresFilter(request.GET,queryset=sress)
       sress=myFilter.qs
       context={'Stockist_id': Stockist_id , 'sress' : sress,'myFilter':myFilter}
       return render(request,'get_your_resources/s_res.html', context)

def h_res(request , pk_test):
    H_id=Hospital.objects.get(id=pk_test)
    Hospital_resources=H_id.hres.all()
    myFilter= HosresFilter(request.GET, queryset=Hospital_resources)
    Hospital_resources=myFilter.qs
    context={'Hospital_resources': Hospital_resources,'H_id' : H_id,'myFilter':myFilter}
    return render(request,'get_your_resources/h_res.html', context)

def createResources(request):
    if request.user.is_authenticated:
           form = OrderResource()
           if request.method == 'POST':
               # print('Printing POST:', request.POST)
                form = OrderResource(request.POST)
           if form.is_valid():
                form.save()
                return redirect('/')
    else:
          return redirect('/tests/')
    context={'form': form}
    return render(request, 'get_your_resources/resourceForm.html', context)

def updateResources(request, pk):
     if request.user.is_authenticated:
         i=Hospital_resource.objects.get(id=pk)
         form = OrderHospital(instance=i)
         if request.method == 'POST':
             # print('Printing POST:', request.POST)
             form = OrderHospital(request.POST, instance=i)
         if form.is_valid():
           form.save()
           return redirect('/hospital/')
     else:
           return redirect('/tests/')
     context={'form': form}
     return render(request, 'get_your_resources/resourceForm.html', context)

def updateResourcesP(request, pk):
    if request.user.is_authenticated:
       i=Pharm_res.objects.get(id=pk)
       form = OrderPharmacy(instance=i)
       if request.method == 'POST':
          # print('Printing POST:', request.POST)
          form = OrderPharmacy(request.POST, instance=i)
       if form.is_valid():
           form.save()
           return redirect('/pharmacy/')
    else:
        return redirect('/tests/')
    context={'form': form}
    return render(request, 'get_your_resources/resourceForm.html', context)

def updateResourcesV(request, pk):
    if request.user.is_authenticated:
       i=Vac_res.objects.get(id=pk)
       form = Ordervacc(instance=i)
       if request.method == 'POST':
           # print('Printing POST:', request.POST)
           form = Ordervacc(request.POST, instance=i)
       if form.is_valid():
           form.save()
           return redirect('/vaccination_centre/')
    else:
        return redirect('/tests/')
    context={'form': form}
    return render(request, 'get_your_resources/resourceForm.html', context)

def updateResourcesS(request, pk):
    if request.user.is_authenticated:
        i=Stockist_resource.objects.get(id=pk)
        form = OrderStock(instance=i)
        if request.method == 'POST':
            # print('Printing POST:', request.POST)
            form = OrderStock(request.POST, instance=i)
        if form.is_valid():
           form.save()
           return redirect('/stockist/')
    else:
        return redirect('/tests/')
    context={'form': form}
    return render(request, 'get_your_resources/resourceForm.html', context)

def delete_view(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Pharm_res, id = id)
        context ={'item':obj}
        if request.method =="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        return redirect('/tests/')
    return render(request, "get_your_resources/delete_view.html", context)

def delete_viewH(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Hospital_resource, id = id)
        context ={'item':obj}
        if request.method =="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        return redirect('/tests/')
    return render(request, "get_your_resources/delete_view.html", context)

def delete_viewV(request, id):
    if request.user.is_authenticated: 
         obj = get_object_or_404(Vac_res, id = id)
         context ={'item':obj}
         if request.method =="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        return redirect('/tests/')
    return render(request, "get_your_resources/delete_view.html", context)

def delete_viewS(request, id):
    if request.user.is_authenticated:
         obj = get_object_or_404(Stockist_resource, id = id)
         context ={'item':obj}
         if request.method =="POST":
            obj.delete()
            return HttpResponseRedirect("/")
    else:
        return redirect('/tests/')
    return render(request, "get_your_resources/delete_view.html", context)

def error(request):
    return render(request, "get_your_resources/test.html")