from django.contrib import admin
from .models import Booking

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "departure_date",)

admin.site.register(Booking, StudentAdmin)