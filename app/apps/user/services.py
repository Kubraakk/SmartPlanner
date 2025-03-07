from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from core.services.base_service import BaseService

User = get_user_model()

class UserSevice(BaseService):
    def __init__(self):
        super().__init__(User)

    def create_user(self,username, email, password):
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )
        user.set_password(password)
        user.save()
        return user

    def authenticate_user(self, email, password):
        user = authenticate(
            email=email,
            password=password
            )

        if not user:
            raise ValidationError(
                "User not found"
            )
        if not user.is_active:
            raise ValidationError("User inactivate")

        refresh = RefreshToken.for_user(user)

        return {
            "acces": str(refresh.acces_token),
            "refresh": str(refresh),
        }