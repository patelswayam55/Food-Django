# Generated by Django 5.0.3 on 2024-05-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_tablebooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebooking',
            name='number_of_people',
            field=models.IntegerField(),
        ),
    ]
