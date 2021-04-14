from django.db import models


class Subject(models.Model):
    subject_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    categories_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
# Create your models here.
