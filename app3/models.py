from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskpolygon = models.TextField(blank=True,null=True)
    notes = models.CharField(max_length=30)
    taskid = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.notes

class GPSData(models.Model):
    #id = models.AutoField(primary_key=True)
    deviceid = models.CharField(max_length=20,primary_key=True)
    taskid = models.CharField(max_length=100,blank=True,null=True)
    gpsdata = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    def __str__(self):
        return self.gpsdata

class DataStorage(models.Model):
    id = models.AutoField(primary_key=True)
    taskid = models.CharField(max_length=100,blank=True,null=True)
    subtaskid = models.CharField(max_length=100,blank=True,null=True)
    data = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    def __str__(self):
        return self.data


class TaskAssignment(models.Model):
    id = models.AutoField(primary_key=True)
    resourcetype=models.CharField(max_length=100, blank=True, null=True)
    planningno=models.CharField(max_length=100, blank=True,null=True)
    priority=models.CharField(max_length=100, blank=True,null=True)

    task_complete=models.BooleanField(default=True)
    task_partially_finished=models.BooleanField(default=True)
    urgent_follow_up=models.BooleanField(default=True)

    task_number=models.CharField(max_length=100,blank=True,  default="0000")
    team_identifier=models.CharField(max_length=100, blank=True,null=True)
    resource_type=models.CharField(max_length=100, blank=True,null=True)
    task_map=models.CharField(max_length=100, blank=True,null=True)

    branch=models.CharField(max_length=100, blank=True,null=True)
    division_group=models.CharField(max_length=100, blank=True,null=True)
    incident_name=models.CharField(max_length=100, blank=True,null=True)

    task_instructions=models.TextField( blank=True,null=True)
    previous_search=models.CharField(max_length=1000, blank=True,null=True)
    transportation=models.CharField(max_length=1000, blank=True,null=True)
    equipment_requirements=models.CharField(max_length=1000, blank=True,null=True)

    expected_time_frame=models.BooleanField(default=True)
    expected_time_frame_input=models.CharField(max_length=100, blank=True,null=True)
    target_pod_subject=models.BooleanField(default=True)
    target_pod_subject_input=models.CharField(max_length=100, blank=True,null=True)

    target_pod_clues=models.BooleanField(default=True)
    target_pod_clues_input=models.CharField(max_length=100, blank=True,null=True)
    team_nearby=models.BooleanField(default=True)
    team_nearby_input=models.CharField(max_length=100, blank=True,null=True)

    applicable_clues=models.BooleanField(default=True)
    terrain_hazrds=models.BooleanField(default=True)
    weather_safety_issues=models.BooleanField(default=True)
    press_family_plans=models.BooleanField(default=True)
    subject_information=models.BooleanField(default=True)
    rescue_find_plans=models.BooleanField(default=True)
    others=models.BooleanField(default=True)
    others_input=models.TextField(blank=True,null=True)

    team_call_sign=models.CharField(max_length=100, blank=True,null=True)
    freq_team=models.CharField(max_length=100, blank=True,null=True)
    base_call_sign=models.CharField(max_length=100, blank=True,null=True)
    freq_base=models.CharField(max_length=100, blank=True,null=True)
    pertinent_phone_no=models.CharField(max_length=100, blank=True,null=True)
    base=models.CharField(max_length=100, blank=True,null=True)
    check_in_feq=models.CharField(max_length=100, blank=True,null=True)
    check_in_hour=models.CharField(max_length=100, blank=True,null=True)

    tactical_1_function=models.CharField(max_length=100, blank=True,null=True)
    tactical_1_freq=models.CharField(max_length=100, blank=True,null=True)
    tactical_1_comments=models.CharField(max_length=100, blank=True,null=True)

    tactical_2_function=models.CharField(max_length=100, blank=True,null=True)
    tactical_2_freq=models.CharField(max_length=100, blank=True,null=True)
    tactical_2_comments=models.CharField(max_length=100, blank=True,null=True)

    tactical_3_function=models.CharField(max_length=100, blank=True,null=True)
    tactical_3_freq=models.CharField(max_length=100, blank=True,null=True)
    tactical_3_comments=models.CharField(max_length=100, blank=True,null=True)

    tactical_4_function=models.CharField(max_length=100, blank=True,null=True)
    tactical_4_freq=models.CharField(max_length=100, blank=True,null=True)
    tactical_4_comments=models.CharField(max_length=100, blank=True,null=True)

    note_safety_message=models.TextField( blank=True,null=True)
    prepared_by=models.CharField(max_length=100, blank=True,null=True)
    briefed_by=models.CharField(max_length=100, blank=True,null=True)
    time_out=models.CharField(max_length=100, blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.resourcetype
