from django.contrib import admin

from .models import DataPoint


class DataPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'value', 'longitude', 'latitude', 'date', )
    inlines = []
    readonly_fields = ()

    search_fields = ['id']

admin.site.register(DataPoint, DataPointAdmin)
