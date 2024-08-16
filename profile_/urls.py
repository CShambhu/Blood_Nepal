from django.urls import path
from .import views
from .views import Profile_list, Sent, Update_Profile, Delete_Profile
# , Request_Blood, History

urlpatterns = [
    path("", views.Login_User, name="home"),
    path("about", views.about, name="about"),
    path("profile", views.profile, name="profile"),
    # path("update-profile", views.update_profile, name="update-profile"),
    path("login/", views.Login_User, name="login"),
    path("signup", views.save_Signup, name="signup"),
    path("requestblood/<int:id>", views.request_blood, name="requestblood"),
    # path('request/<int:pk>/', Request_Blood.as_view(), name='request'),

    path("sent", Sent.as_view(), name="sent"),
    # path("history", views.history, name="history"),

    # path("requestblood/<int:id>/", views.users_data, name="requestblood"),
    path('logout', views.Logout_User, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('donor', Profile_list.as_view(), name='donor'),
    path('search', views.search, name='search'),
    path('update-profile/<int:pk>/', Update_Profile.as_view(), name='update_profile'),

    # path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    # path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),
    path('delete_profile/<int:pk>/', Delete_Profile.as_view(), name='delete_profile'),




   


    # path('sample', views.loginform, name='sample'),
    # path("save_signup", views.save_Signup, name="save_signup"),
    # path("save_user", views.save_User, name="save_user"),
    # path("employee", views.employee_data, name="employee"),
]