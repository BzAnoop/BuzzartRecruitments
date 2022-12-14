# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


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
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    qid = models.BigIntegerField(blank=True, null=True)
    cr_ans = models.IntegerField(blank=True, null=True)
    ch_ans = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answersheet'


class Approval(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    app_sub = models.CharField(max_length=20, blank=True, null=True)
    alottime = models.IntegerField(blank=True, null=True)
    remtime = models.IntegerField(blank=True, null=True)
    submit_st = models.CharField(max_length=20, blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experience(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
    months = models.IntegerField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

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
    status = models.CharField(max_length=20, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'qualifications'


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


class Skills(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    skill_name = models.TextField(blank=True, null=True)
    skill_type = models.IntegerField(blank=True, null=True)
    skill_level = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'skills'


class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default='New', blank=True, null=True)
    t_experience = models.BigIntegerField(blank=True, null=True)
    previous_org = models.CharField(max_length=100, blank=True, null=True)
    link = models.IntegerField(blank=True, null=True)
    ui_app = models.IntegerField(blank=True, null=True)
    python_app = models.IntegerField(blank=True, null=True)
    fs_app = models.IntegerField(blank=True, null=True)
    ijp_app = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
