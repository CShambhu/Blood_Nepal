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
    
    

def update_profile(request, id):
    username = request.user.username # Gets the username of user who is logged in from User table
    signup_user = SignUp.objects.get(id=id)
    form = SignUp_Form(request.POST or None ,request.FILES or None, instance = signup_user) 
    if form.is_valid():
        form.save()
        return redirect('profile')
    else:
        print(form.errors)
    return render(request, 'profile/update_profile.html', {'username':username, 'form':form, 'signup_user': signup_user})

def delete_profile(request, id):
    username = request.user.username # Gets the username of user who is logged in from User table
    signup_user = SignUp.objects.get(id=id)
    if signup_user.delete():
        messages.info(request,("Do you want to delete your profile ?"))
        
        return redirect('home')
    

#User's Signup Form
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
            donate = form.cleaned_data['ready_to_donate']
            last_donation = form.cleaned_data['last_donation']
            em = SignUp.objects.create(
                user = user,
                full_name = name, 
                email = email, 
                phone = phone, 
                gender = gender,
                profile_photo = photo, 
                location = location,
                blood_group = blood,
                weight = weight,
                ready_to_donate = donate,
                last_donation = last_donation

            )
            em.save()
            messages.success(request,("You have successfully completed your profile. Now you can utilize features. "))
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
                
                try :
                    signup_user = SignUp.objects.get(user = request.user)
                    # messages.success(request,('blood request sent.'))
                    return render(request, "profile/home.html", {'signup_user':signup_user, 'username': username})
                
                except SignUp.DoesNotExist:
                    messages.success(request,("Your data is incomplete. Please visit your profile."))
                    return redirect('home')
                
                 
            else:
                messages.error(request, "Incorrect Username and Password")
                return redirect('home') 
    if next_url:
        messages.info(request, 'Login is required.')
    
    return render(request, 'profile/home.html', context)

#Register User
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
def request_blood(request,id):
    username = request.user.username # Gets the username of user who is logged in from User table
    # Get the full data of donor to whom user is requesting 
    signup_donor = SignUp.objects.get(id = id) # gets the data of donor when requestblood is clicked
    signup_user = SignUp.objects.all() # gets the full data of donor on requestblood page. 
    P_Form = PatientsForm()
    user_profile = SignUp.objects.filter(user=request.user).exists()
    if user_profile:
        if request.method == "POST":
            user = request.user
            signup = SignUp.objects.get(user=request.user) # gets the signup foreign key of the logged in user
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
                messages.success(request,(f'You have sent blood request to {signup_donor}.'))
                return redirect( "home")    
            else:
                P_Form = PatientsForm()
    else:
        messages.success(request,('Please complete your profile to request blood.'))
        return redirect('signup')
    return render(request, "profile/requestblood.html", {'P_Form':P_Form, 'username':username,'signup':signup_donor,'signup_user':signup_user})

