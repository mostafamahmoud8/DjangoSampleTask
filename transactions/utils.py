import currencyapicom
import logging
import threading
from .models import ExchangeRate 

logger = logging.getLogger(__name__)

API_KEY = "cur_live_XH9A3bMReyfAXR7fe8yHF2WDDdO8jVFhnfhIjryW"

def write_data_to_db(base_currency, data):
    for key, value in data.items():
        try:
            ExchangeRate.objects.get(from_currency=base_currency, to_currency=value['code'])
        except ExchangeRate.DoesNotExist:
            ExchangeRate.objects.create(from_currency=base_currency, to_currency=value['code'], rate=value['value'])
    
def get_change_rate(base_currency):
    try:
        client = currencyapicom.Client(API_KEY)
        data = client.latest(base_currency=base_currency)['data']
        thread = threading.Thread(target=write_data_to_db, args=(base_currency, data,))
        thread.start()
        return data
    except Exception as e:
        logger.error(repr(e))
        return None