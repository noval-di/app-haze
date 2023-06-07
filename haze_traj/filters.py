import django_filters
from .models import HotspotSipongi

class HotspotFilter(django_filters.FilterSet):
    class Meta:
        model = HotspotSipongi
        fields = ("nama_provinsi", 'kabkota', 'kecamatan', 'lat', 'long', 'date_hotspot_ori', 'confidence_level')