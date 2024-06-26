# Generated by Django 4.2.10 on 2024-04-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('partition_key', models.CharField(editable=False, max_length=64)),
            ],
            options={
                'db_table': 'guest',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
