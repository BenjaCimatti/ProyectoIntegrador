from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.homePage, name='home'),
    path('ver_torneos/', views.verTorneos, name='ver_torneos'),
    path('torneo/<str:pk>/', views.Torneo, name='torneo'),
    path('', RedirectView.as_view(url='login/')),

    #cambiar contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="AdministradorTorneos/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="AdministradorTorneos/password_reset_sent.html"), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
