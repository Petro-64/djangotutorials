from django.db import models
from categories import models as category

class Tutorial(models.Model):
    pub_date = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(category.Catergory, on_delete=models.CASCADE, default=1)
    tutorial_text = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    url_friendly_text = models.CharField(max_length=50, default='url-friendly-tutorial-name')
    created_by = models.CharField(max_length=30, default='admin')
    views = models.IntegerField(default=0)
    def __str__(self):
      return self.tutorial_text

class Contentblock(models.Model):
    description = models.CharField(max_length=30)
    is_visible = models.BooleanField(default=False)
    def __str__(self):
      return self.description



