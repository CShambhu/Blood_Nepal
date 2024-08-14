from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import SignUp_Form, PatientsForm
from .models import SignUp, Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, UpdateView , DeleteView

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
        searched = request.POST["searched"]   
        return render(request, "profile/search.html", {'username':username})

# Donors Profile
class Profile_list(LoginRequiredMixin,ListView):
    # username = request.user.username
    model = SignUp
    template_name = 'profile/donor.html'
    context_object_name = 'donors'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)
        # Add extra context
        context['username'] = self.request.user.username
        return context

    
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
    
    
class Update_Profile(UpdateView):
    model = SignUp
    template_name = 'profile/update_profile.html'
    form_class = SignUp_Form
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Get the object to be updated
        obj = super().get_object(queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


# def update_profile(request, id):
#     username = request.user.username # Gets the username of user who is logged in from User table
#     signup_user = SignUp.objects.get(id=id)
#     form = SignUp_Form(request.POST or None , request.FILES or None, instance = signup_user) 
#     if form.is_valid():
#         form.save()
#         return redirect('profile') 
#     return render(request, 'profile/update_profile.html', {'username':username, 'form':form, 'signup_user': signup_user})

class Delete_Profile(DeleteView):
    template_name = "profile/delete_profile.html"
    model = SignUp
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context
    
    def post(self, request, *args, **kwargs):
        messages.info(request,"Your account has been deleted successfully")
        return super().post(request, *args, **kwargs)

# def delete_profile(request, id):
#     username = request.user.username # Gets the username of user who is logged in from User table
#     signup_user = get_object_or_404(SignUp, id=id)
#     if request.method == 'POST':
#         signup_user.delete()
#         messages.info(request,( 'Your account has been deleted successfully.'))
#         return redirect('home')
#     return render(request, 'profile/delete_profile.html', {'username':username, 'signup_user':signup_user})

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
    # signup_user = SignUp.objects.all() # gets the full data of donor on requestblood page. 
    P_Form = PatientsForm()
    user_profile = SignUp.objects.filter(user=request.user).exists()
    if user_profile:
        if request.method == "POST":
            user = request.user
            blood_requested_by = SignUp.objects.get(user=request.user) # gets the signup foreign key of the logged in user
            blood_requested_to = SignUp.objects.get(id=id)
            P_Form = PatientsForm(request.POST,request.FILES)
            if P_Form.is_valid():
                patients_name = P_Form.cleaned_data['patients_name']
                hospital = P_Form.cleaned_data['hospital']
                patients_department = P_Form.cleaned_data['patients_department']
                patients_phone = P_Form.cleaned_data['patients_phone']
                patients_blood_group = P_Form.cleaned_data['patients_blood_group']
                blood_pint = P_Form.cleaned_data['blood_pint']
                requisition_form = P_Form.cleaned_data['requisition_form']
                required_date = P_Form.cleaned_data['required_date']
                am = Patient.objects.create(
                    user = user,
                    blood_requested_by = blood_requested_by,
                    blood_requested_to = blood_requested_to,
                    patients_name = patients_name,
                    hospital = hospital,
                    patients_department = patients_department,
                    patients_phone = patients_phone,
                    patients_blood_group = patients_blood_group,
                    blood_pint = blood_pint,
                    requisition_form = requisition_form,
                    required_date = required_date
                )
                am.save()
                messages.success(request,(f'You have sent blood request to {signup_donor}.'))
                return redirect( "profile")  
            else:
                # Add this to debug form errors
                print(P_Form.errors)
                messages.error(request, 'There was an error in the form. Please correct it and try again.')  
        else:
            P_Form = PatientsForm()
    else:
        messages.success(request,('Please complete your profile to request blood.'))
        return redirect('signup')
    return render(request, "profile/requestblood.html", {'P_Form':P_Form, 'username':username,'signup':signup_donor})

class History(ListView):
    context_object_name = 'patients'
    template_name = "profile/history.html"
    paginate_by = 2
    def get_queryset(self):
        user = self.request.user
        try:
            sign_up = SignUp.objects.get(user=user)
            return Patient.objects.filter(blood_requested_by=sign_up)
        except SignUp.DoesNotExist:
            messages.success(self.request, 'You have not requested for blood yet.')
    
    def get_context_data(self):
        context = super().get_context_data()
        context['username'] = self.request.user.username
        return context
