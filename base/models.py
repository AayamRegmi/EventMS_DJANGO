from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

# User model with different roles (Event Planner, Vendor, Client)
class User(AbstractUser):  
    username = models.CharField(max_length=300)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=300)
    location = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    USERNAME_FIELD = 'email'  # Login with email instead of username
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Event Category model
class EventCategory(models.Model):    
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category 

# Organizer model (Event Planner)
class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# Vendor model
class Vendor(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    services = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Event model
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    
    organizers = models.ManyToManyField(Organizer, related_name='events')
    vendors = models.ManyToManyField(Vendor, related_name='events')
    tickets = models.ManyToManyField('Ticket', related_name='events', blank=True)

    #attendees are defined by their ticket, attendees can buy tickets after the event has been created

    def __str__(self):
        return self.event_name
    
class Ticket_Category(models.Model):
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# Ticket model
class Ticket(models.Model):
    #attendees are defined by their ticket
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    ticket_category = models.ForeignKey(Ticket_Category, on_delete=models.CASCADE)
    number_of_ticket = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate total = number of tickets * ticket category price
        self.total = self.number_of_ticket * Decimal(self.ticket_category.price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.number_of_ticket} for {self.event.event_name}"


# Payment model
class Payment(models.Model):
    Ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.Ticket.total} for ticket_id:{self.Ticket.id}"

# Event Logistics model
class EventLogistics(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    equipment = models.TextField()
    catering = models.TextField()
    transportation = models.TextField()
    expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Logistics for {self.event.event_name}"
    

# Review model
class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.event.event_name}"
