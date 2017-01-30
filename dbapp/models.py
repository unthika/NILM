# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class ElectricityB1E(models.Model):
    unix_ts = models.IntegerField(primary_key=True)
    v = models.FloatField(db_column='V')  # Field name made lowercase.
    i = models.FloatField(db_column='I')  # Field name made lowercase.
    f = models.FloatField()
    dpf = models.FloatField(db_column='DPF')  # Field name made lowercase.
    apf = models.FloatField(db_column='APF')  # Field name made lowercase.
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.
    s = models.IntegerField(db_column='S')  # Field name made lowercase.
    st = models.IntegerField(db_column='St')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electricity_b1e'


class ElectricityCwe(models.Model):
    unix_ts = models.IntegerField(primary_key=True)
    v = models.FloatField(db_column='V')  # Field name made lowercase.
    i = models.FloatField(db_column='I')  # Field name made lowercase.
    f = models.FloatField()
    dpf = models.FloatField(db_column='DPF')  # Field name made lowercase.
    apf = models.FloatField(db_column='APF')  # Field name made lowercase.
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.
    s = models.IntegerField(db_column='S')  # Field name made lowercase.
    st = models.IntegerField(db_column='St')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electricity_cwe'


class ElectricityDwe(models.Model):
    unix_ts = models.IntegerField(primary_key=True)
    v = models.FloatField(db_column='V')  # Field name made lowercase.
    i = models.FloatField(db_column='I')  # Field name made lowercase.
    f = models.FloatField()
    dpf = models.FloatField(db_column='DPF')  # Field name made lowercase.
    apf = models.FloatField(db_column='APF')  # Field name made lowercase.
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.
    s = models.IntegerField(db_column='S')  # Field name made lowercase.
    st = models.IntegerField(db_column='St')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electricity_dwe'


class ElectricityFge(models.Model):
    unix_ts = models.IntegerField(primary_key=True)
    v = models.FloatField(db_column='V')  # Field name made lowercase.
    i = models.FloatField(db_column='I')  # Field name made lowercase.
    f = models.FloatField()
    dpf = models.FloatField(db_column='DPF')  # Field name made lowercase.
    apf = models.FloatField(db_column='APF')  # Field name made lowercase.
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.
    s = models.IntegerField(db_column='S')  # Field name made lowercase.
    st = models.IntegerField(db_column='St')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electricity_fge'


class PreDayElectricityCwe(models.Model):
    date_day = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_day_electricity_cwe'


class PreDayElectricityDwe(models.Model):
    date_day = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_day_electricity_dwe'


class PreDayElectricityFge(models.Model):
    date_day = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_day_electricity_fge'


class PreElectricityCwe(models.Model):
    time_ts = models.CharField(primary_key=True, max_length=18)
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_electricity_cwe'


class PreElectricityDwe(models.Model):
    time_ts = models.CharField(primary_key=True, max_length=18)
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_electricity_dwe'


class PreElectricityFge(models.Model):
    time_ts = models.CharField(primary_key=True, max_length=18)
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    pt = models.IntegerField(db_column='Pt')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    qt = models.IntegerField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_electricity_fge'


class PreHourElectricityCwe(models.Model):
    datetime_hour = models.CharField(primary_key=True, max_length=18)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_hour_electricity_cwe'


class PreHourElectricityDwe(models.Model):
    datetime_hour = models.CharField(primary_key=True, max_length=18)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_hour_electricity_dwe'


class PreHourElectricityFge(models.Model):
    datetime_hour = models.CharField(primary_key=True, max_length=18)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_hour_electricity_fge'


class PreMonthElectricityCwe(models.Model):
    date_month = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_month_electricity_cwe'


class PreMonthElectricityDwe(models.Model):
    date_month = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_month_electricity_dwe'


class PreMonthElectricityFge(models.Model):
    date_month = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_month_electricity_fge'


class PreYearElectricityCwe(models.Model):
    date_year = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_year_electricity_cwe'


class PreYearElectricityDwe(models.Model):
    date_year = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_year_electricity_dwe'


class PreYearElectricityFge(models.Model):
    date_year = models.DateField(primary_key=True)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_year_electricity_fge'
		
class ClusterElectricityCwe(models.Model):
    time_ts = models.CharField(max_length=18)
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_electricity_cwe'


class ClusterElectricityDwe(models.Model):
    time_ts = models.CharField(max_length=18)
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_electricity_dwe'


class ClusterElectricityFge(models.Model):
    time_ts = models.CharField(max_length=18)
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_electricity_fge'


class ClusterPreHourElectricityCwe(models.Model):
    datetime_hour = models.CharField(primary_key=True, max_length=18)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_hour_electricity_cwe'


class ClusterPreHourElectricityDwe(models.Model):
    datetime_hour = models.CharField(primary_key=True, max_length=18)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_hour_electricity_dwe'


class ClusterPreHourElectricityFge(models.Model):
    datetime_hour = models.CharField(primary_key=True, max_length=18)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_hour_electricity_fge'
		
class ClusterPreDayElectricityFge(models.Model):
    date_day = models.CharField(primary_key=True, max_length=8)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.
    meaningmodel = models.TextField(db_column='MeaningModel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_day_electricity_fge'

class ClusterPreDayElectricityCwe(models.Model):
    date_day = models.CharField(primary_key=True, max_length=8)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.
    meaningmodel = models.TextField(db_column='MeaningModel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_day_electricity_cwe'


class ClusterPreDayElectricityDwe(models.Model):
    date_day = models.CharField(primary_key=True, max_length=8)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.
    meaningmodel = models.TextField(db_column='MeaningModel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_day_electricity_dwe'

class ClusterPreMonthElectricityDwe(models.Model):
    date_month = models.CharField(primary_key=True, max_length=8)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.
    meaningmodel = models.TextField(db_column='MeaningModel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_month_electricity_dwe'


class ClusterPreMonthElectricityFge(models.Model):
    date_month = models.CharField(primary_key=True, max_length=8)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.
    meaningmodel = models.TextField(db_column='MeaningModel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_month_electricity_fge'
		
class ClusterPreMonthElectricityCwe(models.Model):
    date_month = models.CharField(primary_key=True, max_length=8)
    p = models.FloatField(db_column='P')  # Field name made lowercase.
    pt = models.FloatField(db_column='Pt')  # Field name made lowercase.
    q = models.FloatField(db_column='Q')  # Field name made lowercase.
    qt = models.FloatField(db_column='Qt')  # Field name made lowercase.
    label = models.IntegerField(db_column='Label')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning')  # Field name made lowercase.
    meaningmodel = models.TextField(db_column='MeaningModel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster_pre_month_electricity_cwe'
