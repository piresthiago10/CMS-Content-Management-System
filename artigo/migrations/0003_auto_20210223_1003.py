# Generated by Django 3.1.7 on 2021-02-23 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigo', '0002_auto_20210222_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='data_criacao',
            field=models.CharField(default=datetime.date(2021, 2, 23), editable=False, max_length=10),
        ),
    ]