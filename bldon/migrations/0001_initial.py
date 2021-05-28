# Generated by Django 3.1.4 on 2020-12-07 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('gender', models.CharField(max_length=10)),
                ('last_donate', models.DateField()),
                ('password', models.CharField(default='123', max_length=100)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bldon.bloodgroup')),
            ],
            options={
                'managed': True,
            },
        ),
    ]