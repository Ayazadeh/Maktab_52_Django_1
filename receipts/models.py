from django.db import models
from django.utils.translation import gettext as _


class Receipt(models.Model):
    order = models.PositiveIntegerField(verbose_name=_("number of order's:"),
                                        help_text=_("add number of order's"))

    total_price = models.FloatField(verbose_name=_("total price:"))
    total_discount = models.FloatField(verbose_name=_("total discount:"))
    final_price = models.FloatField(verbose_name=_("final price:"))
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(verbose_name=_("delete"))

    def __str__(self):
        return f'{self.id}# order:{self.order} - final price:{self.final_price}'
