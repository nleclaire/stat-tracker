from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from .views import register


class RegisterTests(TestCase):
    def setUp(self):
        url = reverse('users:register')
        self.response = self.client.get(url)

    def test_register_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_register_url_resolves_register_view(self):
        view = resolve('/users/register')
        self.assertEquals(view.func, register)

    def test_csrf_token(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)


class SuccessfulRegisterTests(TestCase):
    def setUp(self):
        url = reverse('users:register')
        data = {
            'username': 'test',
            'password1': 'test_pass_12345',
            'password2': 'test_pass_12345',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('run_stats:index')

    def test_redirect(self):
        """A successful sign in should redirect to the home screen."""
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        """A User object should be created."""
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        """Created User should be authenticated on arbitrary new page."""
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidRegisterTests(TestCase):
    def setUp(self):
        url = reverse('users:register')
        self.response = self.client.post(url, {})

    def test_register_status_code(self):
        """An invalid form will return to the same page."""
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_user_doesnt_exist(self):
        self.assertFalse(User.objects.exists())
