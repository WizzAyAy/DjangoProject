from django.db import models

# Create your models here.

class Information(models.Model):
    paper_id = models.CharField(max_length=30)
    patients = models.BooleanField()
    molecule = models.BooleanField()

    def get_patients(self):
        return self.patients

    def get_molecule(self):
        return self.molecule

    def get_id(self):
        return self.id