from django.contrib.auth.models import User
from django.test import TestCase, Client

from accounts.models import Account


class AccountModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {'username': 'testuser', 'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/accounts/sign_in/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_string_representation(self):
        user = User.objects.create(username="test_user", email="test@example.com", password="test1234")
        account = Account(user, "John", "Perry")
        self.assertEqual(str(account), account.first_name)

    def test_sign_in_view(self):
        self.test_login()
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['accounts']), 1)
