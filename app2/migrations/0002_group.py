# Generated by Django 2.1.5 on 2019-01-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.CharField(max_length=30)),
                ('member1', models.CharField(max_length=30)),
                ('member2', models.CharField(max_length=30)),
                ('member3', models.CharField(max_length=30)),
                ('member4', models.CharField(max_length=30)),
                ('member5', models.CharField(max_length=30)),
                ('member6', models.CharField(max_length=30)),
                ('member7', models.CharField(max_length=30)),
                ('member8', models.CharField(max_length=30)),
                ('member9', models.CharField(max_length=30)),
                ('member10', models.CharField(max_length=30)),
                ('member11', models.CharField(max_length=30)),
                ('member12', models.CharField(max_length=30)),
                ('member13', models.CharField(max_length=30)),
                ('member14', models.CharField(max_length=30)),
                ('member15', models.CharField(max_length=30)),
                ('member16', models.CharField(max_length=30)),
                ('member17', models.CharField(max_length=30)),
                ('member18', models.CharField(max_length=30)),
                ('member19', models.CharField(max_length=30)),
                ('member20', models.CharField(max_length=30)),
                ('other_members', models.CharField(max_length=30)),
            ],
        ),
    ]
