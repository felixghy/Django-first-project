from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):

    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:sch_detail',kwargs={'pk':self.id})

class Student(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('basic_app:student_detail_URL',kwargs={'pk':self.id})

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):

    #create relationship (dont inherit from user!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    # def get_absolute_url(self):
    #     return reverse('basic_app:register',kwargs={'pk':self.id})

    def __str__(self):
        return self.user.username
