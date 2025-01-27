from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField() 
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    #para que no devuelva el objeto en la vista
    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
        