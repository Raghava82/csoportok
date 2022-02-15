from django.contrib import admin
from naptar.models import Event

# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    list_display = ('csoport', 'kontakt_szemely', 'cim', 'email', 'datum', 'ido','fizetve','letrehozva', 'modositva',
                    'szolgaltatasok','jegy', 'megjegyzes')


admin.site.register(Event, GroupAdmin)