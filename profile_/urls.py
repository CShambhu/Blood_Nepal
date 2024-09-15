from django.urls import path, include
from profile_ import views
from . views import Profile_list, Sent, Update_Profile, Delete_Profile, Received, Delete_Blood_Request, Msg_Form


urlpatterns = [
    path("login/", views.Login_User, name="login"),
    path("", views.Login_User, name="home"),
    # path("Blood-Nepal", views.Login_User, name="bloodnepal"),
    path("profile", views.profile, name="profile"),
    path("signup", views.save_Signup, name="signup"),
    path("requestblood/<int:id>", views.request_blood, name="requestblood"),
    path("request-sent", Sent.as_view(), name="request-sent"),
    path("request-received", Received.as_view(), name="request-received"),
    path("delete-blood-request/<int:pk>/", Delete_Blood_Request.as_view(), name="delete-blood-request"),
    path('msg/', Msg_Form.as_view(), name='msg'),
    path('logout', views.Logout_User, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('donor', Profile_list.as_view(), name='donor'),
    path('search', views.search, name='search'),
    path('update-profile/<int:pk>/', Update_Profile.as_view(), name='update_profile'),
    path('delete_profile/<int:pk>/', Delete_Profile.as_view(), name='delete_profile'),
    # path('sample', views.loginform, name='sample'),
    # path("save_signup", views.save_Signup, name="save_signup"),
    # path("save_user", views.save_User, name="save_user"),
    # path("employee", views.employee_data, name="employee"),
    # API URLS 
    path('api/', include('profile_.urls_api')),
]

