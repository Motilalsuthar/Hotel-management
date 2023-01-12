from django.shortcuts import render ,redirect
from .models import *
# Create your views here.
def view(request):
    return render(request,'hotelapp/hotel.html')

def add_view(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        id=request.POST.get('id')
        ml=request.POST.get('mail')
        num=request.POST.get('cnum')
        
        user=add_user(Name=nm,Id_name=id,Mail=ml,Mobile_number=num)
        user.save()
    
    
        
    
    data=add_user.objects.all()
    context={'data':data}
    
    
    
    
    
    return render(request,'hotelapp/add.html',context)
    

def display_view(request):
    
    data=add_user.objects.all()
    context={'data':data}
    if request.method=='POST':
        val=request.POST.get('val')
        data=add_user.objects.filter(Name__contains=val)
        context={'data':data}
        return render(request,'hotelapp/dsu.html',context)

    return render(request,'hotelapp/display.html',context)

def rdisplay_view(request):
    
    data=add_room.objects.all()
    context={'data':data}
    if request.method=='POST':
        val=request.POST.get('val')
        data=add_room.objects.filter(roomtype__contains=val)
        context={'data':data}
        return render(request,'hotelapp/dsr.html',context)
    return render(request,'hotelapp/roomdisplay.html',context)


def room_view(request):
    if request.method=='POST':
        rnm=request.POST.get('rname')
        rfl=request.POST.get('fname')
        rtp=request.POST.get('type')
        rdo=request.POST.get('gridRadios')
        pr=request.POST.get('rprice')
       
        
        user=add_room(roomnumber=rnm,roomfloor=rfl,roomtype=rtp, select=rdo, roomprice=pr)
        user.save()
    
    data=add_room.objects.all()
    context={'data':data}
    return render(request,'hotelapp/addroom.html',context)

def updateuser_view(request,u):
    
    data=add_user.objects.get(id=u)
    context={'data':data}
    if request.method=='POST':
        nm=request.POST.get('name')
        id=request.POST.get('id')
        ml=request.POST.get('mail')
        num=request.POST.get('cnum')
        
        data.Name=nm
        data.Id_name=id
        data.Mail=ml
        data.Mobile_number=num
        data.save()
        return redirect('/display/')
        
        
    return render(request,'hotelapp/update.html',context)


def upuser_views(request):
    
    data=add_user.objects.all()
    context={'data':data}
    if request.method=='POST':
        nm=request.POST.get('name')
        id=request.POST.get('id')
        ml=request.POST.get('mail')
        num=request.POST.get('cnum')
        
        data.Name=nm
        data.Id_name=id
        data.Mail=ml
        data.Mobile_number=num
        data.save()
        return redirect('/update/')
    return render(request,'hotelapp/u_update.html',context)

def updateroom_view(request,u):
    data=add_room.objects.get(id=u)
    context={'data':data}
    if request.method=='POST':
        rnm=request.POST.get('rname')
        rfl=request.POST.get('fname')
        rtp=request.POST.get('type')
        rdo=request.POST.get('gridRadios')
        pr=request.POST.get('rprice')
        
        data.roomnumber=rnm
        data.roomfloor=rfl
        data.roomtype=rtp
        data.select=rdo
        data.roomprice=pr
        data.save()
        return redirect('/roomdisplay/')     
    return render(request,'hotelapp/roomupdate.html',context)


def uproom_views(request):
    data=add_room.objects.all()
    context={'data':data}
    if request.method=='POST':
        rnm=request.POST.get('rname')
        rfl=request.POST.get('fname')
        rtp=request.POST.get('type')
        rdo=request.POST.get('gridRadios')
        pr=request.POST.get('rprice')
        
        data.roomnumber=rnm
        data.roomfloor=rfl
        data.roomtype=rtp
        data.select=rdo
        data.roomprice=pr
        data.save()
        return redirect('/roomdisplay/')
    return render(request,'hotelapp/r_update.html',context)


def uproom_views(request):
    
    data=add_room.objects.all()
    context={'data':data}
    if request.method=='POST':
        nm=request.POST.get('name')
        id=request.POST.get('id')
        ml=request.POST.get('mail')
        num=request.POST.get('cnum')
        
        data.Name=nm
        data.Id_name=id
        data.Mail=ml
        data.Mobile_number=num
        data.save()
        return redirect('/roomdisplay/')
    return render(request,'hotelapp/r_update.html',context)

def delroom_views(request):
    data=add_room.objects.all()
    context={'data':data}
    return render(request,'hotelapp/r_delete.html',context)


def deluser_views(request):
    data=add_user.objects.all()
    context={'data':data}
    if request.method=='POST':
        nm=request.POST.get('name')
        id=request.POST.get('id')
        ml=request.POST.get('mail')
        num=request.POST.get('cnum')
        
        data.Name=nm
        data.Id_name=id
        data.Mail=ml
        data.Mobile_number=num
        data.save()
        return redirect('/delete/')
    return render(request,'hotelapp/u_delete.html',context)
  
  
def deleteuser_view(request,j):
    data=add_user.objects.get(id=j)
    context={'data':data}   
    return render(request,'hotelapp/delete.html',context)


def warning(request,j):
    data=add_user.objects.get(id=j)
    context={'data':data}
    if request.method=='POST':
        data.delete()
        return redirect('/display/')
    return render(request,'hotelapp/areyousure.html',context)

def warning1(request,d):
    data=add_room.objects.get(id=d)
    context={'data':data}
    if request.method=='POST':
        data.delete()
        return redirect('/roomdisplay/')
    return render(request,'hotelapp/room_areUsure.html',context)
    


        





    
