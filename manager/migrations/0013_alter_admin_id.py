# Generated by Django 3.2.7 on 2022-03-16 02:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a496fc26-8250-4ad9-a040-d4d98404f734'), primary_key=True, serialize=False),
        ),
    ]
