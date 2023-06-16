from django.views.generic import View
from django.shortcuts import render, redirect

class ProfileView(View):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)