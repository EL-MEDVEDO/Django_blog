# Generated by Django 4.1.4 on 2022-12-30 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_feedback_rating_alter_feedback_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
