from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['uphone', 'upwd', 'uemail', 'uname']
    fields = ['uname', 'uphone', 'uemail']
admin.site.register(User, UserAdmin)
admin.site.register(Goods)
admin.site.register(GoodsType)