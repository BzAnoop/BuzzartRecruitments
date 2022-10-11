from django.urls import path
from . import views
from .views import proceedtest

urlpatterns = [
    path('',views.home, name ="home"),
    path('register',views.registration, name='register'),
    path('log',views.signin, name='log'),
    path('testhome',views.test_home, name='testhome'),
    path('testrule/<str:skill>',views.test_rule, name='testrule'),
    path('userlogout',views.userlogout, name='userlogout'),
    path('starttest/<str:skill>',views.start_test,name='starttest'),
    path('proceed_test',views.proceedtest,name='proceed_test'),
    # path('proceed_test',proceedtest.as_view(),name='proceed_test'),
    path('tracerec',views.trace_rec, name='tracerec'),
    path('adminboard',views.admin_board, name='adminboard'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('logoutadmin',views.adminLogout, name='logoutadmin'),
    path('applicant_view',views.applicantview,name='applicant_view'),
    path('testResults',views.test_Results,name='testResults'),
    path('addquali',views.add_quali, name='addquali'),
    path('addExp',views.add_Exp, name='addExp'),
    path('addskills',views.add_skills, name = 'addskills'),
    path('approve',views.approvals, name ='approve'),
]