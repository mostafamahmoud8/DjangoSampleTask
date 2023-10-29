from serializers.CustomModelSerializer import ModelSerializer
from .models import Transaction

# write your serializers here

class TransactionSerializer(ModelSerializer):
    
    class Meta:
        model = Transaction
        exclude = ['user']
    
    def create(self, validated_data):
        transaction = Transaction(**validated_data)
        user = self.context['request'].user
        transaction.user = user
        transaction.save()
        return transaction