from django.contrib import admin

from .models import Class, Student, Record

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Record)