from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

class LoginView(View):
    template_name = 'app.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:profile')
        else:
            messages.error(request, 'Неправильный email или пароль')
        return redirect(request.META.get('HTTP_REFERER'))