# Generated by Django 4.1.3 on 2022-12-05 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_project_urlfield_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='URLField',
            new_name='link',
        ),
    ]