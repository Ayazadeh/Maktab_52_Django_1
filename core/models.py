from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    Create_timestamp = models.DateTimeField(auto_now_add=True)
    Modify_timestamp = models.DateTimeField(auto_now=True)
    Delete_timestamp = models.DateTimeField(default=None, null=True, blank=True)

    def logical_delete(self):
        self.Delete_timestamp = timezone.now()
        self.save()


class Cashier(User, TimestampMixin):
    phone_number = models.CharField(max_length=11)
    national_code = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
