from django.db import models
from subjects import models as subject

class Catergory(models.Model):
    category_text = models.CharField(max_length=30)
    subject = models.ForeignKey(subject.Subject, on_delete=models.CASCADE, default=1)
    tuitorials_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    url_friendly_text = models.CharField(max_length=30, default='url-friendly-category-name')

    def __str__(self):
      return self.category_text

