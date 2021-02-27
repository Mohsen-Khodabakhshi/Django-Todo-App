from django.urls import path

from .views import auth, signIn, signUp, logOut

app_name = 'authentication'
urlpatterns = [
    path('', auth, name="auth"),
    path('signin/', signIn, name="signin"),
    path('signup/', signUp, name="signup"),
    path('logout/', logOut, name="logout"),
]