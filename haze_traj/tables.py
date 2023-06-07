import django_tables2 as tables
from .models import HotspotSipongi
from django.shortcuts import render
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from .filters import HotspotFilter

class HotspotTable(tables.Table):
    nama_provinsi = tables.Column(verbose_name='Provinsi')
    kabkota = tables.Column(verbose_name='Kabupaten Kota')
    kecamatan = tables.Column(verbose_name='Kecamatan')
    desa = tables.Column(verbose_name='Desa')
    lat = tables.Column(verbose_name='Latitude')
    long = tables.Column(verbose_name='Longitude')
    date_hotspot_ori = tables.Column(verbose_name='Date & Time')
    confidence_level = tables.Column(verbose_name='Confidence Level')
    
    class Meta:
        # model = HotspotSipongi
        fields = ("nama_provinsi", 'kabkota', 'kecamatan','desa', 'lat', 'long', 'date_hotspot_ori', 'confidence_level')
        template_name = "django_tables2/bootstrap5-responsive.html"
        attrs = {"class": "table table-responsive"}
    def __str__(self):
        return "HotspotTable: Columns={}, Rows={}".format(len(self.columns), len(self.rows))
p
    