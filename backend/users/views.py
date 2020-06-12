from django.contrib.auth import login as django_login, logout as django_logout
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import is_password_usable, check_password, make_password

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters, exceptions, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import (UserSerializer, 
                        LoginSerializer, 
                        UserBarcodeSerializer,  
                        AlternativeLoginSerializer,
                        ChangePasswordSerializer,
                        ManagerApprovalBarcodeSerializer, )
from .permissions import AdminSuperAdmin
from .models import User, UserBarcode


class UserProfileViewset(viewsets.ModelViewSet):
    """Handles CRUD for User Profile"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, AdminSuperAdmin, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username', 'id', 'email']
    search_fields = ['username', 'id', 'email']
    ordering_fields = '__all__'
    ordering = ['id']


class UserLoginAPIView(ObtainAuthToken):
    """Handles creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        print('Login request', request)
        print('Login kwargs', kwargs)
        #Need to find the User associated Company and concat the Company ID to the email address
        # print('User.objects.last()', User.objects.last())
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
        })

class AlternativeLoginAPIView(APIView):
    """Handles creating user auth tokens for Alternative Login"""
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AlternativeLoginSerializer

    def get(self, request):
        return Response({'Message': "Hello There Yall"})

    def post(self, request, *args, **kwargs):
        print('Login request', request)
        print('Login kwargs', kwargs)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        print('serializer.validated_data', serializer.validated_data)
        barcode = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
        return Response({
            'token': token.key,
            'user_id': serializer.validated_data['user'].pk,
            'email': serializer.validated_data['user'].email,
        })

class ManagerBarcodeApprovalAPIView(APIView):
    """Handles creating user auth tokens for Alternative Login"""
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = ManagerApprovalBarcodeSerializer

    def get(self, request):
        return Response({'Message': "GET request for the API Endpoint to verify manager credentials"})

    def post(self, request, *args, **kwargs):
        print('View 1')

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print('View 2')
        serializer.is_valid(raise_exception=True)
        print('serializer.validated_data', serializer.validated_data)
        print('View 3')
        user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
        return Response({
            'approved': "true",
        })

class UserBarcodeViewSet(viewsets.ModelViewSet):
    """User Barcode Endpoints. All of them"""
    serializer_class = UserBarcodeSerializer
    queryset = UserBarcode.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user__id', 'id', 'barcode_type', 'barcode_number', 'user__employee__datacom__id', 'user__employee__partner__id', 'user__employee__company__id', 'user__employee__vendor__id']
    search_fields = ['user__Id', 'id', 'barcode_type', 'barcode_number', 'user__employee__datacom__id', 'user__employee__partner__id', 'user__employee__company__id', 'user__employee__vendor__id']
    ordering_fields = '__all__'
    ordering = ['id']

class UserLogOutAPIView(APIView):
    """Handles removing user auth tokens"""
    authentication_classes = (TokenAuthentication, )

    def logout(self, request):
        print('request', request)
        print('self', self)
        django_logout(request)
        return Response(status=204)

class ChangePasswordAPI(APIView):
    """Handles creating user auth tokens for Alternative Login"""
    serializer_class = ChangePasswordSerializer

    def get(self, request):
        return Response({'Message': "Hello There Yall"})

    def put(self, request, *args, **kwargs):
        print('request', request)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        print('serializer--------', serializer)
        print('serializer.validated_data', serializer.validated_data)
        user = serializer.validated_data['user']
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        
        return Response({
            'user_id': serializer.validated_data['user'].pk,
            'email': serializer.validated_data['user'].email,
        })