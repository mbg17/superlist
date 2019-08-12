from django.shortcuts import render,redirect

# Create your views here.
from .models import Publisher
def publisher_list(request):
    ret = Publisher.objects.all().order_by('id')
    return render(request,'publisher_list.html',{'publisher_list':ret})

def add_publisher(request):
    if request.method=='POST':
        new_publisher = request.POST.get('publisher',None)
        Publisher.objects.create(name=new_publisher)
        return redirect('/publisher_list/')
    return render(request,'add_publisher.html')