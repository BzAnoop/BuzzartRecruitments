from dataclasses import fields
from plistlib import UID
from django.contrib import admin

# Register your models here.
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('uid','first_name','last_name','mobile','email','password','dob','status','Total_Experience','Previous_Organization','link','UI_Developer','Python_Developer','Full_Stack_Developer','ijp_app','result')
    fields=['uid','first_name','last_name','mobile','email','password','dob','status','Total_Experience','Previous_Organization','link','UI_Developer','Python_Developer','Full_Stack_Developer','ijp_app','result']

    def Total_Experience(self, obj):
        return obj.t_experience

    def Previous_Organization(self, obj):
        return obj.previous_org
    
    def UI_Developer(self,obj):
        return obj.ui_app

    def Python_Developer(self,obj):
        return obj.python_app

    def Full_Stack_Developer(self,obj):
        return obj.fs_app

admin.site.register(Users, UsersAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=('uid','address1','address2','address3','pincode','country','state','city','pa_address1','pa_address2','pa_address3','pa_pincode','pa_country','pa_state','pa_city','status')
    fields=['uid','address1','address2','address3','pincode','country','state','city','pa_address1','pa_address2','pa_address3','pa_pincode','pa_country','pa_state','pa_city','status']

admin.site.register(Address, AddressAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display=('uid','title','company','years','months','from_date','to_date','status')
    fields=['uid','title','company','years','months','from_date','to_date','status']

admin.site.register(Experience, ExperienceAdmin)



class QualificationsAdmin(admin.ModelAdmin):
    list_display=('uid','qualification','qualification_status','university_name','institute_name','from_date','to_date','percentage','grade','year','status')
    fields=['uid','qualification','qualification_status','university_name','institute_name','from_date','to_date','percentage','grade','year','status']

admin.site.register(Qualifications, QualificationsAdmin)


class SkillsAdmin(admin.ModelAdmin):
    list_display=('uid','skill_name','skill_type','skill_level','status')
    fields= ['uid','skill_name','skill_type','skill_level','status']
    
admin.site.register(Skills, SkillsAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display=('qid','que','subject','level','status','cr_ans')
    fields=['qid','que','subject','level','status','cr_ans']

admin.site.register(Question, QuestionAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display=('qid','id','ans1','ans2','ans3','ans4','status')
    fields=['qid','id','ans1','ans2','ans3','ans4','status']

admin.site.register(Answers, AnswersAdmin)

class AnswersheetAdmin(admin.ModelAdmin):
    list_display=('uid','qid','cr_ans','ch_ans')
    fields=['uid','qid','cr_ans','ch_ans']
    
admin.site.register(Answersheet, AnswersheetAdmin)

class ApprovalAdmin(admin.ModelAdmin):
    your_choices = (
        ('UI', u'UI Developer'),
        ('Python', u'Python Developer'),
        ('FS', u'Full Stack Developer'),
        ('IJP', u'Internal Job Posting'),
    )

    app_sub = models.CharField(max_length=32, choices=your_choices, null=True, blank=True)
    list_display=('uid','app_sub','alottime','remtime','submit_st','marks','result')
    fields=['uid','app_sub','alottime','remtime','submit_st','marks','result']


admin.site.register(Approval, ApprovalAdmin)
