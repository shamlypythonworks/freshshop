from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('search/',views.searching,name='search'),
    path('reviewpage/<slug:p_slug>',views.reviewpage,name='reviewpage'),
    path('<slug:c_slug>/',views.homepage,name='categwiseview'),
    path('<slug:c_slug>/<slug:p_slug>',views.detailpage,name='detailpage'),

    ]
urlpatterns= urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)