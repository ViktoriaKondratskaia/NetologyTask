from django.db import models


class Phone(models.Model):
    #TODO: Добавьте требуемые поля
    #id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'






