

#  Copyright (c) 2022 ManiakApps
#  All Rights Reserved
#
#  This product is protected by copyright and distributed under
#  licenses restricting copying, distribution, and decompilation.

from django.db import models

from profiles.models import Profile
from receivers.models import Receiver


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
    completion_date = models.DateField()
    issue = models.DateField()
    payment_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    #  if closed we should hide from pending
    closed = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"Invoice number: {self.number}, pk: {self.pk}"

    def get_positions(self):
        pass

    def get_total(self):
        pass

    def get_total_amount(self):
        pass
