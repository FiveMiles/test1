from django.contrib import admin
from .models import *


# 关联对象
# StackedInline 列表，TabularInline表格
class HeraInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3





class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']}),
    ]

    inlines = [HeraInfoInline]



# Register your models here.

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)