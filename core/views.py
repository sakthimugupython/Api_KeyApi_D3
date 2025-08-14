from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_api_key.models import APIKey
from drf_api_key.permissions import HasAPIKey
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

# Custom permission: only allow users with 'Editor' in their username or a custom field
class IsEditor(BasePermission):
    def has_permission(self, request, view):
        # Example: check if user has a profile.role == 'Editor' (if you have a profile model)
        # Here, we'll just check username contains 'editor' for demo
        return request.user.is_authenticated and (
            hasattr(request.user, 'role') and request.user.role == 'Editor' or
            'editor' in request.user.username.lower()
        )

class GenerateAPIKeyView(APIView):
    permission_classes = []  # Allow all (or restrict to admin)

    def post(self, request):
        name = request.data.get('name', 'default')
        api_key, key = APIKey.objects.create_key(name=name)
        return Response({"api_key": key}, status=status.HTTP_201_CREATED)

class EditorOnlyView(APIView):
    permission_classes = [HasAPIKey, IsEditor]

    def get(self, request):
        return Response({"message": "Hello, Editor! You have access to this endpoint."})
