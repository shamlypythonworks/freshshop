from django.contrib import admin
from . models import *
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('ctname',)}
    list_display=['ctname','slug','img']
admin.site.register(categtable,catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(prdttable,prodadmin)