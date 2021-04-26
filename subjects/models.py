from django.db import models


class Subject(models.Model):
    subject_text = models.CharField(max_length=30, unique=True)
    pub_date = models.DateTimeField(auto_now_add = True)
    categories_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    url_friendly_text = models.CharField(max_length=30, default='subject_name')

    def __str__(self):
      return self.subject_text
# Create your models here.
