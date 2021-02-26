from django.db import models
from django.urls import reverse


class Event(models.Model):
    csoport = models.CharField(max_length=200)
    kontakt_szemely = models.CharField(max_length=200)
    cim = models.CharField(max_length=200)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    datum = models.DateField()
    ido = models.TimeField(auto_now=False, auto_now_add=False)
    fizetve = models.BooleanField()
    letrehozva = models.DateField(blank=True, null=True)
    modositva = models.DateField(blank=True, null=True)
    szolgaltatasok = models.CharField(max_length=255, )
    jegy = models.IntegerField()
    megjegyzes = models.TextField()

    @property
    def get_html_url(self):
        url = reverse('naptar:event_edit', args=(self.id,))
        return f"""<a href="{url}"> {self.ido}, {self.csoport}, {self.kontakt_szemely},\n\r {self.telefon}, {self.szolgaltatasok},\n\r  Vendégek száma: {self.jegy}</a>"""
