from django.contrib import admin
from store.models import Tshirt,Brand,Colour,IdealFor,Necktype,Occasion,Sleeve,SizeVarient
class SizeVarientConfiguration(admin.TabularInline):
    model= SizeVarient
class TshirtConfiguration(admin.ModelAdmin):
    inlines= [SizeVarientConfiguration]


admin.site.register(Tshirt,TshirtConfiguration)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(IdealFor)
admin.site.register(Necktype)
admin.site.register(Occasion)
admin.site.register(Sleeve)
