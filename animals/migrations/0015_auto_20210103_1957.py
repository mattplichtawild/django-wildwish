# Generated by Django 3.1.3 on 2021-01-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0014_auto_20210103_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='genus',
            field=models.CharField(max_length=72, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='species',
            field=models.CharField(max_length=72, null=True),
        ),
        migrations.AddField(
            model_name='species',
            name='sub_species',
            field=models.CharField(max_length=72, null=True),
        ),
    ]