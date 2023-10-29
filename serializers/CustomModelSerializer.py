from rest_framework import serializers, exceptions

# write your custom serailziers here

class ModelSerializer(serializers.ModelSerializer):
    
    def is_valid(self, raise_exception=False):
        try:
            return super(serializers.ModelSerializer, self).is_valid(raise_exception=raise_exception)
        except exceptions.ValidationError as e:
            errors = {}
            for item in e.args:
                errors.update(**item)
            raise exceptions.ValidationError({"detail":errors})