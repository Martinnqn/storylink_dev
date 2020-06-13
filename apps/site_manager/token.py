from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, userid, timestamp):
        return (six.text_type(userid) + six.text_type(timestamp) + six.text_type(True))
account_activation_token = TokenGenerator()