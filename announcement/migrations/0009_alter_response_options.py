# Generated by Django 4.2.1 on 2023-05-31 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0008_response_status_alter_response_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ('data',)},
        ),
    ]
