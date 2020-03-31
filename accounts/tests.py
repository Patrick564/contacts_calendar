from django.test import TestCase
from django.contrib.auth import authenticate

from .models import User


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(
            email='lia@re.com',
            password='aiacos22',
            first_name='Lia',
            last_name='Lia',
            gender='Female',
            date_of_birth='2011-02-03',
            phone_number='922344135',
        )

    def test_fields_success(self):
        """Email is successfuy saved and authenticated"""
        lia = User.objects.get(email='lia@re.com')
        password = 'aiacos22'
        u = authenticate(email=lia.email, password=password)

        self.assertEqual(lia.email, 'lia@re.com', 'bad email')
        self.assertIsNotNone(u, 'bad auth')
        # self.assertIsNone(u, 'is none')
