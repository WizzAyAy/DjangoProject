from django.db import models

# Create your models here.

class Information(models.Model):
    paper_id = models.CharField(max_length=30)
    info_patient = models.BooleanField()
    info_molecule = models.BooleanField()
    info_ronapreve = models.BooleanField()
    info_molnupiravir = models.BooleanField()
    info_remdesivir = models.BooleanField()
    info_hydroxychloroquine = models.BooleanField()
    info_colchicine = models.BooleanField()
    info_azithromycine = models.BooleanField()
    info_avigan = models.BooleanField()
    info_anakinra = models.BooleanField()
    info_pfizer = models.BooleanField()
    info_moderna = models.BooleanField()
    info_astrazeneca = models.BooleanField()


    def get_id(self):
        return self.id

    def safe_get_id(self, paper_id):
        try:
            paper = self.objects.get(id=paper_id)
        except Information.DoesNotExist:
            paper = None
        return paper

    def get_patient(self):
        return self.info_patient

    def get_molecule(self):
        return self.info_molecule

    def get_ronapreve(self):
        return self.info_ronapreve

    def get_molnupiravir(self):
        return self.info_molnupiravir
    
    def get_remdesivir(self):
        return self.info_remdesivir

    def get_hydroxychloroquine(self):
        return self.info_hydroxychloroquine

    def get_colchicine(self):
        return self.info_colchicine

    def get_azithromycine(self):
        return self.info_azithromycine

    def get_avigan(self):
        return self.info_avigan

    def get_anakinra(self):
        return self.info_anakinra

    def get_pfizer(self):
        return self.info_pfizer

    def get_moderna(self):
        return self.info_moderna

    def get_astrazeneca(self):
        return self.info_astrazeneca
