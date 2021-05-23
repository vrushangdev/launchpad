from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from sys import intern
# Create your views here.
from django.http import JsonResponse,HttpResponseNotAllowed,HttpResponse

def index(request):
    Featured_pool_list = Pool.objects.filter(pool_access="Featured")
    Upcoming_pool_list = Pool.objects.filter(pool_access="Upcoming")
    # if request.session['eth_address'] is not None:
    eth_address = request.session.get('eth_address',None)
    print(eth_address)
    return render(request,"index.html",{"Featured_pool_list":Featured_pool_list,"Upcoming_pool_list":Upcoming_pool_list, "eth_address":eth_address})

def pool_details(request,id):
    data = request.session.get('eth_address',None)
    pool = Pool.objects.get(id=id)
    whitelisted_address = Whitelist.objects.all().filter(pool_name=pool.id)
    # print(list(whitelisted_address.values('eth_address')))

    whitelisted_address = list(whitelisted_address.values('eth_address'))
    final_whitelisted_address = list()
    whitelist_flag = False 
    
    for addr in whitelisted_address:
        real_address = addr.get('eth_address',None)
        # print(data.lower(), real_address.lower())
        # print(data.lower() == real_address.lower())
        if data.lower() == real_address.lower():
            whitelist_flag = True
    #cant get eth_address from the jquery
    # print((data not in final_whitelisted_address))
    # print("FROM SESSION "+ str(data), "FROM DB " + str(final_whitelisted_address[0]))
    print(whitelist_flag)
    if whitelist_flag:
        # request.session['eth_address'] = None
        return render(request,"pinknode.html",{"pool":pool})        
    else:
        request.session['whitelist_status'] = "Not Whitelisted"
        return redirect("Index")

        
    
@csrf_exempt
def check_address(request,id):
    address = Whitelist.objects.filter(eth_adddres=id)

    if address is not None:
        return HttpResponse("0")
    else:
        return HttpsResponse("1") 

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

