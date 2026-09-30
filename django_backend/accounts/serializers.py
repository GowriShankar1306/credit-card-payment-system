from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Card


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = [
            'id',
            'card_holder_name',
            'masked_card_number',
            'last_four_digits',
            'expiry_month',
            'expiry_year',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']