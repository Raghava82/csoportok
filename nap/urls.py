from django.conf.urls import url
from . import views
from django.urls import path
#from django.conf.urls.defaults import patterns
#from wkhtmltopdf.views import PDFTemplateView

app_name = 'naptar'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
   # url(r'^pdf/$',views.GeneratePDF.as_view(), name='pdf'),
 #   url(r'^calendar/'
  #      r'pdf/$', PDFTemplateView.as_view(template_name='naptar/index.html',filename='naptar/naptar.pdf'), name='pdf'),
    #path('',views.index, name='index'),
    #path('calendar/',views.CalendarView.as_view(), name='calendar'),
    #path('event/new/',views.event, name='event_new'),
    #path('event/edit/',views.event, name='event_edit'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='nyomtatas'),
    ]
