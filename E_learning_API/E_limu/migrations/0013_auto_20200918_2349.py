# Generated by Django 2.2.7 on 2020-09-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_limu', '0012_auto_20200918_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_types',
            field=models.CharField(max_length=100, verbose_name=1),
        ),
    ]
