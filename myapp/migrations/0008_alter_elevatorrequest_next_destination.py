# Generated by Django 4.2.3 on 2023-07-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_elevatorrequest_next_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevatorrequest',
            name='next_destination',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
