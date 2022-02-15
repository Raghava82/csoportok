from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm

from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse
import pdfcrowd
import sys

class CalendarView(generic.ListView):
    model = Event
    template_name = 'naptar/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)


        try:
            # create the API client instance
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

            # configure the conversion
            client.setPageSize(u'A3')
            client.setOrientation(u'landscape')
            client.setNoMargins(True)

            # run the conversion and write the result to a file
            client.convertFileToFile('/home/raghava/Projects/groups/naptar/templates/naptar/index.html',
                                     'letter_landscape.pdf')
        except pdfcrowd.Error as why:
            # report the error
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

            # rethrow or handle the exception
            raise
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('naptar:calendar'))
    return render(request, 'naptar/event.html', {'form': form})


#def pdf_generation(request):
    #html_template = get_template('naptar/naptar.html')
    #pdf_file = HTML(string=html_template).write_pdf()
    #response = HttpResponse(pdf_file, content_type='application/pdf')
    #response['Content-Disposition'] = 'filename="naptar.pdf"'
    #return response




#def nyomtatas(request):
 #   context = {}
  #  return render(request, 'naptar/nyomtatas.html',context)



def index(request):

    return render(request,'naptar/index.html')


  #  return render(request, 'naptar/index.html')
