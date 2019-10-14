from django.contrib import admin
from .models import School,Student,UserProfileInfo
from .models import UserProfileInfo
# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(UserProfileInfo)
