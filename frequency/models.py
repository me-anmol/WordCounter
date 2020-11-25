from django.db import models


class word(models.Model):
    url = models.URLField()
    wordh = models.CharField(max_length = 100)
    freq = models.IntegerField()
