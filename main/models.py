from django.db import models

# Create your models here.
class EmailList(models.Model):
    # name = models.CharField(max_length=200)
    to = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.email


class Item(models.Model):
    emaillist = models.ForeignKey(EmailList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
