from django.contrib import admin
from .models import newuser

# Register your models here.
@admin.register(newuser)
class newuserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'password', 'mobilenum')
