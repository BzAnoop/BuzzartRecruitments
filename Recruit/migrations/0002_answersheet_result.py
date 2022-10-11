# Generated by Django 4.1.1 on 2022-10-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answersheet',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('uid', models.BigIntegerField(blank=True, null=True)),
                ('qid', models.BigIntegerField(blank=True, null=True)),
                ('cr_ans', models.IntegerField(blank=True, null=True)),
                ('ch_ans', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'answersheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('uid', models.BigIntegerField(blank=True, null=True)),
                ('alottime', models.IntegerField(blank=True, null=True)),
                ('remtime', models.IntegerField(blank=True, null=True)),
                ('submitstatus', models.IntegerField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'result',
                'managed': False,
            },
        ),
    ]
