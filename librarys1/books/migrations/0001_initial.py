# Generated by Django 5.1.1 on 2024-10-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('cover', models.ImageField(upload_to='cover')),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
    ]
