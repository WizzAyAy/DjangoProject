from django.http import HttpResponse
import datetime

from paper.models import Paper


def current_datetime(request):
    paper = Paper.objects.get(pk=1)
    now = datetime.datetime.now()
    html = "<html><body>paper titre :  %s.</body></html>" % paper.get_title()
    return HttpResponse(html)

