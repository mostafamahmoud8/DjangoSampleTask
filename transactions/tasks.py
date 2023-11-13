
from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone
from .models import Transaction
import datetime


logger = get_task_logger(__name__)

CHANGE_TASK_STATUS=60*60*48 # 48 hours


@shared_task()
def change_transaction_status():
     date_delta = timezone.now().date() - datetime.timedelta(seconds=CHANGE_TASK_STATUS)
     transactions = Transaction.objects.filter(created_at__date__lte=date_delta)
     transactions.update(status=Transaction.TRANSACTIONSTATUS.PERMANENT)
     msg = str(len(transactions)) + " transactions has been affected by celery task"
     logger.info(msg)
     return msg

 
 