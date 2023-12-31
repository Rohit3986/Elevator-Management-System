# Generated by Django 4.2.3 on 2023-07-20 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_elevator_request_elevatorrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevator',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='elevator_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elevators', to='myapp.elevatorsystem'),
        ),
        migrations.AlterField(
            model_name='elevatorrequest',
            name='elevator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elevator_logs', to='myapp.elevatorsystem'),
        ),
    ]
