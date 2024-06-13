from django.urls import path
from .views import ProductsView, ContactListView, AddContactView, MessagesView, SendMessageView, MessageView


app_name = 'home'
urlpatterns = [
    path('', ProductsView.as_view(), name='home'),
    path('contacts', ContactListView.as_view(), name='contacts'),
    path('message/<int:pk>/', MessageView.as_view(), name='message'),
    path('add-contact', AddContactView.as_view(), name='add-contact'),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('send-message/<int:pk>/', SendMessageView.as_view(), name='send-message')
]