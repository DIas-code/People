# Generated by Django 4.2 on 2023-05-11 09:36

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=120, unique=True)),
                ('image', models.ImageField(upload_to='areas_image')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='events_image')),
                ('date', models.DateTimeField()),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='excursion_image')),
                ('num_of_people_now', models.PositiveIntegerField(default=0)),
                ('max_num_of_people', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('description', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('image', models.ImageField(blank=True, null=True, upload_to='guide_images')),
                ('charac', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Guide',
                'verbose_name_plural': 'Guides',
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='hotels_image')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('phone', models.CharField(max_length=12)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Hotels',
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.events')),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.excursion')),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotels')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.area')),
            ],
        ),
        migrations.AddField(
            model_name='hotels',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.place'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.guide'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.place'),
        ),
        migrations.AddField(
            model_name='events',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.place'),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
        ),
    ]
