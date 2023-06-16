from django.views.generic import View
from account.models import Transaction, Balance
from traning.models import Game, Ages
from django.shortcuts import render, redirect

class MainView(View):
    template_name = 'traning/main.html'

    def get(self, request, *args, **kwargs):
        ages = Ages.objects.all()
        context = {'game_age': ages}
        return render(request, self.template_name, context)
    
    def post(self, request):
        age = request.POST.get('age')
        game = request.POST.get('game')

        user = request.user
        balance = Balance.objects.get(user=user)
        balance.balance -= 1
        balance.save()

        transaction = Transaction.objects.create(user=user, amount=-1)

        age = Ages.objects.get(id=age)
        game_obj = Game.objects.create(user=user, age=age)

        return redirect('traning:game-alphabet')

class AlphabetView(View):
    template_name = 'traning/alphabet_layout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class SoundsView(View):
    template_name = 'traning/sounds_layout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)