# Generated by Django 3.1.5 on 2021-01-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20210123_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_review',
            name='rating',
            field=models.CharField(choices=[('11111', '5'), ('1111', '4'), ('111', '3'), ('11', '2'), ('1', '1')], default=0, max_length=10),
        ),
    ]
