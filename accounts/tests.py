# Django imports
from django.test import TestCase, Client
from django.contrib.auth import authenticate

# App imports
from .models import User


# Test about custom user model
class UserCustom(TestCase):
    """
    Test about accounts creation, auth, password change
    and account with a already registered email.
    """
    # Accounts for tests
    def setUp(self):
        lia = User.objects.create_user(
            username='Lia22',
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
            username='Rem123',
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


# Test about accounts/ page load
class AccountsPageLoad(TestCase):
    """
    Test the accounts app page, load with session and
    a user created.
    """
    # Account for registered user tests
    def setUp(self):
        lia = User.objects.create_user(
            username='Lia22',
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

        self.client = Client()

    def test_create_views_anonymous_user(self):
        create = self.client.get('/accounts/create/', follow=True)
        create_done = self.client.get('/accounts/create/done/', follow=True)

        self.assertEqual(create.status_code, 200, 'Create load error')
        self.assertRedirects(create_done, '/')

    def test_create_views_registered_user(self):
        # Login for testing views in user auth case
        self.client.login(email='lia@re.com', password='aiacos22')

        create = self.client.get('/accounts/create/', follow=True)
        create_done = self.client.get('/accounts/create/done/', follow=True)

        self.assertRedirects(create, '/')
        self.assertEqual(create_done.status_code, 200, 'Done load error')

    def test_profile_views_anonymous_user(self):
        profile = self.client.get('/accounts/profile/Rem2/', follow=True)
        update = self.client.get('/accounts/profile/Rem2/update/', follow=True)

        self.assertRedirects(profile, '/accounts/login/?next=/accounts/profile/Rem2/')  # noqa:E501
        self.assertRedirects(update, '/accounts/login/?next=/accounts/profile/Rem2/update/')  # noqa:E501

    def test_profile_views_registered_user(self):
        # Login for testing views in user auth case
        self.client.login(email='lia@re.com', password='aiacos22')

        profile = self.client.get('/accounts/profile/Rem2/')
        update = self.client.get('/accounts/profile/Rem2/update/')

        self.assertEqual(profile.status_code, 200, 'Profile load error')
        self.assertEqual(update.status_code, 200, 'Update load error')

    def test_context(self):
        login = self.client.get('/accounts/login/')
        password_change = self.client.get('/accounts/password_change/')
        password_reset = self.client.get('/accounts/password_reset/')

        print('Login')
        print(login.context)

        print('Pwd Change')
        print(password_change.context)

        print('Pwd Reset')
        print(password_reset.context)
