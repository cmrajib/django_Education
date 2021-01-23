from django.contrib import messages
from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    comment = models.TextField()

    def __str__(self):
        return self.email + ' - ' + self.name