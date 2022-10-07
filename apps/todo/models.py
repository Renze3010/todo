from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):

    name = models.CharField(max_length = 45, null=False)
    description = models.TextField()
    date = models.DateField()
    deadline = models.DateField()
    userID = models.IntegerField()


    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
