# Generated by Django 4.2.7 on 2023-12-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
