# Generated by Django 3.1.5 on 2021-01-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210123_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_review',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default=0, max_length=100),
        ),
    ]