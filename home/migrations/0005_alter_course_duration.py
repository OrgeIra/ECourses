# Generated by Django 5.1.6 on 2025-03-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
