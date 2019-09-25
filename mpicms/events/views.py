from django.http import HttpResponse

from .models import EventIndex


def ics_view(request):
    index = EventIndex.objects.first()
    response = HttpResponse(index.ics, content_type="text/calendar") 
    response["Content-disposition"] = "attachment; filename=calendar.ics"
    return response
