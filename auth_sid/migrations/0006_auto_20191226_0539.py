# Generated by Django 3.0.1 on 2019-12-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_sid', '0005_auto_20191220_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]