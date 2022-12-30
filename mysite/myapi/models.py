from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
