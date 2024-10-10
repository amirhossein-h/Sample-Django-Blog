from django.views import generic
from .models import ContactMe
from .forms import SignUpForm, ContactMeForm
from django.urls import reverse_lazy
from django.contrib import messages


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class ContactMeView(generic.CreateView):
    model = ContactMe
    form_class = ContactMeForm
    template_name = "accounts/contactme.html"
    context_object_name = "contactme"
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        messages.success(self.request, "Thank you for sending message to us. We will respond you ASAP!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = ContactMeForm()
        return context