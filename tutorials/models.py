from django.db import models
from categories import models as category
from django.db.models import F
import time
import math
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode


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

    def fill_tutorial(self):
        #/admin/tutorials/tutorial/17/change/
        url = (
            reverse("admin:tutorials_contentcontent_changelist")
            + "?"
            + urlencode({"tutorial_id": f"{self.id}"})
        )
        #return format_html("<a href='/admin/tutorials/tutorial/{}/change/'>Edit</a>", self.id)
        return format_html('<a href="{}">Fill tutorial</a>', url)

    def get_subject(self):
        return self.category.subject

    def get_category(self):
        return self.category

    get_subject.short_description = 'Subjects'

    def delete(self, *args, **kwargs):
        category.Catergory.objects.filter(id=self.category.id).update(tuitorials_number=F('tuitorials_number') - 1)
        return super().delete(*args, **kwargs)

class Contentblock(models.Model):
    description = models.CharField(max_length=30)
    is_visible = models.BooleanField(default=False)
    def __str__(self):
      return self.description

class Contentcontent(models.Model):
    content = models.CharField(max_length=3000)
    mediapath = models.CharField(max_length=3000, default='')
    is_visible = models.BooleanField(default=False)
    tutorial_id = models.ForeignKey(Tutorial, on_delete=models.CASCADE, default=1)
    block_id = models.ForeignKey(Contentblock, on_delete=models.CASCADE, default=1)
    order = models.IntegerField(default=0)

    def get_block(self):
        return self.block_id

    def tutorial(self):
        return self.tutorial_id

    def block_up(self):
        return format_html('<a href="#" class="link-move-up" data-contentid="{}">Move up</a>', self.id)
    
    def block_down(self):
        return format_html('<a href="#" class="link-move-down" data-contentid="{}">Move down</a>', self.id)    

    def save_order(self):
        # this is for being able to change order later, just swap 
        self.order = math.ceil(time.time())

    def save(self, *args, **kwargs):
        self.save_order()        
        super(Contentcontent, self).save(*args, **kwargs)
    
    def __str__(self):
      return self.content


