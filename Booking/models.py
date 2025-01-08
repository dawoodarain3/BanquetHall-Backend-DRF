from django.db import models
from rest_framework.exceptions import ValidationError
from .validator import validate_cnic
# Models
class UserDetail(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    cnic_number = models.CharField(max_length=15,unique=True,validators=[validate_cnic])
    cnic_pictures = models.ImageField(upload_to='cnic_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class BanquetDetail(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pictures = models.ImageField(upload_to='hall_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name
class BookingDetail(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='bookings')
    banquet = models.ForeignKey(BanquetDetail, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('banquet', 'start_time', 'end_time')

    def clean(self):
        # Ensure start_time is earlier than end_time
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be earlier than end time.")

        # Check for overlapping bookings
        overlapping_booking = BookingDetail.objects.filter(
            banquet=self.banquet,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk)

        if overlapping_booking.exists():
            raise ValidationError("This time slot is already booked for the selected banquet.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
