# Generated by Django 3.0.3 on 2020-03-11 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinglineitem',
            old_name='order',
            new_name='booking',
        ),
    ]