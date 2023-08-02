from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfigTest(TestCase):
    def test_sectet_key_sterngth(self):
            try:
                is_strong = validate_password(settings.SECRET_KEY)
            except Exception as e :
                msg = f'weak secret key {e.messages}'
                self.fail(msg)