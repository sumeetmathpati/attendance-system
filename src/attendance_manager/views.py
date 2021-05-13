from django.shortcuts import render, redirect, get_object_or_404
from .forms import TakeAttendance
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import arpreq
from .models import Student, Record, Class
from django.core.mail import send_mail
from datetime import datetime, timedelta


def index(request):
    context = {}
    if request.method == 'POST':

        if request.user.is_authenticated:

            form = TakeAttendance(request.POST) 
            if form.is_valid():
                email = request.user.email
                class_name = get_object_or_404(Class, title=form.cleaned_data.get('class_name'))
                from_date = form.cleaned_data.get('from_date')
                to_date = form.cleaned_data.get('to_date')
                print(f'{class_name}, {email}, {from_date}, {to_date}')
                
                # students = Student.objects.filter(class_name=class_name)
                records = Record.objects.filter(present_time__gte=from_date, present_time__lt=to_date).distinct('student')

                if records:
                    print(records)
                return redirect('index')
    else:
        if request.user.is_authenticated:
            form = TakeAttendance()
            context['form'] = form

    return render(request, 'attendance_manager/index.html', context)


@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        print(f"roll_no: {request.POST.get('id')}")
    else:
        print('*************')
    request_mac = arpreq.arpreq(get_client_ip(request))
    student_with_mac = Student.objects.filter(mac=request_mac)
    if (student_with_mac):
        record = Record(student=student_with_mac.first())
        record.save()
    else:
        print('Not a student')
    print(' ')
    return HttpResponse(status=200)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def delete_old_records():
    Record.objects.filter(present_time__lt=datetime.now()-timedelta(days=5)).delete()

def get_attendance():
    mac_list = []
    for i in range(1, 255):
        request_mac = arpreq.arpreq(f'192.168.0.{i}')
        if request_mac:
            student_with_mac = Student.objects.filter(mac=str(request_mac).strip())
            if student_with_mac.exists():
                record = Record(student=student_with_mac.first())
                record.save() 

    