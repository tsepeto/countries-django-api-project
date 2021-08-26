# Generated by Django 3.2.6 on 2021-08-24 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=11)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=11)),
                ('type', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rootapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=11)),
                ('type', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rootapp.region')),
            ],
        ),
    ]