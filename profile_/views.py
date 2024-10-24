from django.conf import settings
from django.db.models.query import QuerySet
# from django.http import HttpRequest
from django.http import HttpRequest
from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
# from django.views import View
from profile_.forms import SignUp_Form, PatientsForm, MessageForm
from .models import SignUp, Patient, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, UpdateView , DeleteView, FormView
from datetime import date, timedelta
from django.utils import timezone
from blood_banks.models import BloodBanks

from django.core.mail import send_mail

from allauth.socialaccount.models import SocialAccount

#Searching on basis of location/blood_group
@login_required
def search(request):
    username = request.user.username
    if request.method == "POST":
        searched = request.POST.get("searched","")
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
    # paginate_by = 4

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)
        # Add extra context
        context['username'] = self.request.user.username
        return context

    
def home(request):
    return render(request, "profile/home.html")

#profile of User who is logged in
@login_required
def profile(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    try:
        signup_user = SignUp.objects.get(user = request.user)
        return render(request, "profile/profile.html", {'signup_user':signup_user, 'username': username})
    
    except SignUp.DoesNotExist:
        # messages.success(request,('Please fill up the below form to use features.'))
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

#Logout User
def Logout_User(request):
    logout(request)
    # messages.error(request, ("You are logged out"))
    return redirect('home') 

#User's Signup Form
def save_Signup(request):
    username = request.user.username # Gets the username of user who is logged in from User table
    id = request.user.id
    form = SignUp_Form() 
    user = request.user
    email = user.email
    social_account = SocialAccount.objects.filter(user=user, provider='google').first()
    facebook_account = SocialAccount.objects.filter(user=user, provider='facebook').first()

    # Prepopulate full_name and email if social_account exists
    initial_data = {}
    if social_account:
        initial_data['full_name'] = social_account.extra_data.get('name', '')
        initial_data['email'] = user.email
    elif facebook_account:
        extra_data = social_account.extra_data
        initial_data['full_name'] = extra_data.get('name', '')
        initial_data['email'] = extra_data.get('email', user.email) 
        # initial_data['email'] = user.email

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
            last_donation = form.cleaned_data['last_donation']
            ready_to_donate = form.cleaned_data['ready_to_donate']
            
            # # Initialize ready_to_donate with default value
            # ready_to_donate = 'no'

            # if last_donation:
            #     # Ensure last_donation is a date object
            #     if isinstance(last_donation, str):
            #         # Convert string to date if necessary
            #         last_donation = timezone.datetime.strptime(last_donation, "%Y-%m-%d").date()

            #     # Calculate the date 3 months ago from today
            #     three_months_ago = timezone.now().date() - timedelta(days=90)

            #     # Check if the last donation was more than 3 months ago
            #     if last_donation <= three_months_ago:
            #         ready_to_donate = 'yes'
                
            #     # Debugging prints (Remove or comment out in production)
            #     print("Last donation:", last_donation)
            #     print("Three months ago:", three_months_ago)
            #     print("Ready to donate:", ready_to_donate)
            
            # Check if email already exists
            if not SignUp.objects.filter(email=email).exists():
                # messages.info(request, "This email address is already in use.")
                # return render(request, 'profile/signup.html', context)
            
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
                                ready_to_donate = ready_to_donate,
                                last_donation = last_donation

                            )
                em.save()
                messages.success(request,("You have successfully completed your profile. Now you can utilize features. "))
                return redirect('profile')
            else:
                messages.info(request, "This email address is already in use.")
                return redirect('signup')
    else:
        form = SignUp_Form(initial= initial_data)
    context =  {'form': form, 'username': username, 'id':id, 'username':user.username, 'email':user.email, 'id': user.id}
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
                # messages.success(request, (f" Welcome "+username+"."))
                
                try :
                    bankdetails = BloodBanks.objects.all()
                    signup_user = SignUp.objects.get(user = request.user)
                    # messages.success(request,('blood request sent.'))
                    return render(request, "profile/home.html", {'signup_user':signup_user, 'username': username, 'bankdetails':bankdetails})
                
                except SignUp.DoesNotExist:
                    messages.success(request,("Your data is incomplete. Please visit your profile."))
                    return redirect('home')  
            else:
                messages.error(request, "Incorrect Username and Password")
                return redirect('home') 
    if next_url:
        messages.info(request, 'Login is required.')
        return redirect('home') 

    
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




