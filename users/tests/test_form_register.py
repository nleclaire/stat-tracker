from unittest import TestCase

from django.contrib.auth.forms import UserCreationForm


class TestRegisterForm(TestCase):
    def test_form_has_3_fields(self):
        form = UserCreationForm()
        expected = ['username', 'password1', 'password2']
        fields = list(form.fields)
        self.assertSequenceEqual(expected, fields)
