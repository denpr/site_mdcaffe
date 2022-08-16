from django.contrib import admin
from .models import Category
from .models import MenuItem
from .models import IncomingMessage
from .models import InformCategory
from .models import InformBlockMenuContent

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(IncomingMessage)
admin.site.register(InformCategory)
admin.site.register(InformBlockMenuContent)
