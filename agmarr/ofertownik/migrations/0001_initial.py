# Generated by Django 2.2.3 on 2020-12-01 14:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_of_images', models.TextField(blank=True, max_length=500)),
                ('name', models.TextField(blank=True, max_length=500)),
                ('price', models.TextField(blank=True, max_length=500)),
                ('rozmiar', models.CharField(blank=True, max_length=500)),
                ('material', models.TextField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofertownik.Offer')),
            ],
        ),
    ]
