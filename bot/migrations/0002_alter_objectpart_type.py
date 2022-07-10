# Generated by Django 3.2.8 on 2021-10-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpart',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Text'), (2, 'Image'), (3, 'Video'), (4, 'Pause'), (5, 'Button'), (6, 'Formtext'), (7, 'Formorder')], verbose_name='тип'),
        ),
    ]