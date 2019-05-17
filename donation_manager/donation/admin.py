from django.contrib import admin
from .models import Institution, Donation, Donee

# Register your models here.
admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(Donee)