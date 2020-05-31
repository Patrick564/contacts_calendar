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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, default='Empty')
    phone_number = PhoneField(blank=True, default='00000000')
    contact_email = models.EmailField(
        max_length=254,
        blank=True,
        default='empty@contactscalendar.com'
    )
    date_of_birth = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
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
