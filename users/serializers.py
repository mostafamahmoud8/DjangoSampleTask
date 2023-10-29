from django.contrib.auth import get_user_model, password_validation
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from serializers.CustomModelSerializer import ModelSerializer


# write your serializers here

User = get_user_model()

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            try:
                 password_validation.validate_password(password, user)
                 user.set_password(password)    
            except exceptions.ValidationError as e:
                 raise serializers.ValidationError({"detail":{'password':e.messages}})
            user.save()
        return user