# #Patient's Blood Request Form
@login_required(login_url='/login/')
def request_blood(request, id):
    username = request.user.username
    signup_donor = get_object_or_404(SignUp, id=id)
    EMAIL_RECIPIENT = signup_donor.email
    # Instead of get_object_or_404, use filter and check existence
    signup = SignUp.objects.filter(user=request.user).first()
    
    if signup is None:
        messages.error(request, 'Please complete your profile to request blood.')
        return redirect('donor')
    
    full_name = signup.full_name
    P_Form = PatientsForm()

    if request.method == "POST":
        user = request.user
        blood_request_sent_by = signup
        blood_request_sent_to = signup_donor
        
        P_Form = PatientsForm(request.POST, request.FILES)
        if P_Form.is_valid():
            patients_name = P_Form.cleaned_data['patients_name']
            hospital = P_Form.cleaned_data['hospital']
            patients_department = P_Form.cleaned_data['patients_department']
            patients_phone = P_Form.cleaned_data['patients_phone']
            patients_blood_group = P_Form.cleaned_data['patients_blood_group']
            blood_pint = P_Form.cleaned_data['blood_pint']
            requisition_form = P_Form.cleaned_data['requisition_form']
            required_date = P_Form.cleaned_data['required_date']
            message = P_Form.cleaned_data['message']

            today = date.today()
            if blood_request_sent_to.blood_group == patients_blood_group:
                if required_date >= today:
                    Patient.objects.create(
                        user=user,
                        blood_request_sent_by=blood_request_sent_by,
                        blood_request_sent_to=blood_request_sent_to,
                        patients_name=patients_name,
                        hospital=hospital,
                        patients_department=patients_department,
                        patients_phone=patients_phone,
                        patients_blood_group=patients_blood_group,
                        blood_pint=blood_pint,
                        requisition_form=requisition_form,
                        required_date=required_date,
                        message=message,
                    )
                    login_url = f"{request.build_absolute_uri(reverse('login'))}?next"
                    # subject = f'Blood Request From: User {user}'  # Make sure this is an instance
                    subject = f'Blood Request From: {full_name}'  # Make sure this is an instance
                    message = (
                                f'Greetings, {signup_donor}\n'
                                f'fullname:{full_name} (username: {user}) has requested {patients_blood_group.title()} blood for '
                                f'patient "{patients_name.title()}" who is admitted at {hospital.title()} hospital. \n'
                                f'Blood Required Date: {required_date} \n'
                                f'Message: {message.title()} \n'
                                f'Please login to check out more details at {login_url}'
)
                    email_from = settings.DEFAULT_FROM_EMAIL
                    recipient_list = [EMAIL_RECIPIENT]  # Add the recipient email
                    send_mail(subject, message, email_from, recipient_list)
                    messages.success(request, f'You have sent a blood request to {signup_donor}.')
                    return redirect("profile")
                else:
                    messages.error(request, "Oops! Looks like you have entered past dates.")
            else:
                messages.error(request, "Blood group does not match with the donor's.")
        else:
            print(P_Form.errors)
            messages.error(request, 'There was an error in the form. Please correct it and try again.')
    
    return render(request, "profile/requestblood.html", {'P_Form': P_Form, 'username': username, 'signup': signup_donor})

