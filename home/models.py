from django.db import models
from users.models import CustomUser
from django.utils import timezone
# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='participant_contacts')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='owner_contacts')

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return f"{self.user.username}'s contact | {self.users.username}"


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'Message from {self.sender.username} at {self.timestamp}'