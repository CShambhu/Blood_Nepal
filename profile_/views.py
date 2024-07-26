from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
# from django import forms
from .forms import SignUp_Form, PatientsForm
from .models import SignUp, Patient

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
#Searching on basis of location/blood_group
@login_required
def search(request):
    username = request.user.username
    if request.method == "POST":
        searched = request.POST["searched"]
        # pattern = r'^(a|A|b|B|o|O|ab|AB)(\+|-)$'
        # blood_search = SignUp.objects.filter(blood_group__regex = pattern)
        blood_search = SignUp.objects.filter(blood_group__iexact = searched)
        location_search = SignUp.objects.filter(location__contains = searched)
        return render(request, "profile/search.html", {'username':username,'searched':searched, 'blood_search':blood_search, 'location_search':location_search})

    else:    
        return render(request, "profile/search.html", {'username':username})
    

# Donors Profile
@login_required
def donors_profile(request):
    username = request.user.username
    donor = SignUp.objects.all()
    return render(request, "profile/donor.html", {'donor': donor, 'username': username})

def home(request):
    return render(request, "profile/home.html")

def about(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    context = {'username':username}
    return render(request, "profile/about.html",context)

#profile of User who is logged in
@login_required
def profile(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    try:
        signup_user = SignUp.objects.get(user = request.user)
        return render(request, "profile/profile.html", {'signup_user':signup_user, 'username': username})
    except SignUp.DoesNotExist:
        messages.success(request,('Please fill up the below form to use features.'))
        return redirect('signup')

def update_profile(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    signup_user = SignUp.objects.get(user = request.user)
    form = SignUp_Form(request.POST) 
    if form.is_valid():
        form.save
        return redirect('profile')
    return render(request, 'profile/update_profile.html', {'username':username, 'form':form, 'signup_user':signup_user})

#User's Signup Form
@login_required
def save_Signup(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    id = request.user.id
    form = SignUp_Form() 
    context =  {'form': form, 'username': username, 'id':id}
    if (request.method=="POST"):
        user = request.user
        form = SignUp_Form(request.POST,request.FILES)
        if (form.is_valid()):
            name =  form.cleaned_data['full_name']
            email =  form.cleaned_data['email']
            phone =  form.cleaned_data['phone']
            gender =  form.cleaned_data['gender']
            photo =  form.cleaned_data['profile_photo']
            location =  form.cleaned_data['location']
            blood =  form.cleaned_data['blood_group']
            weight =  form.cleaned_data['weight']

            em = SignUp.objects.create(user = user,
                full_name = name, 
                email = email, 
                phone = phone, 
                gender = gender,
                profile_photo = photo, 
                location = location,
                blood_group = blood,
                weight = weight,

            )
            em.save()
            messages.success(request,("You have successfully completed your profile"))
            return redirect('profile')
        else:
            form = SignUp_Form()
    return render(request, 'profile/signup.html', context)

#Login Authentication for User
def Login_User(request):
    next_url = request.GET.get('next')  # Get 'next' parameter to redirect after login
    username = request.user.username # Gets the username of user who is logged in from User table
    context = {'username':username}
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, (f" Welcome "+username+"."))
                try:
                    signup_user = SignUp.objects.get(user = request.user)
                    return render(request, "profile/home.html", {'signup_user':signup_user, 'username': username})
                except SignUp.DoesNotExist:
                    messages.success(request,('Your data is incomplete. Please visit your profile.'))
                    return redirect('home')
                 
            else:
                messages.error(request, "Incorrect Username and Password")
                return redirect('home') 
    if next_url:
        messages.info(request, 'Login is required.')
    
    return render(request, 'profile/home.html', context)

#Register User
def register_user(request):
    # username = request.user.username # Gets the username of user who is logged in from User table
    # context = {'username':username}
    # messages.info(request,('you are already registered'))
    # return render(request, "home.html", context)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username = username, password = password)
            # login(request, user)
            messages.success(request, ('Registration Successful'))
            return redirect('home')
    else:
        form = UserCreationForm()      
    return render(request, 'profile/register.html', {'form': form})

#Logout User
def Logout_User(request):
    logout(request)
    messages.error(request, ("You are logged out"))
    return redirect('home') 

#Patient's Blood Request Form
@login_required
def save_patient(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    P_Form = PatientsForm()
    if request.method == "POST":
        user = request.user
        signup, created = SignUp.objects.get_or_create(user=user, defaults={'full_name': user.get_full_name(), 'email': user.email})

        P_Form = PatientsForm(request.POST,request.FILES)
        if P_Form.is_valid():
            full_name = P_Form.cleaned_data['full_name']
            hospital = P_Form.cleaned_data['hospital']
            patient_department = P_Form.cleaned_data['patients_department']
            patients_phone = P_Form.cleaned_data['patients_phone']
            patients_blood_group = P_Form.cleaned_data['patients_blood_group']
            blood_pint = P_Form.cleaned_data['blood_pint']
            requisition_form = P_Form.cleaned_data['requisition_form']
            am = Patient.objects.create(
                user = user,
                signup = signup,
                full_name = full_name,
                hospital = hospital,
                patients_department = patient_department,
                patients_phone = patients_phone,
                patients_blood_group = patients_blood_group,
                blood_pint = blood_pint,
                requisition_form = requisition_form
            )
            am.save()
            try:
                signup_user = SignUp.objects.get(user = request.user)
                messages.success(request,('blood request sent.'))
                return render(request, "profile/home.html", {'signup_user':signup_user, 'username': username})
            except SignUp.DoesNotExist:
                messages.success(request,('Please complete your profile to request blood.'))
                return redirect('requestblood')    
        else:
            P_Form = PatientsForm()
    return render(request, "profile/requestblood.html", {'P_Form':P_Form, 'username':username})

# Get the full data of user 
def users_data(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    full_name = request.user.full_name
    try:
        signup_user = SignUp.objects.get(full_name = request.full_name)
        return render(request, "profile/requestblood.html", {'signup_user':signup_user, 'username': username, 'full_name':full_name})
    except SignUp.DoesNotExist:
        messages.success(request,("Couldn't get data"))
        return redirect('requestblood')

