# Generated by Django 3.1.3 on 2020-11-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('word', models.CharField(max_length=100)),
                ('freq', models.IntegerField()),
            ],
        ),
    ]
