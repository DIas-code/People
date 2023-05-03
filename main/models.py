from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from users .models import User
# Create your models here.
class Area(models.Model):
    location = models.CharField(max_length=120, unique=True)
    image = models.ImageField(upload_to='areas_image')
    # description = models.TextField()

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.location

class Place(models.Model):
    name = models.CharField(max_length=120, unique=True)
    area = models.ForeignKey(to=Area, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

class Events(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='events_image')
    date = models.DateTimeField()
    description = models.TextField(null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('0.01'))])
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'Event {self.name} in {self.place.name}'

class Excursion(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='excursion_image')
    num_of_people_now = models.PositiveIntegerField(default=0)
    max_num_of_people = models.PositiveIntegerField()
    date = models.DateTimeField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField(null=True)
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Excursion in {self.place.name}'

class Guide(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='guide_images', null=True, blank=True)
    excursion = models.ForeignKey(to=Excursion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Guide'
        verbose_name_plural = 'Guides'

    def __str__(self):
        return f'Guide {self.first_name} {self.last_name}'

class Hotels(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='hotels_image')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('0.01'))])
    phone = models.CharField(max_length=12)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return f'{self.name} in {self.place.Area.location}'

class Products(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    hotels = models.ForeignKey(to=Hotels, on_delete=models.CASCADE)
    events = models.ForeignKey(to=Events, on_delete=models.CASCADE)
    excursion = models.ForeignKey(to=Excursion, on_delete=models.CASCADE)
    area = models.ForeignKey(to=Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

    def __str__(self):
        if self.hotels.name != 'none':
            return f'{self.category.name}: {self.hotels.name}'
        elif self.excursion.name != 'none':
            return f'{self.category.name}: {self.excursion.name}'
        else:
            return f'{self.category.name}: {self.events.name}'

class Basket(models.Model) :
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Корзина товаров для {self.user.username}"

    def sum(self):
        if self.products.category == "Events":
            return self.products.events.price * self.quantity
        elif self.products.category == "Excursions":
            return self.products.excursion.price * self.quantity
        return self.products.hotels.price * self.quantity