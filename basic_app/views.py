from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy,reverse

from . import models
# from . import forms
from .forms import UserForm,UserProfileInfoForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class based http response")

class IndexView(TemplateView):
    template_name ='basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'basic injection'

        return context
class SchoolListView(ListView):
    """docstring for  SchoolListView."""
    context_object_name = 'schools'
    model = models.School
    #this returns school_list by default by framework
    print('======school list view is called')
    template_name = 'basic_app/school_list2.html'
    #if template_name is not defined, system will use school_list.html as default html

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    #this by default return school as school details.
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    #template_name = ''
    #default system is loooking for school_form.html
class SchoolUpdateView(UpdateView):

    # why i cannot just put one field??
    fields = ('principal',)
    model = models.School
class SchoolDeleteView(DeleteView):
    """docstring for SchoolDeleteView."""
    model = models.School
    success_url = reverse_lazy("basic_app:list")

# class UserRegisterView(CreateView):
#     context_object_name = 'registerProfile'
#     model = models.UserProfileInfo
#     #successful_url = reverse_lazy("basic_app:user_list")
#     template_name = 'basic_app/register.html'

class StudentCreateView(CreateView):

        fields = ('name','age','school')
        model = models.Student
        template_name = 'basic_app/student_form.html'

class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student
    #this by default return school as school details.
    template_name = 'basic_app/student_detail.html'

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:student_list")

class StudentListView(ListView):
    """docstring for StudentList."""
    context_object_name = 'students'
    model = models.Student
    # use default naming, student_list

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
            else:
                print('-----NOT PROFLE IMAGE found!------')
            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    print(request.POST)
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')


        user = authenticate(username=user_name,password=user_password)

        if user:
            if user.is_active:
                login(request,user)
                print(f'------welcome {user_name}login---------')
                return HttpResponseRedirect(reverse('basic_app:list'))
            else:
                return HttpResponse("uaser account is not active")
        else:
            print("some one tried login but not successful")
            print(f'user name is {user_name}, and passwor is {user_password}')


    return render(request,'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    print('logout is called===')
    return HttpResponseRedirect(reverse('basic_app:login_NS'))
