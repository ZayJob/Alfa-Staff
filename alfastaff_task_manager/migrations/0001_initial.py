# Generated by Django 3.0.7 on 2020-09-30 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alfastaff_shedule', '0003_scheduleforoneday_holiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15, null=True, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('priority', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'red'), (2, 'yellow'), (3, 'green')], null=True, verbose_name='Приеоритет')),
                ('status', models.CharField(blank=True, choices=[('Преложенно', 'Преложенно'), ('К работе', 'К работе'), ('В процессе', 'В процессе'), ('Готово', 'Готово')], max_length=15, null=True, verbose_name='Статус')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alfastaff_shedule.ScheduleForOneDay', verbose_name='День')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['day'],
            },
        ),
    ]
