# Generated by Django 2.0.5 on 2019-07-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190701_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
