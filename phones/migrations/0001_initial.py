# Generated by Django 4.2.5 on 2023-10-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]
