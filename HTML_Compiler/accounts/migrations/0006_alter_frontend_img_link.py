# Generated by Django 3.2.17 on 2023-03-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_frontend_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend',
            name='img_link',
            field=models.CharField(max_length=1000),
        ),
    ]
