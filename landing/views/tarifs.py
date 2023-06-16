from django.views.generic import View
from django.shortcuts import render, redirect

class TarifsView(View):
    template_name = 'landing/tarifs/tarifs.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)