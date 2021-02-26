from django.forms import ModelForm, DateInput, TimeInput
from naptar.models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'datum': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      'ido': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['datum'].input_formats = ('%Y-%m-%d',)
    self.fields['ido'].input_formats = ('%H:%M',)
