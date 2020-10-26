from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='home'),
    path('', RedirectView.as_view(url='login/')),

]
