# Generated by Django 3.1.3 on 2020-11-24 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoos', '0001_initial'),
        ('images', '0001_initial'),
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('images', models.ManyToManyField(to='images.Image')),
            ],
            options={
                'db_table': 'toys',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='images',
            field=models.ManyToManyField(to='images.Image'),
        ),
        migrations.AddField(
            model_name='animal',
            name='zoo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='zoos.zoo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='zoo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='zoos.zoo'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='bio',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.CharField(max_length=72),
        ),
        migrations.AlterField(
            model_name='animal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='animals.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=72),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterModelTable(
            name='animal',
            table='animals',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
                ('images', models.ManyToManyField(to='images.Image')),
                ('toy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.toy')),
            ],
            options={
                'verbose_name_plural': 'Wishes',
                'db_table': 'wishes',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_first_name', models.CharField(max_length=72)),
                ('donor_last_name', models.CharField(max_length=72)),
                ('donor_email', models.EmailField(max_length=72)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.user')),
                ('wish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.wish')),
            ],
            options={
                'db_table': 'donations',
            },
        ),
    ]
