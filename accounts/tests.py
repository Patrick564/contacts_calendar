# Django imports
from django.test import TestCase
from django.contrib.auth import authenticate

# App imports
from .models import User


# Test about custom user model
class UserTestCase(TestCase):

    # Create accounts
    def setUp(self):
        """
        Initial accounts in posterior tests.
        """
        lia = User.objects.create_user(
            email='lia@re.com',
            password='aiacos22',
            first_name='Lia',
            last_name='Lia',
            gender='Female',
            date_of_birth='2011-03-02',
            phone_number='+51 922 344 135'
        )
        lia.is_active = True
        lia.save()

        rem = User.objects.create_user(
            email='empresa@coronita.com',
            password='ninguno123',
            first_name='Rem',
            last_name='Hibike',
            gender='Female',
            date_of_birth='1995-05-02',
            phone_number='+51 933 222 345'
        )
        rem.is_active = True
        rem.save()

    # Auth account
    def test_auth_account(self):
        lia = User.objects.get(email='lia@re.com')
        rem = User.objects.get(email='empresa@coronita.com')
        password_lia = 'aiacos22'
        password_rem = 'ninguno123'

        lia = authenticate(email=lia.email, password=password_lia)
        rem = authenticate(email=rem.email, password=password_rem)

        self.assertEqual(lia.email, 'lia@re.com', 'Wrong Lia email')
        self.assertEqual(rem.email, 'empresa@coronita.com', 'Wrong Rem email')
        self.assertIsNotNone(lia, 'Auth Lia error')
        self.assertIsNotNone(rem, 'Auth Rem error')

    # Password change
    def test_password_change(self):
        lia = User.objects.get(email='lia@re.com')
        rem = User.objects.get(email='empresa@coronita.com')
        lia.set_password('newpassword123')
        rem.set_password('newpassword456')

        lia = authenticate(email=lia.email, password='newpassword123')
        rem = authenticate(email=rem.email, password='newpassword456')

        self.assertIsNotNone(lia, 'Auth Lia error')
        self.assertIsNotNone(rem, 'Auth Rem error')

    # Create account with a repeated email
    def test_create_account_with_same_email(self):
        ram = User.objects.create_user(
            email='empresa@coronita.com',
            password='newpass123',
            first_name='Ram',
            last_name='Minatsuki',
            gender='Female',
            date_of_birth='1999-09-24',
            phone_number='+51 959 934 789'
        )

        self.assertNotEqual(ram, 'empresa@coronita.com', 'User repeated')
