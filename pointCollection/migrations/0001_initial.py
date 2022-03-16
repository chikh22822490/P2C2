# Generated by Django 3.2.7 on 2022-03-16 01:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0006_alter_admin_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointCollection',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e8d1ff90-e62b-4f37-9857-fda3e55f81ff'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('adresse', models.CharField(blank=True, max_length=25, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.admin')),
            ],
        ),
    ]