from django.views.generic import View
import random
import string
from traning.models import Game, Ages
from django.http import JsonResponse
from django.shortcuts import render, redirect

class GameAlphabetView(View):
    template_name = 'traning/games/alphabet.html'

    def letters(self):
        return list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    def get(self, request, *args, **kwargs):
        letters = self.letters()
        correct_letter = random.choice(letters)

        request.session['correct_letter'] = correct_letter

        random_letters = random.sample(letters, 3)
        options = random_letters + [correct_letter]
        random.shuffle(options)
        context = {'letters': options, 'correct_letter': correct_letter}
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse(context)  # Возвращаем JSON-ответ для AJAX-запроса
        else:
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        selected_letter = request.POST.get('letter')
        letters = self.letters()
        correct_letter = request.session.get('correct_letter')
        correct = (selected_letter == correct_letter)

        if 'letter' in request.POST and correct:
            new_letters = random.sample(letters, 3) + [correct_letter]
            random.shuffle(new_letters)
        else:
            new_letters = request.POST.getlist('letters[]')
        
        response_data = {
            'correct': correct,
            'letters': new_letters,
            'correct_letter': correct_letter
        }
        
        return JsonResponse(response_data)
