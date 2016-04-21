import re

from django.contrib.auth import get_user_model

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .serializers import AccountSerializer


Account = get_user_model()


class AccountViewSet(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    @list_route(methods=['get'])
    def me(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(AccountSerializer(request.user).data)

    @list_route(methods=['post', 'patch'])
    def change_email(self, request, *args, **kwargs):

        if 'email' in request.data and 'confirm_email' in request.data:
            if request.data['email'].strip().lower() == request.data['confirm_email'].strip().lower():
                if re.match(r"[^@]+@[^@]+\.[^@]+", request.data['email']):
                    request.user.email = request.data['email'].strip()
                    request.user.save()

                    return Response(status=status.HTTP_204_NO_CONTENT)

                return Response({'error': 'EMAIL INVALID'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'EMAIL MISMATCH'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'EMAIL MISSING'}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post', 'patch'])
    def change_password(self, request, *args, **kwargs):
        if 'password' not in request.data or 'password_repeat' not in request.data or\
           ('old_password' not in request.data and 'password_reset_key' not in request.data):
            return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['password'] != request.data['password_repeat']:
            return Response({'error': 'Password mismatch'}, status=status.HTTP_400_BAD_REQUEST)
        if 'old_password' in request.data and not request.user.check_password(request.data.get('old_password')):
            return Response({'error': 'Old password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        if 'password_reset_key' in request.data and not request.data.get('password_reset_key') == request.user.password_reset_key:
            return Response({'error': 'Reset key already used'}, status=status.HTTP_400_BAD_REQUEST)

        if 'password_reset_key' in request.data and not request.data.get('password_reset_key') == '':
            request.user.password_reset_key = Account._meta.get_field('password_reset_key').generate_unique(instance=request.user, sender=Account)
        request.user.set_password(request.data['password'])
        request.user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
