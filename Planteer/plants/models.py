from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    flag = models.ImageField(upload_to='flags/')

    def __str__(self):
        return self.name


class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        FLOWER = 'flower', 'Flower'
        TREE = 'tree', 'Tree'
        HERB = 'herb', 'Herb'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30, choices=CategoryChoices.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.name


class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author + ' on ' + self.plant.name