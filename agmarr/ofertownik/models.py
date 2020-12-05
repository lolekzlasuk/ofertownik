from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.crypto import get_random_string




def slug_save(obj):
    """ A function to generate a 5 character slug and see if it has been used and contains naughty words."""
    if not obj.slug: # if there isn't a slug
        obj.slug = get_random_string(5) # create one
        slug_is_wrong = True
    while slug_is_wrong: # keep checking until we have a valid slug
        slug_is_wrong = False
        other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
        if len(other_objs_with_slug) > 0:
            # if any other objects have current slug
            slug_is_wrong = True
        if slug_is_wrong:
            # create another slug and check it again
            obj.slug = get_random_string(5)

class Offer(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title =  models.CharField(max_length=200)
    slug = models.SlugField(max_length=5,blank=True,)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        slug_save(self) # call slug_save, listed below
        super(Offer, self).save(*args, **kwargs)


class Product(models.Model):
    offer = models.ForeignKey('ofertownik.Offer',on_delete=models.CASCADE,related_name='products')
    name = models.TextField(max_length=500,blank=True)
    price = models.TextField(max_length=500,blank=True)
    size = models.CharField(max_length=500,blank=True)
    material = models.TextField(max_length=500,blank=True)
    description = models.TextField(max_length=500,blank=True)
    
    def __str__(self):
        return self.name
class ProductImage(models.Model):
    product = models.ForeignKey('ofertownik.Product',on_delete=models.CASCADE, related_name='images')
    adress = models.TextField(max_length=None)
