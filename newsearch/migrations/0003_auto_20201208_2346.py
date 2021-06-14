# Generated by Django 3.1.3 on 2020-12-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0002_auto_20201112_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='about',
            field=models.CharField(default='Lorem ipsum', max_length=5000),
        ),
        migrations.AddField(
            model_name='hospital',
            name='direction_url',
            field=models.CharField(default='www.google.com', max_length=250),
        ),
        migrations.AddField(
            model_name='hospital',
            name='image_url',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYlm9vhkUbpK0HCU53rdbzsFSSYNpLDgPPpQ&usqp=CAU', max_length=250),
        ),
    ]