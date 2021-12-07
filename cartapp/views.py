from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from homeapp.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_Details(request,items=None,count=0,total=0):
    try:
        ct=cartlist.objects.get(cart_id=createsessionid(request))
        items=cartitems.objects.filter(listkee=ct,active=True)
        for i in items:
            total=total+(i.prokee.price * i.quan)
            count= count+ i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ct_item':items,'total':total,'count':count})
def createsessionid(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def addtocart(request,p_slug):
    pdt = prdttable.objects.get(slug=p_slug)
    try:
        ct_list = cartlist.objects.get(cart_id=createsessionid(request))
    except cartlist.DoesNotExist:
            ct_list = cartlist.objects.create(cart_id=createsessionid(request))
    ct_list.save()
    try:
        item=cartitems.objects.get(prokee=pdt,listkee=ct_list)
        if item.quan <= item.prokee.stock:
            item.quan = item.quan+1
        item.save()
    except cartitems.DoesNotExist:
        item = cartitems.objects.create(prokee=pdt, listkee=ct_list,quan=1)
        item.save()
    return redirect('cartDetails')
def min_cart(request,p_slug):
    pdt = prdttable.objects.get(slug=p_slug)
    ct = cartlist.objects.get(cart_id=createsessionid(request))
    item = get_object_or_404(cartitems,listkee=ct,prokee=pdt)
    if item.quan > 1:
        item.quan -= 1
        item.save()
    else:
        item.delete()
    return redirect('cartDetails')
def del_item(request,p_slug):
    pdt = prdttable.objects.get(slug=p_slug)
    ct = cartlist.objects.get(cart_id=createsessionid(request))
    item = get_object_or_404(cartitems,listkee=ct,prokee=pdt)
    item.delete()
    return redirect('cartDetails')
