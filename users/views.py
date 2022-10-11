from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView
from .forms import Registration
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


class Register(CreateView):
    template_name = "signin.html"
    form_class = Registration
    success_url = reverse_lazy('login')
    


class ULogin(LoginView):
    template_name = 'login_form.html'

class ULogout(LogoutView):
    success_url = reverse_lazy('login/')

    """""

def login(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('home.html')
        else:
            return('signin.html')


    def user_reg(request):
        if request.method == "POST":
            reg_form = Registration(request.POST)
            if reg_form.is_valid():
                user = reg_form.save()
                login = (request, user)
                messages.success(request, "Successfully registered Welcome")
                return redirect('signin')
            messages.error(request, "Registration is unsuccessful Please try again")
        reg_form = Registration()
        return render(request, {"reg_form":reg_form})

        """""