# Generated by Django 3.1.2 on 2020-10-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_datafileone_datafiletwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafileone',
            name='time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='datafiletwo',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
