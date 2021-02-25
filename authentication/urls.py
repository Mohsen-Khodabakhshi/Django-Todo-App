from django.urls import path

from .views import home, signIn, signUp, logOut

urlpatterns = [
    path('', home),
    path('signin/', signIn),
    path('signup/', signUp),
    path('logout/', logOut),
]