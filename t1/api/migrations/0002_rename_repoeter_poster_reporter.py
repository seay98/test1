# Generated by Django 3.2.12 on 2022-02-12 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poster',
            old_name='repoeter',
            new_name='reporter',
        ),
    ]