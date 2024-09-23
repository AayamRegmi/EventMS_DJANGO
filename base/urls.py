from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserApiView.as_view({'get':'list'}), name='user'),
    path('user/<int:pk>', UserApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_user'),

    path('event/', EventApiView.as_view(),name='event'),
    path('event/<int:pk>', EventDetailApiView.as_view(),name='specific_event'),

    path('category/', CategoryApiView.as_view({'get':'list'}),name='category'),

    path('organizer/', OrganizerApiView.as_view({'get':'list','post':'create'}),name='organizer'),
    path('organizer/<int:pk>', OrganizerApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_event'),

    path('vendor/', VendorApiView.as_view({'get':'list','post':'create'}),name='vendor'),
    path('vendor/<int:pk>', VendorApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_vendor'),

    path('ticket/', TicketApiView.as_view({'get':'list','post':'create'}), name='ticket'),
    path('ticket/<int:pk>', TicketApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_ticket'),

    path('payment/', PaymentApiView.as_view({'get':'list','post':'create'}),name='payment'),
    path('payment/<int:pk>', PaymentApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_payment'),

    path('eventlogistic/', EventLogisticsApiView.as_view({'get':'list','post':'create'}),name='logistic'),
    path('eventlogistic/<int:pk>', EventLogisticsApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_logistic'),

    path('review/', ReviewApiView.as_view({'get':'list','post':'create'}),name='review'),
    path('review/<int:pk>', ReviewApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='specific_review'),

    path('login/', login, name='login'),
    path('register/', register, name='register')
]


