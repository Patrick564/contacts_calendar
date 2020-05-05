# Django imports
from django.test import TestCase, Client

# App imports
from accounts.models import User


class First(TestCase):

    def setUp(self):
        User.objects.create_user(
            username='Lia22',
            email='pvilchez794@gmail.com',
            password='aiacos22',
            first_name='Lia',
            last_name='Lia',
            gender='Female',
            date_of_birth='2011-03-02',
            phone_number='+51 922 344 135'
        )

        self.client = Client()

    def test_first(self):
        self.client.login(email='pvilchez794@gmail.com', password='aiacos22')

        index = self.client.get('/')

        print(index.content)
