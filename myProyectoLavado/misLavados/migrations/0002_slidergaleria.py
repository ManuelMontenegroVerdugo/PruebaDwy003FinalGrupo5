# Generated by Django 2.2.16 on 2020-10-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misLavados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderGaleria',
            fields=[
                ('ident1', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('image1', models.ImageField(null=True, upload_to='car')),
            ],
        ),
    ]
