# Generated by Django 3.0 on 2023-04-19 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articale', '0003_article_contant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='contant',
            new_name='content',
        ),
    ]
