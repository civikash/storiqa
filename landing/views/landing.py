from django.views.generic import View
from django.shortcuts import render, redirect

class AppView(View):
    template_name = 'landing/base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)