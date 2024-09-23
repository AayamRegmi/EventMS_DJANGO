from rest_framework.serializers import ModelSerializer
from .models import User, EventCategory, Organizer, Vendor, Event, Ticket, Payment, EventLogistics, Review
from django.contrib.auth.models import Group

        
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(ModelSerializer):  
    groups = GroupSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','groups']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EventCategorySerializer(ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'

class OrganizerSerializer(ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'

class VendorSerializer(ModelSerializer):      
    class Meta:
        model = Vendor
        fields = '__all__'

class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class EventLogisticsSerializer(ModelSerializer):
    class Meta:
        model = EventLogistics
        fields = '__all__'

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'        
                             