# @login_required(login_url='/login/')
# def request_blood(request,id):
#     username = request.user.username # Gets the username of user who is logged in from User table
#     # Get the full data of donor to whom user is requesting 
#     signup_donor = SignUp.objects.get(id = id) # gets the data of donor when requestblood is clicked
#     # EMAIL_RECIPIENT = signup_donor.email
#     signup = get_object_or_404(SignUp, user=request.user)
#     # Retrieve the full name
#     full_name = signup.full_name
#     P_Form = PatientsForm()
#     user_profile = SignUp.objects.filter(user=request.user).exists()
#     if user_profile:
#         if request.method == "POST":
#             user = request.user
#             blood_request_sent_by = SignUp.objects.get(user=request.user) # gets the signup foreign key of the logged in user
#             blood_request_sent_to = SignUp.objects.get(id=id)
#             P_Form = PatientsForm(request.POST,request.FILES)
#             if P_Form.is_valid():
#                 patients_name = P_Form.cleaned_data['patients_name']
#                 hospital = P_Form.cleaned_data['hospital']
#                 patients_department = P_Form.cleaned_data['patients_department']
#                 patients_phone = P_Form.cleaned_data['patients_phone']
#                 patients_blood_group = P_Form.cleaned_data['patients_blood_group']
#                 blood_pint = P_Form.cleaned_data['blood_pint']
#                 requisition_form = P_Form.cleaned_data['requisition_form']
#                 required_date = P_Form.cleaned_data['required_date']
#                 message = P_Form.cleaned_data['message']

#                 today = date.today()
#                 if blood_request_sent_to.blood_group == patients_blood_group:
#                     if required_date >= today:
#                         am = Patient.objects.create(
#                                 user = user,
#                                 blood_request_sent_by = blood_request_sent_by,
#                                 blood_request_sent_to = blood_request_sent_to,
#                                 patients_name = patients_name,
#                                 hospital = hospital,
#                                 patients_department = patients_department,
#                                 patients_phone = patients_phone,
#                                 patients_blood_group = patients_blood_group,
#                                 blood_pint = blood_pint,
#                                 requisition_form = requisition_form,
#                                 required_date = required_date,
#                                 message = message,
                                
#                             )
#                         am.save()

#                         messages.success(request,(f'You have sent blood request to {signup_donor}.'))
#                         return redirect( "profile")
#                     else:
#                         messages.error(request, "Ooops ! Looks like you have entered past dates")  
#                 else:
#                     messages.error(request, "Blood group does not match with the donor's.")  
#             else:
#                 # Add this to debug form errors
#                 print(P_Form.errors)
#                 messages.error(request, 'There was an error in the form. Please correct it and try again.')  
#         else:
#             P_Form = PatientsForm()
#     else:
#         messages.success(request,(f'Please complete your profile to request blood.'))
#         return redirect('donor')
#     return render(request, "profile/requestblood.html", {'P_Form':P_Form, 'username':username,'signup':signup_donor})



class Sent(ListView):
    context_object_name = 'patients'
    template_name = "profile/sent.html"
    paginate_by = 2
    def get_queryset(self):
        user = self.request.user
        try:
            sign_up = SignUp.objects.get(user=user)
            return Patient.objects.filter(blood_request_sent_by=sign_up)
        except SignUp.DoesNotExist:
            messages.success(self.request, 'You have not requested for blood yet.')
    
    def get_context_data(self):
        context = super().get_context_data()
        context['username'] = self.request.user.username
        context['current_date'] = timezone.now().date()
        return context


class Received(Sent):
    template_name = "profile/received.html"

    def get_queryset(self):
        user = self.request.user
        try:
            sign_up = SignUp.objects.get(user=user)
            return Patient.objects.filter(blood_request_sent_to=sign_up)
        except SignUp.DoesNotExist:
            messages.success(self.request, 'You have not received any blood request yet.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['current_date'] = timezone.now().date()

        return context

class Delete_Blood_Request(DeleteView):
    template_name = "profile/delete_blood_request.html"
    model = Patient
    success_url = reverse_lazy('request-received')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context
    
    def post(self, request, *args, **kwargs):
        messages.info(request,"You deleted a request.")
        return super().post(request, *args, **kwargs)

#to display msg form so requester can send msg to donor in received.html
class Msg_Form(FormView):
    template_name = "profile/msg.html"
    form_class = MessageForm
    success_url = reverse_lazy('request-received')
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context

#to display msg of donor back to requester sent.html 
class View_(FormView):
    template_name = "profile/request-sent.html"
    get_context_data = 'Msg'
    model = Message
    # success_url = reverse_lazy('request-received')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context
    
    













