
from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone
from .models import Transaction
import datetime


logger = get_task_logger(__name__)

DELETE_TEMP_USER_TIME=60*60*48 # 48 hours


@shared_task()
def change_transaction_status():
     date_delta = timezone.now().date() - datetime.timedelta(seconds=DELETE_TEMP_USER_TIME)
     transactions = Transaction.objects.filter(created_at__date__lte=date_delta)
     transactions.update(status=Transaction.TRANSACTIONSTATUS.PERMANENT)
     return str(len(transactions)) + " transactions has been affected by celery task"

 
 