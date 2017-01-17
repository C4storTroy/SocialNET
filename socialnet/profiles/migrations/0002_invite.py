# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invited', models.ForeignKey(related_name='received_invites', to='profiles.Profile')),
                ('requester', models.ForeignKey(related_name='done_invites', to='profiles.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
