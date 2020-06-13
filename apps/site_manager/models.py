from django.db import models
from apps.users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "%s " % self.name

# Create your models here.
class UnsubscribeMassiveMail(models.Model):
    user = models.ForeignKey(CustomUser, related_name='unsubscribeMail', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return "%s " % self.user.username

