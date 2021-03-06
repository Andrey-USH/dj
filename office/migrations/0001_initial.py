# Generated by Django 3.0.7 on 2020-06-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('dateOfBirth', models.DateField(verbose_name='Дата рождения')),
                ('startDateWork', models.DateField(blank=True, verbose_name='дата начала работы')),
                ('photo', models.ImageField(upload_to='photo/')),
            ],
        ),
    ]
