from django import forms
from django.forms import ModelForm
from .models import TaskAssignment,QuestionnaireModel,ParticipantStatusModel,DemographicsModel,PostExpSurveyModel

class DemoForm(forms.Form):
    resourcetype=forms.CharField(label='Resource type',max_length=100)
    planningno=forms.CharField(label='Planning #',max_length=100)
    priority=forms.CharField(label='Priority',max_length=100)
    def save_to_db(self):
        # send email using the self.cleaned_data dictionary
        pass

class TaskAssignmentForm(ModelForm):

    class Meta:
        model = TaskAssignment
        fields = '__all__'
        #exclude = ['id','created_at','updated_at']
        #fields=["resourcetype","planningno","priority"]
        #fields = '__all__'

class QuestionnaireForm(ModelForm):
    class Meta:
        model = QuestionnaireModel
        fields = '__all__'

class ConsentForm(ModelForm):
    class Meta:
        model = ParticipantStatusModel
        fields = '__all__'

class DemographicsForm(ModelForm):
    class Meta:
        model = DemographicsModel
        fields = '__all__'

class PostExpSurveyForm(ModelForm):
    class Meta:
        model = PostExpSurveyModel
        fields = '__all__'
        