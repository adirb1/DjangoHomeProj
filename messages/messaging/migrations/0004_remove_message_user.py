# Generated by Django 3.2.6 on 2021-10-06 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
