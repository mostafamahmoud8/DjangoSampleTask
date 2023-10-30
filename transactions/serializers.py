from rest_framework import serializers
from serializers.CustomModelSerializer import ModelSerializer
from .models import Transaction, ExchangeRate
from .utils import get_change_rate

# write your serializers here

class TransactionSerializer(ModelSerializer):
    
    class Meta:
        model = Transaction
        exclude = ['user']
        read_only_fields = ['exhange_rate', 'result']
    
    def create(self, validated_data):
        from_currency = validated_data["from_currency"] = str(validated_data.get("from_currency", None)).upper()
        to_currency = validated_data["to_currency"] = str(validated_data.get("to_currency", None)).upper()
        user = self.context['request'].user
        transaction = Transaction(**validated_data)
        transaction.user = user
        data = get_change_rate(base_currency=from_currency)
        if data:
            transaction.exhange_rate = data[to_currency]['value']
            transaction.result = validated_data.get('amount') * transaction.exhange_rate
        else:
            try:
                exchange_rate = ExchangeRate.objects.get(from_currency=from_currency, to_currency=to_currency)
                transaction.rate = exchange_rate.rate
                transaction.result = validated_data.get('amount') * transaction.exhange_rate
            except ExchangeRate.DoesNotExist:
                raise serializers.ValidationError({"error":"error happend during transaction", "detail":data})
        transaction.save()
        return transaction