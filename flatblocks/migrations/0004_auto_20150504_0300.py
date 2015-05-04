# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatblocks', '0003_auto_20150504_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatblock',
            name='slug',
            field=models.CharField(help_text='A unique name used for reference in the templates', unique=True, max_length=255, verbose_name='Slug'),
        ),
    ]
