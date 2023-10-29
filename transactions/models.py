from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.

User = get_user_model()

class Transaction(models.Model):
    class TRANSACTIONSTATUS(models.TextChoices):
        TEMPORARY =  'temporary', _('Temporary')
        PERMANENT = 'permanent', _('Permanent')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transaction')
    amount = models.FloatField(_('transaction amount'), null=False, blank=False)
    from_currency = models.CharField(_('from currency'), max_length=10, null=False, blank=False)
    to_currency = models.CharField(_('to currency'), max_length=10, null=False, blank=False)
    status = models.CharField(_('transaction status'), max_length=10, choices=TRANSACTIONSTATUS.choices, default=TRANSACTIONSTATUS.TEMPORARY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.get_username()
