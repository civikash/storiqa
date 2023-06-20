from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class AccountActivation(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.id) + text_type(timestamp) +
           text_type(user.accountinformation.email_confirmed)
        )
account_activation_token = AccountActivation()
