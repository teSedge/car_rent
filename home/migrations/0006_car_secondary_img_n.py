# Generated by Django 4.0.3 on 2022-06-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_car_secondary_img_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_secondary_img',
            name='N',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
