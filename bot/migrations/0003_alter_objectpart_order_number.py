# Generated by Django 3.2.8 on 2021-10-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_objectpart_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpart',
            name='order_number',
            field=models.IntegerField(unique=True, verbose_name='порядковый номер'),
        ),
    ]