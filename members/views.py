from django.views import generic
from django.urls import reverse_lazy
from .forms import SigUpForm


# view for user registration
class UserRegisterView(generic.CreateView):
    form_class = SigUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
