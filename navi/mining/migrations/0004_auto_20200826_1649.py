# Generated by Django 3.1 on 2020-08-26 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0003_match_method_type_matched_pattern'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matched',
            name='MAT_match_method_type',
        ),
        migrations.RemoveField(
            model_name='matched',
            name='MAT_pattern',
        ),
        migrations.RemoveField(
            model_name='matched',
            name='MAT_topology',
        ),
        migrations.DeleteModel(
            name='Match_Method_Type',
        ),
        migrations.DeleteModel(
            name='Matched',
        ),
    ]
