from django.shortcuts import render, redirect
from products.models import Products
from django.views import View

from .models import Contacts, Message
from .forms import ContactForm, MessageForm

from users.models import CustomUser
# Create your views here.


def messages(request):
    return render(request, 'messages.html')


class ProductsView(View):
    def get(self, request):
        products = Products.objects.all()
        context = {
            'products': []
        }
        for product in products:
            discounted_price = None
            if product.discount_price:
                discounted_price = product.price - (product.price * product.discount_price.discount / 100)

            context['products'].append({
                'pk': product.pk,
                'image': product.image,
                'info': product.name,
                'price': product.price,
                'discounted_price': discounted_price,
                'discount': product.discount_price.discount if product.discount_price else None,
            })
        return render(request, 'home.html', context=context)


class ContactListView(View):
    def get(self, request):
        contacts = Contacts.objects.filter(user=request.user).order_by('name')
        context = {
            'contacts': []
        }
        for contact in contacts:
            if contact.users != self.request.user:
                context['contacts'].append({
                    'pk': contact.pk,
                    'name': contact.name,
                    'image': contact.users.image,
                    'username': contact.users.username,
                    'first_name': contact.users.first_name,
                    'last_name': contact.users.last_name,
                })
        return render(request, 'contact_list.html', context=context)


class AddContactView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'add_contact.html', context=context)

    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('home:contacts')
        else:
            context = {
                'form': form
            }
            return render(request, 'add_contact.html', context=context)


class MessagesView(View):
    def get(self, request):
        messages = Message.objects.filter(conversation__users=request.user).order_by('-timestamp')
        context = {
            'messages': messages
        }
        return render(request, 'messages.html', context=context)


class MessageView(View):
    def get(self, request, pk):
        sender = CustomUser.objects.get(pk=pk)
        received_message = Message.objects.filter(conversation__users=request.user, sender=sender)
        sent_message = Message.objects.filter(sender=request.user, conversation__users=sender)

        context = {
            'contact': sender.pk,
            'received_messages': received_message,
            'sent_messages': sent_message
        }
        return render(request, 'received.html', context=context)


class SendMessageView(View):
    def get(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        message = MessageForm()
        context = {
            'form': message,
            'contact': contact,
        }
        return render(request, 'send_message.html', context=context)

    def post(self, request, pk):
        message = MessageForm(data=request.POST)
        if message.is_valid():
            message = message.save(commit=False)
            message.sender = request.user
            message.conversation = Contacts.objects.get(pk=pk)
            message.save()
            return redirect('home:messages')
        else:
            context = {
                'form': message
            }
            return render(request, 'send_message.html', context=context)