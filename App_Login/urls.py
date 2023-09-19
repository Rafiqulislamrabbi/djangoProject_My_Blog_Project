from django.urls import path
from App_Login import views

from django.conf import settings
# from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf.urls.static import static
app_name = 'App_Login'

urlpatterns=[
    path("",views.sign_up,name="signup"),
    path("login/",views.login_page,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("change_profile/",views.user_chance,name="user_chance"),
    path("change_pass/",views.pass_change,name="pass_change"),
    path("add_picture/",views.upload_profile_picture,name="add_profile_pic"),
    path("change_picture/",views.change_profile_pic,name="change_profile_pic"),

]





