# Generated by Django 3.2.7 on 2022-03-16 02:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pointCollection', '0002_alter_pointcollection_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointcollection',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5d714bcf-1e5e-441a-b5e9-156ca1d86b6d'), primary_key=True, serialize=False, unique=True),
        ),
    ]
