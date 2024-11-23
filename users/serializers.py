from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.models import User, Payments


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = ("user", "date", "paid_course", "paid_lesson", "amount", "payment_method")


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'tg_nick', 'city', 'avatar', 'payments']
