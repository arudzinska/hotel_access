# Generated by Django 2.0.5 on 2018-05-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_rule_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='free_per_stay',
            field=models.PositiveIntegerField(null=True),
        ),
    ]