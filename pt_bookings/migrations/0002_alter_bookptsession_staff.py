# Generated by Django 3.2 on 2022-04-09 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookptsession',
            name='staff',
            field=models.CharField(choices=[('Karen', 'Karen')], default='karen', max_length=15),
        ),
    ]