from django.db import models


class Paper(models.Model):
    paper_title = models.CharField(max_length=30)
    paper_year = models.IntegerField()

    def get_title(self):
        return self.paper_title

    def get_year(self):
        return self.paper_year
