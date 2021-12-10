import logging
import math
import re
from operator import itemgetter

import requests
from django.http import HttpResponseNotFound
from django.shortcuts import render
from lxml import etree
from nltk import tokenize
from nltk.corpus import stopwords
from information.models import Information

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
                xmlstr = etree.tostring(elem, encoding='utf8', method='text')
            xmlstr = str(xmlstr)
            xmlstr = " ".join(xmlstr.split())
            xmlstr = xmlstr.replace('\\n', '\n\r')
            xmlstr = xmlstr.replace('\\', '')
            xmlstr = xmlstr.replace('b"', '')
            xmlstr = xmlstr.replace('b\'', '')
            xmlstr = re.sub(
                r'[\]x[0-9]*',
                '',
                xmlstr
            )
            most_used_words = get_most_used_word(xmlstr)
            most_used_words_string = ""

            for index, most_used_word in enumerate(most_used_words):
                if index == 0:
                    most_used_words_string += most_used_word
                else:
                    most_used_words_string += ", " + most_used_word
            
            getMolecules(xmlstr)

            Paper.objects.create(
                id=paper_id,
                paper_title=response_meta['result'][paper_id]['title'],
                paper_subject=subject,
                paper_year=response_meta['result'][paper_id]['pubdate'],
                paper_text=xmlstr,
                paper_most_used_words=most_used_words_string,
            )

            text = xmlstr.lower()

            Information.objects.create(
                paper_id = paper_id,
                info_patient = checkword(text, "patients"),
                info_molecule = checkword(text, "molecule"),
                info_ronapreve = checkword(text, "ronapreve"),
                info_molnupiravir = checkword(text, "molnupiravir"),
                info_remdesivir = checkword(text, "remdesivir"),
                info_hydroxychloroquine = checkword(text, "hydroxychloroquine"),
                info_colchicine = checkword(text, "colchicine"),
                info_azithromycine = checkword(text, "azithromycine"),
                info_avigan = checkword(text, "avigan"),
                info_anakinra = checkword(text, "anakinra"),
                info_pfizer = checkword(text, "pfizer"),
                info_moderna = checkword(text, "moderna"),
                info_astrazeneca = checkword(text, "astrazeneca")
            )
    
    

    paper_list = Paper.objects.all()

    context = {
        'paper_list': paper_list,
        'added_papers': added_papers,
        'subject': subject
    }

    return render(request, '../templates/paperList.html', context)


def check_sent(word, sentences):
    final = [all([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))


def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key=itemgetter(1), reverse=True)[:n])
    return result


def get_most_used_word(text):
    stop_words = set(stopwords.words('english'))
    total_words = text.split()
    total_word_length = len(total_words)

    total_sentences = tokenize.sent_tokenize(text)
    total_sent_len = len(total_sentences)

    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    tf_score.update((x, y / int(total_word_length)) for x, y in tf_score.items())

    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    try:
        idf_score.update((x, math.log(int(total_sent_len) / y)) for x, y in idf_score.items())
        tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
    except:
        return []

    key_word = get_top_n(tf_idf_score, 10)
    keys = key_word.keys()
    return keys




def checkword(text, word):
    if(word in text):
        return True
    else:
        return False

def getMolecules(text):
    pass