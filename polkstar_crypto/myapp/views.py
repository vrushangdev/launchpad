from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.http import JsonResponse

def index(request):
    Featured_pool_list = Pool.objects.filter(pool_access="Featured")
    Upcoming_pool_list = Pool.objects.filter(pool_access="Upcoming")

    return render(request,"index.html",{"Featured_pool_list":Featured_pool_list,"Upcoming_pool_list":Upcoming_pool_list})

def pool_details(request,id):
    pool = Pool.objects.get(id=id)
    if pool.pool_status:
        return render(request,"pinknode.html",{"pool":pool})
    return redirect("Index")

def check_address(request,id):
    address = Whitelist.objects.get(eth_adddres=id)
    if address is not None:
        return JsonResponse({'whitelsited':'FALSE'})
    return JsonResponse({'whitelsited':'TRUE'}) 
