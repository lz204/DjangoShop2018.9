from django.contrib import admin
from .models import 产品列表, 商品类别表
# Register your models here.

# 商品列表
class 商品类别表Admin(admin.ModelAdmin):
    list_display = ['id', '名称', '图片']

admin.site.register(商品类别表, 商品类别表Admin)

# 产品列表
class 产品列表Admin(admin.ModelAdmin):
    list_display = ['id', '名称', '图片', '所属类别', '价格', '库存', '上架情况', '创建时间', '修改时间']
    list_editable = ['名称', '所属类别', '价格', '库存', '上架情况']
    list_per_page = 10

admin.site.register(产品列表, 产品列表Admin)
