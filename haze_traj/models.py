# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Haze_traj_db(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
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
    objects= models.Manager()
    class Meta:
        managed = False
        db_table = 'new_hotspot'
        
class HotspotSipongi(models.Model):
    hs_id = models.DateTimeField(blank=True, primary_key=True)
    date_hotspot_ori = models.DateTimeField(blank=True, null=True)
    provinsi_id = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    sumber = models.CharField(max_length=25, blank=True, null=True)
    ori_sumber = models.CharField(max_length=25, blank=True, null=True)
    date_hotspot = models.CharField(max_length=50, blank=True, null=True)
    desa_id = models.CharField(max_length=255,blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    confidence_level = models.CharField(max_length=10, blank=True, null=True)
    kawasan = models.CharField(max_length=255, blank=True, null=True)
    desa = models.CharField(max_length=255, blank=True, null=True)
    kecamatan = models.CharField(max_length=255, blank=True, null=True)
    kabkota = models.CharField(max_length=255, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=255, blank=True, null=True)
    pulau = models.CharField(max_length=255, blank=True, null=True)
    objects= models.Manager()
    class Meta:
        managed = False
        db_table = 'hotspot_sipongi'

        

