# Generated by Django 2.0.1 on 2018-01-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='events'),
        ),
    ]
