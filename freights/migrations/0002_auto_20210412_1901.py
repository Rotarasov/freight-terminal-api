# Generated by Django 3.1.7 on 2021-04-12 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20210328_1816'),
        ('freights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='prefix',
        ),
        migrations.AlterField(
            model_name='device',
            name='prefix',
            field=models.CharField(choices=[('G', 'Giga'), ('M', 'Mega'), ('K', 'Kilo'), ('C', 'Centi'), ('m', 'Milli'), ('micro', 'Micro'), ('n', 'Nano')], max_length=30, null=True, verbose_name='prefix'),
        ),
        migrations.AlterField(
            model_name='freight',
            name='transfer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.transfer'),
        ),
    ]
