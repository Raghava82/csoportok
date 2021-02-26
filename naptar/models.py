from django.db import models
from django.urls import reverse

class Service(models.Model):
    ZENE_VARAZSA = 'ZV'
    KELET_DIVATJA = 'KD'
    EGZOTIKUS_FUSZERKALAUZ = 'EF'
    LELEK_HANGJA = 'LH'
    ZARANDOKKORUT = 'ZK'
    KORTURA = 'KK'
    OKO_TANOSVENY = 'OT'
    EBED = 'EB'
    ETELKOSTOLO = 'ET'
    Service_choices = [
        (ZENE_VARAZSA, 'Zene varázsa'),
        (KELET_DIVATJA, 'KElet divatja'),
        (EGZOTIKUS_FUSZERKALAUZ , 'Egzotikus fűszerkalauz'),
        (LELEK_HANGJA, 'Lélek Hangja'),
        (ZARANDOKKORUT, 'Szerencsét hozó zarándokkörút'),
        (KORTURA, 'Krisna-völgyi Körtúra'),
        (OKO_TANOSVENY, 'Öko Tanösvény'),
        (EBED, 'Ebéd'),
        (ETELKOSTOLO, 'Ételkóstoló'),
    ]


#    def is_upperclass(self):
#        return self.choosed_services in {self.JUNIOR, self.SENIOR}


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
    szolgaltatasaink = models.CharField(
        max_length=2,
        choices=Service.Service_choices,
        default=Service.KORTURA,
    )

    @property
    def get_html_url(self):
        url = reverse('naptar:event_edit', args=(self.id,))
        return f"""<a href="{url}"> {self.ido}, {self.csoport}, {self.kontakt_szemely},\n\r {self.telefon}, {self.szolgaltatasok},\n\r  Vendégek száma: {self.jegy}, {self.szolgaltatasaink}</a>"""
