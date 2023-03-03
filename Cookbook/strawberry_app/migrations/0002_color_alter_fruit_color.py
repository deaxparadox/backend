# Generated by Django 4.1.5 on 2023-02-21 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strawberry_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='fruit',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='strawberry_app.color'),
        ),
    ]
