# Generated by Django 3.1.3 on 2021-03-08 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_title'),
        ('animals', '0026_auto_20210127_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.vendor'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='images',
            field=models.ManyToManyField(blank=True, to='images.Image'),
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]