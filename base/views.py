from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from .serializers import *
from .models import *
from .permissions import CustomPermission

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    
    password = request.data.get('password')
    hash_password = make_password(password) #encrypting the password
    request.data['password'] = hash_password #overriding value in password field

    serializer = RegisterSerializer(data = request.data) #passes data to serializer

    if serializer.is_valid():
        serializer.save()
        return Response("User data registered")
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    email = request.data.get('email')
    password = request.data.get('password')   
    
    user = authenticate(username = email, password = password)

    if user == None:
        return Response("invalid credentials")
    else:
        token,_ = Token.objects.get_or_create(user = user) 

        return Response(token.key)
    

class UserApiView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated, CustomPermission]

class OrganizerApiView(ModelViewSet):

    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

    permission_classes = [IsAuthenticated, CustomPermission]
    filterset_fields = ['user']
    search_fields = ['name']
    

class VendorApiView(ModelViewSet):
    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    permission_classes = [IsAuthenticated, CustomPermission]
    filterset_fields = ['user']
    search_fields = ['name']

class TicketApiView(ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    permission_classes = [IsAuthenticated, CustomPermission]
    filterset_fields = ['user','event']
    search_fields = ['ticket_number']

class PaymentApiView(ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticated, CustomPermission]

class EventLogisticsApiView(ModelViewSet):

    queryset = EventLogistics.objects.all()
    serializer_class = EventLogisticsSerializer

    permission_classes = [IsAuthenticated, CustomPermission]

class ReviewApiView(ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated, CustomPermission]

class CategoryApiView(ModelViewSet):

    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer

    permission_classes = [IsAuthenticated, CustomPermission]

class EventApiView(GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated, CustomPermission]
    filterset_fields = ['organizers', 'vendors']
    search_fields = ['event_name']

    def get(self, request):

        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        
        return Response(serializer.data)

    def post(self, request):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Event Created")
        else:
            return Response(serializer.errors)

class EventDetailApiView(GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated, CustomPermission]

    def get(self, request, pk):

        queryset = self.get_object()
        serializer = self.serializer_class(queryset)

        return Response(serializer.data)
    
    def put(self, request, pk):
        queryset = self.get_object()
        serializer = self.serializer_class(queryset, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response("Event Updated")
        else:
            return Response(serializer.errors)
    
    #delete specific event by id
    def delete(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response('Event Removed')   

        


































    