# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0011_koha_ws_29sep2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koha_WS_12oct2018',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('college', models.CharField(max_length=500)),
                ('remote', models.CharField(max_length=500)),
                ('purpose', models.CharField(default=b'KMW', max_length=10)),
            ],
        ),
    ]
