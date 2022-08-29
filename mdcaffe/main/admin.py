from django.contrib import admin
from .models import Category
from .models import MenuItem
from .models import IncomingMessage
from .models import InformCategory
from .models import InformBlockMenuContent

admin.site.register(Category)
admin.site.register(InformCategory)


@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):
    list_display = ("category", "title", "price_float", "position", "cover")
    def get_cover(self, obj):
        return mark_safe(f'<img src={obj.cover.url} width="50" heigth="50"')
    get_cover.short_description = "Изображение"


@admin.register(IncomingMessage)
class IncomingMessage(admin.ModelAdmin):
    list_display = ("created", "name", "phone", "email","answered")
    
    
@admin.register(InformBlockMenuContent)
class InformBlockMenuContent(admin.ModelAdmin):
    list_display = ("informCategory", "title", "weight", "price_float", "position")

