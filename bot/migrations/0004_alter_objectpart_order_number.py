# Generated by Django 3.2.8 on 2021-10-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_alter_objectpart_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpart',
            name='order_number',
            field=models.IntegerField(verbose_name='порядковый номер'),
        ),
    ]