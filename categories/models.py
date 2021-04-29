from django.db import models
from subjects import models as subject
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db.models import F



class Catergory(models.Model):
    category_text = models.CharField(max_length=30)
    subject = models.ForeignKey(subject.Subject, on_delete=models.CASCADE, default=1)
    tuitorials_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    url_friendly_text = models.CharField(max_length=30)

    def __str__(self):
        return self.category_text

    def save(self, *args, **kwargs):
        subject.Subject.objects.filter(id=self.subject.id).update(categories_number=F('categories_number') + 1)
        if not self.url_friendly_text:
            self.url_friendly_text = slugify(self.category_text)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        subject.Subject.objects.filter(id=self.subject.id).update(categories_number=F('categories_number') - 1)
        return super().delete(*args, **kwargs)