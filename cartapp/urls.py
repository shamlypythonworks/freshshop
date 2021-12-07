from django.urls import path
from . import views
urlpatterns=[
    path('addtocart/<slug:p_slug>',views.addtocart,name='addtocart'),
    path('minCart/<slug:p_slug>',views.min_cart,name='minCart'),
    path('delitem/<slug:p_slug>',views.del_item,name='delitem'),
    path('cartDetails/',views.cart_Details,name='cartDetails'),

]