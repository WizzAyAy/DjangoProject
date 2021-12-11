from django.shortcuts import render, get_object_or_404
from paper.models import Paper
from information.models import Information
import logging

logger = logging.getLogger('project.interesting.stuff')


def index(request):
    paper_list = Paper.objects.all()
    context = {'paper_list': paper_list}
    return render(request, '../templates/paperList.html', context)


def index_specific(request):
    word = request.POST.get('wordToCompare')
    paper_list = Paper.objects.all()
    paper_list_to_send = []
    for paper in paper_list:
        if word in str(paper.get_most_used_words()):
            paper_list_to_send.append(paper)

    context = {'paper_list': paper_list_to_send, 'paper_word': word}
    return render(request, '../templates/paperList.html', context)


def view(request):
    paper = get_object_or_404(Paper, pk=request.POST.get('paper'))
    context = {'paper': paper}
    return render(request, '../templates/paper.html', context)


def graph(request):
    informations = Information.objects.all()
    dict_molecules = {
        'ronapreve': 0,
        'olnupiravir': 0,
        'remdesivir': 0,
        'hydroxychloroquine': 0,
        'colchicine': 0,
        'azithromycine': 0,
        'avigan': 0,
        'anakinra': 0,
    }
    dict_vaccines = {
        'pfizer': 0,
        'moderna': 0,
        'astrazeneca': 0,
    }
    for information in informations:
        for key in dict_molecules.keys():
            if information.get_molecule(name=key) is True:
                dict_molecules[key] += 1
        for key in dict_vaccines.keys():
            if information.get_vaccines(name=key) is True:
                dict_vaccines[key] += 1

    context = {
        'numberOfPaper': len(Paper.objects.all()),
        'molecules': list(dict_molecules.keys()),
        'molecules_values': list(dict_molecules.values()),
        'vaccines': list(dict_vaccines.keys()),
        'vaccines_values': list(dict_vaccines.values())
    }
    return render(request, '../templates/graph.html', context)
