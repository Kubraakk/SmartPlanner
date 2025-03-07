from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.user.services import UserSevice
from apps.user.models import Profile


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True, min_length=5, style = {"input_type": "password"}
    )
    class Meta:
        model = User
        fields = ('uuid', 'username','password','email')

    def create(self, validated_data):
        user_service = UserSevice()
        return user_service.create_user(
            email = validated_data["email"],
            username = validated_data["username"],
            password = validated_data["password"],
        )

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "bio", "avatar", "birth_date", "phone_number"]
