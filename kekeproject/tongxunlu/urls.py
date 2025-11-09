from django.urls import path
from . import views

urlpatterns = [
    # /api/contacts/
    path('contacts/', views.contact_list, name='contact_list'),

    # /api/contacts/1/
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
]