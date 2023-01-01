# Generated by Django 4.1.3 on 2022-11-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0002_remove_letter_delivered_alter_letter_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='sent',
        ),
        migrations.AlterField(
            model_name='letter',
            name='status',
            field=models.CharField(choices=[('PND', 'Pending'), ('SNT', 'Sent'), ('TRV', 'Traveling'), ('DLV', 'Deliered')], default='PND', max_length=3),
        ),
    ]
