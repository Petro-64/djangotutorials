from django.db import models

class Catergory(models.Model):
    category_text = models.CharField(max_length=30)

    def __str__(self):
      return self.category_text

