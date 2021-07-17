from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Enter name:",
                            help_text="name of category")

    description = models.CharField(max_length=285, verbose_name="description:",
                                   help_text="add description", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Price(models.Model):
    start_date = models.DateTimeField()
    amount = models.IntegerField()
    price = models.IntegerField(verbose_name="Enter price:", help_text="price of item")

    def __Str__(self):
        return f'{self.amount}: {self.price}'


class Discount(models.Model):
    name = models.CharField(max_length=100, verbose_name="name:",
                            help_text="name of discount", null=True, blank=True)

    code = models.CharField(max_length=285)

    amount = models.IntegerField(verbose_name="amount:", max_length=285,
                                 null=True, blank=True,
                                 help_text="amount of discount")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.code}"


class MenuItems(models.Model):
    name = models.CharField(max_length=30, verbose_name="Enter name:",
                            help_text="name of item")

    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    image = models.FileField(validators="add image:", help_text="image for item",
                             upload_to='item/img', null=True, blank=True)

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    starting_cooking_time = models.TimeField()
    stimated_cooking_time = models.TimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    def __str__(self):
        return f'{self.id}# {self.name}: {self.price}'
