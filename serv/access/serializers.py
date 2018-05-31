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
            'area', 'from_time', 'to_time',
            'from_date', 'to_date', 'price', 'for_guests', 'adult', 'weekend',
            'visited_this_day'
        )


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        fields = ('name', 'date', 'area')


class AccessSerializer(serializers.Serializer):
    """
    Serializer generating a response to the client.
    """

    access = serializers.BooleanField()
    description = serializers.CharField()
