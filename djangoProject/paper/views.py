from django.shortcuts import render, get_object_or_404
from paper.models import Paper


def index(request):
    paper_list = Paper.objects.all()
    context = {'paper_list': paper_list}
    return render(request, '../templates/paperList.html', context)


def view(request):
    paper = get_object_or_404(Paper, pk=request.POST.get('paper'))
    context = {'paper': paper}
    return render(request, '../templates/paper.html', context)
