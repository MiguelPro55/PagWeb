# Generated by Django 2.2.1 on 2019-05-22 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30, unique=True)),
                ('precio', models.IntegerField()),
                ('cpu', models.CharField(max_length=20)),
                ('os', models.CharField(max_length=20)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca')),
            ],
        ),
    ]
