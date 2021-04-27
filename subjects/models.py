from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Subject(models.Model):
    subject_text = models.CharField(max_length=30, unique=True)
    pub_date = models.DateTimeField(auto_now_add = True)
    categories_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    url_friendly_text = models.CharField(max_length=30)

    def __str__(self):
      return self.subject_text

    def save(self, *args, **kwargs): # new
        if not self.url_friendly_text:
            self.url_friendly_text = slugify(self.subject_text)
        return super().save(*args, **kwargs)

# Create your models here.
