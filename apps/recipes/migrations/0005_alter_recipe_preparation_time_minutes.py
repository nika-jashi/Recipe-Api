# Generated by Django 4.2.6 on 2023-11-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_minutes',
            field=models.PositiveIntegerField(),
        ),
    ]
