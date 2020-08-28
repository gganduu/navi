# Generated by Django 3.1 on 2020-08-26 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_key',
            name='MK_key_type',
        ),
        migrations.RemoveField(
            model_name='match_key',
            name='MK_match',
        ),
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
        migrations.RemoveField(
            model_name='pattern_source',
            name='PS_pattern',
        ),
        migrations.RemoveField(
            model_name='pattern_source',
            name='PS_topology',
        ),
        migrations.DeleteModel(
            name='Key_Type',
        ),
        migrations.DeleteModel(
            name='Match_Key',
        ),
        migrations.DeleteModel(
            name='Match_Method_Type',
        ),
        migrations.DeleteModel(
            name='Matched',
        ),
        migrations.DeleteModel(
            name='Pattern',
        ),
        migrations.DeleteModel(
            name='Pattern_Source',
        ),
    ]