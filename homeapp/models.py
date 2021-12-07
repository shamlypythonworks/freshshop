from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class categtable(models.Model):
    ctname = models.CharField(max_length=100,unique=True,primary_key=True)
    slug = models.SlugField(max_length=100,unique=True)
    img = models.ImageField(upload_to='images')
    class Meta:
        ordering=('ctname',)
        verbose_name= 'category'
        verbose_name_plural= 'categories'
    def get_url(self):
        return reverse('categwiseview',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.ctname)
class prdttable(models.Model):
    name = models.CharField(max_length=100,unique=True,primary_key=True)
    slug = models.SlugField(max_length=100,unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey(categtable,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)
    def get_url_review(self):
        return reverse('reviewpage',args=[self.slug])
    def get_url(self):
        return reverse('detailpage',args=[self.category.slug,self.slug])
