from django.db import models

from menu_items.models import MenuItems
from receipts.models import Receipt
from table.models import Table


class OrderStatus(models.Model):
    status = models.CharField(max_length=30,
                              verbose_name="status:",
                              help_text="add status for order's")

    def __str__(self):
        return f"{self.id}# {self.status}"


class Orders(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1,
                                         verbose_name="number of item's:",
                                         help_text="add number of item's")

    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    def __str__(self):
        return f'{self.id}# table:{self.table} - item:{self.menu_items}' \
               f'- number:{self.number} - status:{self.status}'
