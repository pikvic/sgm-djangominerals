from django.contrib import admin

from .models import Mineral, Material, Item, Element, MineralUses, ElementUses

admin.site.register(Mineral)
admin.site.register(Material)
admin.site.register(Item)
admin.site.register(Element)
admin.site.register(MineralUses)
admin.site.register(ElementUses)