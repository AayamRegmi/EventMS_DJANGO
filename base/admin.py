from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Vendor)
admin.site.register(Ticket)
admin.site.register(Ticket_Category)
admin.site.register(Payment)
admin.site.register(EventLogistics)
admin.site.register(Review)
