# Generated by Django 3.1.3 on 2020-11-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20201123_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wish',
            name='fund_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]