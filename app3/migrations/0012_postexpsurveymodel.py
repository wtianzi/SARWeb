# Generated by Django 3.1.2 on 2020-10-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0011_demographicsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostExpSurveyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('participantid', models.CharField(blank=True, max_length=100, null=True)),
                ('q1', models.TextField(blank=True, null=True)),
                ('q2', models.TextField(blank=True, max_length=100, null=True)),
                ('q3', models.TextField(blank=True, max_length=100, null=True)),
                ('q4', models.TextField(blank=True, null=True)),
                ('q5', models.TextField(blank=True, null=True)),
                ('q6', models.TextField(blank=True, null=True)),
                ('q7', models.TextField(blank=True, null=True)),
                ('q8', models.TextField(blank=True, null=True)),
                ('q9', models.TextField(blank=True, null=True)),
                ('q10', models.TextField(blank=True, null=True)),
                ('q11', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
