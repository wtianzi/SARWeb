# Generated by Django 2.1.5 on 2019-05-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataStorage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskid', models.CharField(blank=True, max_length=100, null=True)),
                ('subtaskid', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GPSData',
            fields=[
                ('deviceid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('taskid', models.CharField(blank=True, max_length=100, null=True)),
                ('gpsdata', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskpolygon', models.TextField(blank=True, null=True)),
                ('notes', models.CharField(max_length=30)),
                ('taskid', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resourcetype', models.CharField(blank=True, max_length=100, null=True)),
                ('planningno', models.CharField(blank=True, max_length=100, null=True)),
                ('priority', models.CharField(blank=True, max_length=100, null=True)),
                ('task_complete', models.BooleanField(default=True)),
                ('task_partially_finished', models.BooleanField(default=True)),
                ('urgent_follow_up', models.BooleanField(default=True)),
                ('task_number', models.CharField(blank=True, default='0000', max_length=100)),
                ('team_identifier', models.CharField(blank=True, max_length=100, null=True)),
                ('resource_type', models.CharField(blank=True, max_length=100, null=True)),
                ('task_map', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('division_group', models.CharField(blank=True, max_length=100, null=True)),
                ('incident_name', models.CharField(blank=True, max_length=100, null=True)),
                ('task_instructions', models.TextField(blank=True, null=True)),
                ('previous_search', models.CharField(blank=True, max_length=1000, null=True)),
                ('transportation', models.CharField(blank=True, max_length=1000, null=True)),
                ('equipment_requirements', models.CharField(blank=True, max_length=1000, null=True)),
                ('expected_time_frame', models.BooleanField(default=True)),
                ('expected_time_frame_input', models.CharField(blank=True, max_length=100, null=True)),
                ('target_pod_subject', models.BooleanField(default=True)),
                ('target_pod_subject_input', models.CharField(blank=True, max_length=100, null=True)),
                ('target_pod_clues', models.BooleanField(default=True)),
                ('target_pod_clues_input', models.CharField(blank=True, max_length=100, null=True)),
                ('team_nearby', models.BooleanField(default=True)),
                ('team_nearby_input', models.CharField(blank=True, max_length=100, null=True)),
                ('applicable_clues', models.BooleanField(default=True)),
                ('terrain_hazrds', models.BooleanField(default=True)),
                ('weather_safety_issues', models.BooleanField(default=True)),
                ('press_family_plans', models.BooleanField(default=True)),
                ('subject_information', models.BooleanField(default=True)),
                ('rescue_find_plans', models.BooleanField(default=True)),
                ('others', models.BooleanField(default=True)),
                ('others_input', models.TextField(blank=True, null=True)),
                ('team_call_sign', models.CharField(blank=True, max_length=100, null=True)),
                ('freq_team', models.CharField(blank=True, max_length=100, null=True)),
                ('base_call_sign', models.CharField(blank=True, max_length=100, null=True)),
                ('freq_base', models.CharField(blank=True, max_length=100, null=True)),
                ('pertinent_phone_no', models.CharField(blank=True, max_length=100, null=True)),
                ('base', models.CharField(blank=True, max_length=100, null=True)),
                ('check_in_feq', models.CharField(blank=True, max_length=100, null=True)),
                ('check_in_hour', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_1_function', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_1_freq', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_1_comments', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_2_function', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_2_freq', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_2_comments', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_3_function', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_3_freq', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_3_comments', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_4_function', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_4_freq', models.CharField(blank=True, max_length=100, null=True)),
                ('tactical_4_comments', models.CharField(blank=True, max_length=100, null=True)),
                ('note_safety_message', models.TextField(blank=True, null=True)),
                ('prepared_by', models.CharField(blank=True, max_length=100, null=True)),
                ('briefed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
