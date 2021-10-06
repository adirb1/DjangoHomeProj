from django.db import models
from django.contrib.auth.models import User
import uuid

class Message(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    subject = models.CharField(max_length=100)

    message=models.CharField(max_length=2500)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
   


    def __str__(self):
        return self.message
