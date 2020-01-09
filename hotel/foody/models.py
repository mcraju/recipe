from django.db import models


class Foody(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=200)
    process = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
