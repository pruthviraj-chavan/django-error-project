from django.db import models

class about(models.Model):
    my_title = models.CharField(max_length=100)
    my_desc = models.TextField()
