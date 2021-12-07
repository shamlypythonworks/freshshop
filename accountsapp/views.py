from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
# Create your views here.
def register(request):
    return render(request,'register.html')
def registerinfo(request):
  try:
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('e_mail'):
            reg = registertble()
            reg.fullname = request.POST.get('name')
            reg.email = request.POST.get('e_mail')
            if request.POST.get('pswd') == request.POST.get('repswd'):
                reg.paswd = request.POST.get('pswd')
                reg.repaswd = request.POST.get('repswd')
                reg.chk_box = request.POST.get('chkbox')
                reg.save()
                messages.success(request,'successfully entered your details')
                # code to show warning msg
            else:
                messages.warning(request,'password mismatch')
    return render(request,'register.html')
  except IntegrityError:
        messages.warning(request,'email already exists')
        return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def validation(request):
    try:
        if request.method == 'POST':
            usrname = request.POST.get('Username')
            pwd = request.POST.get('psw')
            obj = registertble.objects.get(fullname=usrname)
            if obj.paswd == pwd:
                return redirect('cartDetails')
            else:
                messages.error(request,'your password is not correct')
                return render(request,'login.html')
    except registertble.DoesNotExist:
        messages.error(request,'username is not valid')
        return render(request,'login.html')



