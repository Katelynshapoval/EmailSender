from django.db import models

# Create your models here.
class EmailList(models.Model):
    name = models.CharField(max_length=200)
    # to = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    emaillist = models.ForeignKey(EmailList, on_delete=models.CASCADE)
    recipient = models.EmailField(max_length=300)
    # chosen = models.BooleanField()
    # to = models.EmailField(blank=True, null=True)
    # to = models.EmailField()


    def __str__(self):
        return self.recipient
