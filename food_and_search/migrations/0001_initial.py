# Generated by Django 2.0.5 on 2018-05-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('link_http', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('saturated_fat_100g', models.IntegerField(max_length=4)),
                ('carbohydrates_100g', models.IntegerField(max_length=4)),
                ('energy_100g', models.IntegerField(max_length=4)),
                ('sugars_100g', models.IntegerField(max_length=4)),
                ('sodium_100g', models.IntegerField(max_length=4)),
                ('categories', models.ManyToManyField(to='food_and_search.Categories')),
            ],
        ),
    ]