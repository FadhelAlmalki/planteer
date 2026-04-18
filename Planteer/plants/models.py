from django.db import models

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

