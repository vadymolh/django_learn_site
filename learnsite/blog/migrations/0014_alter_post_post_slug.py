# Generated by Django 4.1.4 on 2023-04-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(default='default_post', max_length=80),
        ),
    ]
