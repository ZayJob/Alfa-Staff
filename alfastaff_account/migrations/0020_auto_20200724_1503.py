# Generated by Django 3.0.7 on 2020-07-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_account', '0019_auto_20200722_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_binary',
            field=models.BinaryField(blank=True, verbose_name='Фотография байткод'),
        ),
    ]