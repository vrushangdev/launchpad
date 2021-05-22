from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.http import JsonResponse,HttpResponseNotAllowed,HttpResponse

def index(request):
    Featured_pool_list = Pool.objects.filter(pool_access="Featured")
    Upcoming_pool_list = Pool.objects.filter(pool_access="Upcoming")

    return render(request,"index.html",{"Featured_pool_list":Featured_pool_list,"Upcoming_pool_list":Upcoming_pool_list})

def pool_details(request,id):
    address = Whitelist.objects.get()
    pool = Pool.objects.get(id=id)
    data = request.session['eth_address']
    #cant get eth_address from the jquery
    if pool.pool_status and address in data:
        return render(request,"pinknode.html",{"pool":pool,"address":address})
    return redirect("Index")

def check_address(request,id):
    address = Whitelist.objects.get(eth_adddres=id)
    if address is not None:
        return JsonResponse({'whitelsited':'FALSE'})
    return JsonResponse({'whitelsited':'TRUE'}) 

def update_session(request):
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    data = request.session['eth_address']
    return HttpResponse("{'address_set': {}}".format(data))

