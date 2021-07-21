from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name=_("status:"),
                            help_text=_("add status for table's"))

    def __str__(self):
        return f"{self.id}# {self.name}"


class Table(models.Model):
    table_number = models.PositiveIntegerField(verbose_name=_("table number:"),
                                               help_text=_("add number for table"))

    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE,
                               verbose_name=_("status:"),
                               help_text=_("choice status for table"))

    def __str__(self):
        return f'{self.id}# table number:{self.table_number} - table status:{self.status}'
