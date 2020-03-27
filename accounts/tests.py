from django.test import TestCase

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
        """Email is successfuy saved"""
        lia = User.objects.get(email='lia@re.com')

        self.assertEqual(lia.email, 'lia@re.com')

    # def test_send_email(self):
    #     """Send a email"""
    #     send_mail(
    #         'Welcome',
    #         'Register verification',
    #         settings.EMAIL_HOST_USER,
    #         [email],
    #         fail_silently=False
    #     )
