from django.urls import path
from .views import SignUpView, ContactMeView
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("contactme/", ContactMeView.as_view(), name="contact_me"),

]