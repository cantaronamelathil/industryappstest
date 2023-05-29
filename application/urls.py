from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.CustomLogin.as_view(),name='userlogin'),
    # path('customlogout/',views.LogoutView.as_view(),name='logout'),
    path('home/',views.Home.as_view(),name='home'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    
]


