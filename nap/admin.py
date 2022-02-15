from django.contrib import admin
from naptar.models import Event

# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    list_display = ('csoport', 'kontakt_szemely', 'cim', 'email', 'datum', 'fizetve','letrehozva', 'modositva',
                    'szolgaltatasok','felnott_jegy', 'kedvezmenyes_jegy', 'megjegyzes')


admin.site.register(Event, GroupAdmin)