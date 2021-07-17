from django.db import models


class Receipt(models.Model):
    order = models.PositiveIntegerField(verbose_name="number of order's:",
                                        help_text="add number of order's")

    total_price = models.FloatField(verbose_name="total price:")
    total_discount = models.FloatField(verbose_name="total discount:")
    final_price = models.FloatField(verbose_name="final price:")
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    def __str__(self):
        return f'{self.id}# order:{self.order} - final price:{self.final_price}' \

