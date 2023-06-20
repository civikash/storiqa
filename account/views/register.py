from account.views.tokens import account_activation_token
from account.models import Account
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.password_validation import validate_password


class RegisterView(View):
    template_name = 'landing/base.html'
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password1 = request.POST.get('password')

        # Проверка на наличие пользователя с таким email
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'Пожалуйста, проверьте правильность пароля и Email')
            return render(request, self.template_name)
     

        # Создание аккаунта
        user = Account.objects.create_account(email=email, password=password1)
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        mail_subject = 'Активация аккаунта на сайте Сторика'
        message = render_to_string('account/emails/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(str(user.id))),
            'token': account_activation_token.make_token(user),
        })
        to_email = email
        email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
        email.attach_alternative(message, 'text/html')
        email.send()

        messages.success(
            request, 'Пожалуйста, подтвердите адрес электронной почты')
        return redirect('landing:landing')


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(id=uid, is_active=False)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.accountinformation.email_confirmed = True
            user.save()
            messages.success(
                request, ('Ваша учетная запись подтверждена. Пожалуйста, авторизуйтесь'))
            return redirect('landing:landing')
        else:
            messages.warning(
                request, ('Ссылка для подтверждения была недействительной, возможно, потому, что она уже использовалась'))
            return redirect('landing:landing')
