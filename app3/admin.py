from django.contrib import admin
from .models import ClueMedia
from .models import GPSData,DataStorage,WaypointsData

# Register your models here.
class ClueMediaAdmin(admin.ModelAdmin):
    def photo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
            )
    )
    pass
admin.site.register(ClueMedia, ClueMediaAdmin)

class GPSDataAdmin(admin.ModelAdmin):
    list_display = ['deviceid','taskid','gpsdata','created_at','updated_at']
    pass
admin.site.register(GPSData, GPSDataAdmin)
#admin.site.register(ClueMedia)

class DataStorageAdmin(admin.ModelAdmin):
    list_display = ['id','taskid','subtaskid','data','created_at','updated_at']
    pass
admin.site.register(DataStorage, DataStorageAdmin)

class WaypointsDataAdmin(admin.ModelAdmin):
    list_display = ['deviceid','taskid','waypointsdata','created_at','updated_at']
    pass
admin.site.register(WaypointsData, WaypointsDataAdmin)
