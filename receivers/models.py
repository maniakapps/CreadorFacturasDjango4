#  Copyright (c) 2022 ManiakApps
#  All Rights Reserved
#
#  This product is protected by copyright and distributed under
#  licenses restricting copying, distribution, and decompilation.

from datetime import datetime

from django.db import models


# Create your models here.

class Receiver(models.Model):
    """
    Cliente que recibe la factura.
    """
    name = models.CharField(max_length=200)
    address = models.TextField()
    website = models.URLField(blank=True)
    created = models.DateTimeField(default=datetime.now)

    #later
    #logo

    def __str__(self):
        return str(self.name)