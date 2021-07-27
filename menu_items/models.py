from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


class Categories(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name=_("Enter name:"),
                            help_text=_("name of category"))

    description = models.CharField(max_length=50,
                                   verbose_name=_("description:"),
                                   help_text=_("add description"),
                                   null=True,
                                   blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(verbose_name=_("delete"))

    def __str__(self):
        return f'{self.name}'


class Price(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(verbose_name=_("amount:"), help_text=_("The number you want to price"))
    price = models.IntegerField(verbose_name=_("Enter price:"),
                                help_text=_("price of item"))

    def __str__(self):
        return f'{self.id}# {self.amount}: {self.price}'


class Discount(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name=_("name:"),
                            help_text=_("name of discount"),
                            null=True,
                            blank=True)

    code = models.CharField(max_length=30,
                            verbose_name=_("Enter Code:"),
                            help_text=_("Enter Code for Discount"))

    amount = models.IntegerField(verbose_name=_("amount:"),
                                 null=True,
                                 blank=True,
                                 help_text=_("amount of discount"))

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(verbose_name=_("delete"))

    def __str__(self):
        return f"{self.name} {self.code}"


def menu_item_validator(value: str):
    if not value.istitle():
        raise ValidationError("name of menu item is wrong :(")


def price_positive(value: Price):
    if not value.price > 0:
        raise ValidationError("price most be positive :(")


class MenuItems(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name=_("Enter name:"),
                            help_text=_("name of item"))

    price = models.ForeignKey(Price,
                              on_delete=models.CASCADE,
                              verbose_name=_("price:"),
                              help_text=_("choice the price"))

    discount = models.ForeignKey(Discount,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("discount:"),
                                 help_text=_("choice the discount"))

    image = models.FileField(verbose_name=_("add image:"),
                             help_text=_("image for item"),
                             upload_to='menu_items/images',
                             null=True,
                             blank=True)

    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("category"),
                                 help_text=_("Choose the group to which the item belongs"))

    starting_cooking_time = models.TimeField(verbose_name=_("starting cooking time:"),
                                             null=True,
                                             blank=True)

    estimated_cooking_time = models.TimeField(verbose_name=_("estimated cooking time:"),
                                              null=True,
                                              blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(verbose_name=_("delete"),
                                  default=False)

    def __str__(self):
        return f'{self.id}# {self.name}: {self.price}'
