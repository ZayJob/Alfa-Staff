# Generated by Django 3.0.7 on 2020-07-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_bonuses', '0023_auto_20200722_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuscard',
            name='image',
            field=models.ImageField(blank=True, default='images/bonuses/incognita.png', null=True, upload_to='bonuses', verbose_name='Фотография'),
        ),
    ]
