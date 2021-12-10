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


def graph(request):
    context = {
        'numberOfPaper': 12,
        'molecules': ['molecule1', 'molecule2', 'molecule3', 'molecule4', 'molecule5', 'molecule6', 'molecule7',
                      'molecule8'],
        'molecules_values': [50, 10, 5, 6, 8, 50, 30, 10],
        'vaccines': ['moderna', 'physez'],
        'vaccines_values': [50, 5]
    }
    return render(request, '../templates/graph.html', context)
