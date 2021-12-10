from django.db import models


class Paper(models.Model):
    paper_title = models.CharField(max_length=30)
    paper_year = models.CharField(max_length=30)
    paper_subject = models.CharField(max_length=30)
    paper_text = models.TextField()
    paper_most_used_words = models.TextField()

    def get_title(self):
        return self.paper_title

    def get_year(self):
        return self.paper_year

    def get_subject(self):
        return self.paper_subject

    def get_text(self):
        return self.paper_text

    def get_most_used_words(self):
        return self.paper_most_used_words

    def get_id(self):
        return self.id

    def safe_get_id(self, paper_id):
        try:
            paper = self.objects.get(id=paper_id)
        except Paper.DoesNotExist:
            paper = None
        return paper