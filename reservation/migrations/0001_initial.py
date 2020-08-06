# Generated by Django 3.1 on 2020-08-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstname', max_length=45, null=True)),
                ('familyname', models.CharField(blank=True, db_column='familyname', max_length=45, null=True)),
                ('dateofbirth', models.CharField(blank=True, db_column='dateofbirth', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='email', max_length=45, null=True)),
            ],
            options={
                'db_table': 'register',
                'managed': False,
            },
        ),
    ]