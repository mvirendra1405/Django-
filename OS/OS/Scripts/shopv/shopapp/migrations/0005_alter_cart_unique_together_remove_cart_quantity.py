# Generated by Django 5.0.7 on 2024-09-02 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_cart_quantity_alter_cart_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
