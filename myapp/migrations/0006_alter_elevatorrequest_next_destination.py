# Generated by Django 4.2.3 on 2023-07-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_elevatorrequest_elevator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevatorrequest',
            name='next_destination',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]