from django.db import models

from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.TextField(verbose_name='imagelink')
    release_date = models.DateField(blank=True, null=True, verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='В наличии')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def __str__(self):
        return f'Название: {self.name}, цена: {self.price}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
    

