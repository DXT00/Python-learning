# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Novelcontent1(models.Model):
    novelhref = models.CharField(max_length=255, blank=True, null=True)
    imgsrc = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_recommend = models.CharField(max_length=255, blank=True, null=True)
    data_ack0 = models.CharField(max_length=255, blank=True, null=True)
    data_ack1 = models.CharField(max_length=255, blank=True, null=True)
    data_ack2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'novelcontent1'
