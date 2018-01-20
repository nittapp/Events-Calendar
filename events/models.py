from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    end = models.DateTimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events')

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)