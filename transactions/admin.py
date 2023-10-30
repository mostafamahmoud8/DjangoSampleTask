from django.contrib import admin
from .models import Transaction, ExchangeRate

# write your admin models here

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction

@admin.register(ExchangeRate)
class TransactionAdmin(admin.ModelAdmin):
    model = ExchangeRate