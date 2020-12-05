# Generated by Django 2.2.3 on 2020-12-01 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertownik', '0003_auto_20201201_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ofertownik.Offer'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ofertownik.Product'),
        ),
    ]
