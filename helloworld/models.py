from django.db import models


class Counter(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.value}"
