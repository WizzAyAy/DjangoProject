from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from paper.models import Paper


def index(request):
    paper_list = Paper.objects.all()
    context = {'paper_list': paper_list}
    return render(request, 'paperList.html', context)


def view(request):
    paper_id = RequestContext(request, 'paper')
    paper = get_object_or_404(Paper, pk=paper_id)
    context = {'paper': paper}
    return render(request, 'paper.html', context)
