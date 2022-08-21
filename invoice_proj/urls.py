
#  Copyright (c) 2022 ManiakApps
#  All Rights Reserved
#
#  This product is protected by copyright and distributed under
#  licenses restricting copying, distribution, and decompilation.

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
