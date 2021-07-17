from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name="status:",
                            help_text="add status for table's")

    def __str__(self):
        return f"{self.id}# {self.name}"


class Table(models.Model):
    table_number = models.PositiveIntegerField(verbose_name="table number:",
                                               help_text="add number for table")

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}# table number:{self.table_number} - table status:{self.status}'
