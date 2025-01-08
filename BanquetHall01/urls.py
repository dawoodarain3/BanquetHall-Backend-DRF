from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Booking.views import UserDetailViewSet,BanquetDetailViewSet,BookingDetailViewSet

router = DefaultRouter()
router.register(r'users', UserDetailViewSet, basename='userdetail')
router.register(r'banquets', BanquetDetailViewSet, basename='banquetdetail')
router.register(r'bookings', BookingDetailViewSet, basename='bookingdetail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
