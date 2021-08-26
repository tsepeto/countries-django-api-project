# Generated by Django 3.2.6 on 2021-08-25 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='region',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rootapp.country', verbose_name='Countries'),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
