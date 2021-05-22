from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse,HttpResponseNotAllowed,HttpResponse

def index(request):
    Featured_pool_list = Pool.objects.filter(pool_access="Featured")
    Upcoming_pool_list = Pool.objects.filter(pool_access="Upcoming")
    eth_address = request.session['eth_address']
    print(eth_address)

    return render(request,"index.html",{"Featured_pool_list":Featured_pool_list,"Upcoming_pool_list":Upcoming_pool_list, "eth_address":eth_address})

def pool_details(request,id):
    address = Whitelist.objects.get()
    print(address)
    address = address[0]
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

@csrf_exempt
def update_session(request):
    print(request)
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponse("Get Not Allowed")
    # data = request.POST.get("eth_address",none)
    eth_address = request.POST.get('eth_address')
    request.session['eth_address'] = eth_address
    print("REQ POST", eth_address)
    return HttpResponse(eth_address)

