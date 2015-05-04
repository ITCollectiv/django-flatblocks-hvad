# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatblocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatBlockTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='Content', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'flatblocks_flatblock_translation',
                'db_tablespace': '',
            },
        ),
        migrations.RemoveField(
            model_name='flatblock',
            name='content',
        ),
        migrations.AddField(
            model_name='flatblocktranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', editable=False, to='flatblocks.FlatBlock', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='flatblocktranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
