# Generated by Django 5.1 on 2024-09-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_ticket_number_of_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number_of_ticket',
            field=models.PositiveIntegerField(),
        ),
    ]
