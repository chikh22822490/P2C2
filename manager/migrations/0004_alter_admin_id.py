# Generated by Django 4.0.2 on 2022-03-15 23:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f0052022-f39c-4478-8edd-1ea9fd83e34c'), primary_key=True, serialize=False),
        ),
    ]
