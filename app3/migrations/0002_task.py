# Generated by Django 2.1.5 on 2019-02-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskpolygon', models.CharField(max_length=10000)),
                ('notes', models.CharField(max_length=30)),
            ],
        ),
    ]
