# Generated by Django 2.2.7 on 2020-09-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_limu', '0010_remove_choice_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice',
            field=models.CharField(default='a', max_length=100, verbose_name=1),
            preserve_default=False,
        ),
    ]
