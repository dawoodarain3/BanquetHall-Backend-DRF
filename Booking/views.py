from rest_framework import viewsets
from .serializers import BanquetDetailSerializer,BookingDetailSerializer,UserDetailSerializer
from .models import BanquetDetail,BookingDetail,UserDetail
from rest_framework.response import Response
# Create your views here.

# ViewSets
class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

class BanquetDetailViewSet(viewsets.ModelViewSet):
    queryset = BanquetDetail.objects.all()
    serializer_class = BanquetDetailSerializer


class BookingDetailViewSet(viewsets.ModelViewSet):
    queryset = BookingDetail.objects.all()
    serializer_class = BookingDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
