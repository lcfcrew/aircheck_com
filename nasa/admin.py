from django.contrib import admin

from .models import DiscretizedDataPoint, NasaDataFile


class DiscretizedDataPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'value', 'longitude', 'latitude', 'date', )
    inlines = []
    readonly_fields = ()

    search_fields = ['id']

class NasaDataFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection_short_name', 'collection_long_name', 'hdf', 'xml', 'bounding_west', 'bounding_north', 'bounding_east', 'bounding_south', 'date', )
    inlines = []
    readonly_fields = ()

    search_fields = ['id']

admin.site.register(DiscretizedDataPoint, DiscretizedDataPointAdmin)
admin.site.register(NasaDataFile, NasaDataFileAdmin)
