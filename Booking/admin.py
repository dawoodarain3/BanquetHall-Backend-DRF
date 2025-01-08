from django.contrib import admin
from .models import BanquetDetail,BookingDetail,UserDetail
# Register your models here.

# Admin
@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'cnic_number')
    search_fields = ('name', 'city', 'cnic_number')

@admin.register(BanquetDetail)
class BanquetDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(BookingDetail)
class BookingDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'banquet', 'start_time', 'end_time', 'advance_payment', 'total_payment', 'created_at')
    search_fields = ('user__name', 'banquet__name')
    list_filter = ('start_time', 'banquet')
