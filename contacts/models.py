# Django imports
from django.db import models

# Library imports
from phone_field import PhoneField

# Python imports
from datetime import date, datetime

# App imports
from accounts.models import User


# Model for contacts data
class ContactField(models.Model):
    """
    Model for contacts, FK to User model.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=50, default='Cosme Fulanito')
    # phone_number = PhoneField(default='00000000')
    contact_email = models.EmailField(
        max_length=254,
        default='empty@cc.com'
    )
    date_of_birth = models.DateField(
        auto_now=False,
        auto_now_add=False,
        default=date.today
    )
    favorite = models.BooleanField(default=False)
    filed = models.BooleanField(default=False)

    def __str__(self):
        today = datetime.now()
        date_id = str(today.year) + str(today.month) + str(today.day)
        time_id = str(today.hour) + str(today.minute) + str(today.second)
        str_id = str(self.user_id) + str(self.id) + date_id + time_id

        return str_id
