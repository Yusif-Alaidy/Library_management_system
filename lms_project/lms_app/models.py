from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    status_book = [
        ('avalible','avalible'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to='photos')
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2,)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    totale_rental = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title