# Generated by Django 2.2 on 2019-05-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_celular_idpaypalcarrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=10, unique=True)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]