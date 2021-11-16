import logging
import requests
from django.http import HttpResponseNotFound
from django.shortcuts import render
from lxml import etree

from paper.models import Paper

logger = logging.getLogger('project.interesting.stuff')


def generate_new_papers(request):
    return render(request, '../templates/generateNewPapers.html')


def get_paper_from_api(request):
    retmax = request.POST.get('number_papers')
    subject = request.POST.get('subject')

    if retmax is None or subject is None:
        return HttpResponseNotFound('Bad arguments')

    response = requests.get(
        'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term=' + subject + '&retmax=' + str(
            retmax) + '&retmode=json')
    json = response.json()
    id_list = json['esearchresult']['idlist']

    added_papers = 0
    for paper_id in id_list:
        paper = Paper.safe_get_id(Paper, paper_id)
        if paper is None:

            added_papers = added_papers + 1

            # url pour recup les métas données
            response_meta = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id=' + str(
                paper_id) + '&retmode=json').json()

            # url pour recup le text
            response_text = requests.get(
                'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=' + str(paper_id))
            tree = etree.fromstring(response_text.text)
            xmlstr = ""
            for elem in list(tree.iter('body')):
                xmlstr = etree.tostring(elem, encoding='utf8', method='xml')

            Paper.objects.create(
                id=paper_id,
                paper_title=response_meta['result'][paper_id]['title'],
                paper_subject=subject,
                paper_year=response_meta['result'][paper_id]['pubdate'],
                paper_text=xmlstr
            )

    paper_list = Paper.objects.all()

    context = {
        'paper_list': paper_list,
        'added_papers': added_papers,
        'subject': subject
    }

    return render(request, '../templates/paperList.html', context)
