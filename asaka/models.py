from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Articles(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"