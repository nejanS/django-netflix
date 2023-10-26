from django.contrib import admin
from .models import *

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ('category',)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ('category',)

class PopularAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ('category',)

class NetflixAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Series, SeriesAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Popular, PopularAdmin)
admin.site.register(Netflix, NetflixAdmin)
admin.site.register(Category, CategoryAdmin)

class SeriesInline(admin.TabularInline):
    model = Series

class MoviesInline(admin.TabularInline):
    model = Movies 
    
class PopularInline(admin.TabularInline):
    model = Popular 
    
class NetflixInline(admin.TabularInline):
    model = Popular 
    
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SeriesInline, MoviesInline, PopularInline]

admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)
