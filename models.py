# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BatasDesaAcehHotspot(models.Model):
    gid = models.IntegerField(blank=True, null=True)
    object_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kode_desa = models.CharField(max_length=10, blank=True, null=True)
    desa_kelur = models.CharField(max_length=34, blank=True, null=True)
    kecamatan = models.CharField(max_length=31, blank=True, null=True)
    kab_kota = models.CharField(max_length=27, blank=True, null=True)
    provinsi = models.CharField(max_length=26, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jumlah_hotspot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batas_desa_aceh_hotspot'


class HotspotRawRecordBackup(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    hs_id = models.DateTimeField(blank=True, null=True)
    date_hotspot_ori = models.TextField(blank=True, null=True)
    provinsi_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    sumber = models.TextField(blank=True, null=True)
    ori_sumber = models.TextField(blank=True, null=True)
    date_hotspot = models.TextField(blank=True, null=True)
    desa_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    counter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    confidence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    confidence_level = models.TextField(blank=True, null=True)
    kawasan = models.TextField(blank=True, null=True)
    desa = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    kabkota = models.TextField(blank=True, null=True)
    nama_provinsi = models.TextField(blank=True, null=True)
    pulau = models.TextField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'hotspot_raw_record_backup'
# Unable to inspect table 'hotspot_sipongi'
# The error was: permission denied for table hotspot_sipongi


class NewHotspot(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    hs_id = models.TextField(blank=True, null=True)
    date_hotspot_ori = models.TextField(blank=True, null=True)
    provinsi_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    sumber = models.TextField(blank=True, null=True)
    ori_sumber = models.TextField(blank=True, null=True)
    date_hotspot = models.TextField(blank=True, null=True)
    desa_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    counter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    confidence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    confidence_level = models.TextField(blank=True, null=True)
    kawasan = models.TextField(blank=True, null=True)
    desa = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    kabkota = models.TextField(blank=True, null=True)
    nama_provinsi = models.TextField(blank=True, null=True)
    pulau = models.TextField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'new_hotspot'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class WilayahIndonesia(models.Model):
    gid = models.BigAutoField(primary_key=True)
    desa = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    kab_kota = models.TextField(blank=True, null=True)
    provinsi = models.TextField(blank=True, null=True)
    pulau = models.TextField(blank=True, null=True)
    desa_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    kode_desa = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wilayah_indonesia'
