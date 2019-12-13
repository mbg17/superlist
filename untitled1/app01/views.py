from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from app01.models import *
from django.utils import timezone
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/index/')
    return render(request,'login.html')


def index(request):
    html = ''
    date = request.GET.get('date',timezone.now().date())
    print(date)
    time_choices = Book.time_list
    room_list = Room.objects.all()
    book_list = Book.objects.all().filter(date=date)
    for room in room_list:
        html+=f'<tr><td>{room.caption}({room.num})</td>'
        for time in time_choices:
            flag = False
            for book in book_list:
                if book.room.id ==room.id and book.time == time[0]:
                    flag=True
                    break
            if flag:
                if request.user.id == book.user.id:
                    html+=f'<td class="active item" room_id ={room.id} time_id={time[0]}>{book.user.username}</td>'
                else:
                    html += f'<td class="another_active item" room_id ={room.id} time_id={time[0]}>{book.user.username}</td>'
            else:
                html += f'<td class="item" room_id ={room.id} time_id={time[0]}></td>'
    html+='</tr>'
    return render(request,'index.html',{'time_choices':time_choices,'html':html})

def book(request):
    print(request.POST)
    return HttpResponse(request.POST.get('POST_DATE'))