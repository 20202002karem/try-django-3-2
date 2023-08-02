from django.db import models
from django.conf import settings
from .validators import validat_unit_of_measure
# Create your models here.

User = settings.AUTH_USER_MODEL
class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE )
    name = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(null=True,blank=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50,validators=[validat_unit_of_measure])
    directions = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    