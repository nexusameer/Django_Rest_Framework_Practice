# Generated by Django 5.0.6 on 2024-06-24 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Category',
            new_name='category',
        ),
    ]
