# Generated by Django 4.1.2 on 2022-10-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категориb'},
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
    ]
