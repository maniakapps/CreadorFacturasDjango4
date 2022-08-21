#  Copyright (c) 2022 ManiakApps
#  All Rights Reserved
#
#  This product is protected by copyright and distributed under
#  licenses restricting copying, distribution, and decompilation.

from django.db import models

from invoices.models import Invoice


# Create your models here.

class Position(models.Model):
    """
    La posición del trabajador
    """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Informacion opcional")
    amount = models.FloatField(help_text="Cantidad de dinero en USD")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice :  {self.invoice.number}, position title:{self.title}"
