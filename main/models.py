from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
# Create your models here.
class Area(models.Model):
    location = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.location

class Place(models.Model):
    name = models.CharField(max_length=120)
    Area = models.ForeignKey(to=Area, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{Category.name}'

class Events(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    description = models.TextField(null=True)
    Place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    Category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'Event {self.name} in {self.Place.name}'

class Excursion(models.Model):
    name = models.CharField(max_length=120)
    num_of_people_now = models.PositiveIntegerField(default=0)
    max_num_of_people = models.PositiveIntegerField()
    date = models.DateTimeField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField(null=True)
    Place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    Category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Excursion in {self.Place.name}'

class Guide(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='guide_images', null=True, blank=True)
    Excursion = models.ForeignKey(to=Excursion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Guide'
        verbose_name_plural = 'Guides'

    def __str__(self):
        return f'Guide {self.first_name} {self.last_name}'

class Hotels(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('0.01'))])
    phone = models.CharField(max_length=12)
    description = models.TextField(null=True)
    Category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    Place = models.ForeignKey(to=Place, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return f'{self.name} in {self.Place.Area.location}'
