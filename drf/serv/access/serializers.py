from rest_framework import serializers
from access.models import Customer, Area, Rule

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'balance', 'is_guest', 'birth')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('name')

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = (
            'area', 'can_access', 'from_time', 'to_time',
            'on_date', 'price', 'for_guests', 'adult', 'weekend',
            'visited_this_day'
        )

class AccessSerializer(serializers.ModelSerializer):
    # Access: JSON z polem True/False i Description
