# Generated by Django 3.2.17 on 2023-03-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_frontend'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]