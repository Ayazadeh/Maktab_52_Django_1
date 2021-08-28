from django.db import models
from django.utils.translation import gettext as _
from menu_items.models import MenuItems
from receipts.models import Receipt
from table.models import Table


class OrderStatus(models.Model):
    status = models.CharField(max_length=30,
                              verbose_name=_("status:"),
                              help_text=_("add status for order's"))

    def __str__(self):
        return f"{self.id}# {self.status}"


class Orders(models.Model):
    table = models.ForeignKey(Table,
                              on_delete=models.CASCADE,
                              verbose_name=_("table:"),
                              help_text=_("choice table"))

    menu_items = models.ForeignKey(MenuItems,
                                   on_delete=models.CASCADE,
                                   verbose_name=_("item:"),
                                   help_text=_("choice item you want"))

    number = models.PositiveIntegerField(default=1,
                                         verbose_name=_("number:"),
                                         help_text=_("add number of item's"))

    receipt = models.ForeignKey(Receipt,
                                on_delete=models.CASCADE,
                                verbose_name=_("receipt:"),
                                help_text=_("choice receipt"))

    status = models.ForeignKey(OrderStatus,
                               on_delete=models.CASCADE,
                               verbose_name=_("status:"),
                               help_text=_("choose status of order"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(verbose_name=_("delete"))

    @classmethod
    def order_by_menu_item(cls, id):
        return cls.objects.filter(menu_items_id=id)

    def __str__(self):
        return f'{self.id}# table:{self.table} - item:{self.menu_items}' \
               f'- number:{self.number} - status:{self.status}'


