from django.db import models


class Paper(models.Model):
    paper_title = models.CharField(max_length=30)
    paper_year = models.CharField(max_length=30)

    def get_title(self):
        return self.paper_title

    def get_year(self):
        return self.paper_year

    def get_id(self):
        return self.id

    def safe_get_id(self, paper_id):
        try:
            paper = self.objects.get(id=paper_id)
        except Paper.DoesNotExist:
            paper = None
        return paper
