
from django.db import models

class Question(models.Model):
    qid = models.BigIntegerField(primary_key=True)
    que = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cr_ans = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class Answers(models.Model):
    qid = models.BigIntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    ans1 = models.TextField(blank=True, null=True)
    ans2 = models.TextField(blank=True, null=True)
    ans3 = models.TextField(blank=True, null=True)
    ans4 = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class Answersheet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.TextField(blank=True, null=True)
    qid = models.BigIntegerField(blank=True, null=True)
    cr_ans = models.IntegerField(blank=True, null=True)
    ch_ans = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answersheet'


class Result(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.BigIntegerField(blank=True, null=True)
    alottime = models.IntegerField(blank=True, null=True)
    remtime = models.IntegerField(blank=True, null=True)
    submitstatus = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result'

class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    t_experience = models.IntegerField(blank=True, null=True)
    previous_org = models.CharField(max_length=100, blank=True, null=True)
    link = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Address(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    address3 = models.TextField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pa_address1 = models.TextField(blank=True, null=True)
    pa_address2 = models.TextField(blank=True, null=True)
    pa_address3 = models.TextField(blank=True, null=True)
    pa_pincode = models.IntegerField(blank=True, null=True)
    pa_country = models.CharField(max_length=100, blank=True, null=True)
    pa_state = models.CharField(max_length=100, blank=True, null=True)
    pa_city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Experience(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
    months = models.IntegerField(blank=True, null=True)
    from_date = models.IntegerField(blank=True, null=True)
    to_date = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experience'


class Qualifications(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    qualification_status = models.CharField(max_length=50, blank=True, null=True)
    university_name = models.TextField(blank=True, null=True)
    institute_name = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qualifications'



class Skills(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    skill_name = models.TextField(blank=True, null=True)
    skill_type = models.IntegerField(blank=True, null=True)
    skill_level = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'

