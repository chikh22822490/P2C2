# Generated by Django 3.2.7 on 2022-03-16 02:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ab28cc70-2a83-4e5b-9c4e-50b5457391d1'), primary_key=True, serialize=False),
        ),
    ]
