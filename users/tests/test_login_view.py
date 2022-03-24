from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestLoginView(TestCase):
    def setUp(self):
        url = reverse('users:login')
        self.response = self.client.get(url)

    def test_default_redirect_to_login(self):
        url = reverse('run_stats:runs')
        self.response = self.client.get(url)
        self.assertRedirects(self.response, '/users/login/?next=/runs')

    def test_csrf_token(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_form_inputs(self):
        """Form should only have 4 inputs. csrf, username, password, and next"""
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="password"', 1)
        self.assertContains(self.response, 'type="hidden"', 2)


class SuccessfulLoginTests(TestCase):
    def setUp(self):
        user = User.objects.create(username='test')
        user.set_password('test_password')
        user.save()
        url = reverse('users:login')
        data = {
            'username': 'test',
            'password': 'test_password'
        }
        self.response = self.client.post(url, data)

    def test_redirect(self):
        """A successful sign in should receive 302."""
        self.assertEquals(self.response.status_code, 302)

    def test_successful_login_redirects_to_home(self):
        """A successful sign in shuold redirect to the home screen."""
        self.assertRedirects(self.response, '/')

    def test_user_authentication(self):
        """User should be authenticated on arbitrary new page."""
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
