# Generated by Django 2.2.3 on 2020-12-01 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertownik', '0002_auto_20201201_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='list_of_images',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofertownik.Product')),
            ],
        ),
    ]
