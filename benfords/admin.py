from django.contrib import admin

from benfords.models import DataSet


@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    pass