from rest_framework import serializers
from .models import BanquetDetail,BookingDetail,UserDetail,ValidationError


# Serializers
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

class BanquetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanquetDetail
        fields = '__all__'

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetail
        fields = '__all__'

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise ValidationError("Start time must be earlier than end time.")
        return data
