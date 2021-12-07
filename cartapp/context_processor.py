from . models import *
from . views import *
def count(request):
    item_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=createsessionid(request))
            ct_item=cartitems.objects.all().filter(listkee=ct[:1])
            for c in ct_item:
                item_count = item_count + c.quan
        except cartlist.DoesNotExist:
            item_count=0
        return dict(itc=item_count,item=ct_item)