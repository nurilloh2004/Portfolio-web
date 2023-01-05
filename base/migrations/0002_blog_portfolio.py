# Generated by Django 4.1.3 on 2023-01-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.FileField(upload_to='media/blog')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='media/portfolio')),
                ('link1', models.CharField(max_length=500)),
                ('link2', models.CharField(max_length=500)),
                ('link3', models.CharField(max_length=500)),
            ],
        ),
    ]
