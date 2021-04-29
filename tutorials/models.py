from django.db import models
from categories import models as category
from django.db.models import F


class Tutorial(models.Model):
    pub_date = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(category.Catergory, on_delete=models.CASCADE, default=1)
    tutorial_text = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    url_friendly_text = models.CharField(max_length=50)
    created_by = models.CharField(max_length=30, default='admin')
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs): # new
        category.Catergory.objects.filter(id=self.category.id).update(tuitorials_number=F('tuitorials_number') + 1)
        if not self.url_friendly_text:
            self.url_friendly_text = slugify(self.tutorial_text)
        return super().save(*args, **kwargs)

    def __str__(self):
      return self.tutorial_text

    def delete(self, *args, **kwargs):
        category.Catergory.objects.filter(id=self.category.id).update(tuitorials_number=F('tuitorials_number') - 1)
        return super().delete(*args, **kwargs)

class Contentblock(models.Model):
    description = models.CharField(max_length=30)
    is_visible = models.BooleanField(default=False)
    def __str__(self):
      return self.description



