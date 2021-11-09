import logging
import requests
from django.shortcuts import render

from paper.models import Paper

logger = logging.getLogger('project.interesting.stuff')


def view(request):
    paper_id = 22368089
    response = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=' + str(paper_id))
    logger.error(response.text)
    context = {
        'date': response.text
    }
    return render(request, 'paperInformation.html', context)


def get_paper(request):
    retmax = 10
    response = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term=covid 19&retmax=' + str(retmax) +'&retmode=json')
    json = response.json()
    id_list = json['esearchresult']['idlist']
    context = {
        'date': id_list,
    }
    for paper_id in id_list:
        paper = Paper.safe_get_id(Paper, paper_id)
        if paper is None:
            response = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id='+ str(paper_id) + '&retmode=json').json()
            Paper.objects.create(
                id=paper_id,
                paper_title=response['result'][paper_id]['title'],
                paper_year=response['result'][paper_id]['pubdate']
            )

    return render(request, 'paperInformation.html', context)
