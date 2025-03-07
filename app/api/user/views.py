from apps.user.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny


class RegisterViewSets(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

