#  Copyright (c) 2022 ManiakApps
#  All Rights Reserved
#
#  This product is protected by copyright and distributed under
#  licenses restricting copying, distribution, and decompilation.

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Clase del dueño de la factura
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=26, blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # avatar =
    # company_logo =

    def __str__(self):
        return f"Profile of the user: {self.user}"