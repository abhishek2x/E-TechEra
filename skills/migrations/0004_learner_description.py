# Generated by Django 3.0.7 on 2020-06-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20200614_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]