# Generated by Django 2.2.7 on 2020-09-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_limu', '0006_auto_20200918_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.CharField(max_length=100, verbose_name=(1, 2, 3)),
        ),
    ]
