# Generated by Django 3.1 on 2020-08-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=60)),
                ('datail', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
