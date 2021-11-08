from django.db import models

class Bascet(models.Model):
    title = models.CharField("Название продукта", max_length=50)
    anonse = models.CharField("Описание продукта", max_length=250)
    price = models.IntegerField("Цена продукта")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
