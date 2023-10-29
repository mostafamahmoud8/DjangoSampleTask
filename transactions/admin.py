from django.contrib import admin
from .models import Transaction

# write your admin models here

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction