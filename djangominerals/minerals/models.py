from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length=200)

class Element(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    materials = models.ManyToManyField(Material)
    items = models.ManyToManyField(Item)

class Mineral(models.Model):
    name = models.CharField(max_length=200)
    elements = models.ManyToManyField(Element)
    materials = models.ManyToManyField(Material)
    items = models.ManyToManyField(Item)

class MineralUses(models.Model):
    text = models.TextField()
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE)

class ElementUses(models.Model):
    text = models.TextField()
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE)
