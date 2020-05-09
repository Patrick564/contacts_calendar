from django.contrib.auth.backends import ModelBackend

from .models import User


class EmailBackend(ModelBackend):

    def authenticate(self, request, email, password, **kwargs):
        if email and password:
            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                return None

            else:
                if user.is_active:
                    return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
