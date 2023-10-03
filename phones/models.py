from django.db import models

from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return f'{self.name}, {self.price}: {self.release_date}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
    

