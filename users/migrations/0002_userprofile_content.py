# Generated by Django 2.2 on 2021-01-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
