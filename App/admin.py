from django.contrib import admin
from .models import Singer,Song

# Register your models here.

admin.site.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender']
    
admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','singe','title','duration']