# Generated by Django 3.1.3 on 2021-01-07 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0022_auto_20210106_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speciesgroup',
            options={'verbose_name': 'Species Group'},
        ),
        migrations.AddField(
            model_name='toy',
            name='ship_cost',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Leave blank if unknown.', max_digits=6, null=True),
        ),
    ]
