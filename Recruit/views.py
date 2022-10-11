from multiprocessing import context
from time import sleep
from urllib import request
from django.shortcuts import render, redirect
from .models import *
from .forms  import *
from random import *
import mysql.connector
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.cache import never_cache

#Libraries for Formatted E-Mail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.views.generic import ListView
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#Unused Libraries
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from pynput.mouse import Listener

# Create your views here.
rand_ques =[]
tot_marks=0
#Answer will be saved here and tracked 
def trace_rec(req):
    global tot_marks
    global rand_ques
    req.session['last_activity'] = datetime.datetime.now().second
    time_taken = datetime.datetime.now() - req.session.get('b_time')

    # if time_taken.seconds <= 1800:
    #     time_left = 1800 - time_taken
    #     return render(req,'test_paper.html',{'page_obj':cont,'page_no':page_no,'time_left':time_left})
    # else:
    #     User_login = True
    #     return render(req,'home.html', {'msg':'Test Session Expired', 'userlogin':User_login})    
    if time_taken.seconds <= 1800:
        if req.session.has_key('UserID'):
            User_login = True
            usrid = req.session.get('UserID')
            q_id = req.POST['quesId']
            ans = req.POST['answer']
            
            # buz_con = mysql.connector.connect(host='localhost', user='root', password = 'root',database ='buzzart_req')
            # buz_cur = buz_con.cursor()
            # buz_cur.execute("select uid, u.qid, u.cr_ans, u.ch_ans, que, subject, level, ans1, ans2, ans3, ans4 from answersheet as u left join (select q.qid, q.que, subject, level, ans1, ans2, ans3, ans4 from question as q join answers as a on q.qid = a.qid) as qu on qu.qid = u.qid")
            # rand_ques = list(buz_cur.fetchall())
            # buz_con.close()
            # buz_cur.close()
            
            # rec = Answersheet.objects.filter(uid = usrid, qid = q_id)
            # rec[0].ch_ans = int(ans)
            # print("Name :",rec[0].uid,"\nQueston id :",rec[0].qid)
            # rec[0].save()

            rec = Answersheet.objects.get(uid=usrid,qid=q_id)
            rec.ch_ans = int(ans)
            if rec.cr_ans == int(ans):
                tot_marks+=5
            rec.save()

            # buz_con = mysql.connector.connect(host='localhost', user='root', password = 'root',database ='buzzart_req')
            # buz_cur = buz_con.cursor()
            # val = (ans,usrid,q_id)
            # buz_cur.execute("update answersheet set ch_ans = %s where uid = %s and qid = %s",val)
            # buz_con.commit()
            # buz_con.close()
            # buz_cur.close()

            subm = req.POST['sub']
            if subm=='Top':
                req.session['page_no'] = 0
                rec = Users.objects.get(uid=usrid)
                skill = req.session.get('skill')
                rec1 = rec.approval_set.get(app_sub=skill)
                rec1.marks = tot_marks
                rec1.save()
                rec.save()
            elif subm=='Previous':
                req.session['page_no'] = int(req.session.get('page_no')) - 1
                rec = Users.objects.get(uid=usrid)
                skill = req.session.get('skill')
                rec1 = rec.approval_set.get(app_sub=skill)
                rec1.marks = tot_marks
                rec1.save()
                rec.save()
            elif subm=='Next':
                print("Selected Answer",ans)
                req.session['page_no'] = int(req.session.get('page_no')) + 1
                rec = Users.objects.get(uid=usrid)
                skill = req.session.get('skill')
                rec1 = rec.approval_set.get(app_sub=skill)
                rec1.marks = tot_marks
                rec1.save()
                rec.save()
            elif subm=='Last':
                req.session['page_no'] = len(rand_ques)-1
                rec = Users.objects.get(uid=usrid)
                skill = req.session.get('skill')
                rec1 = rec.approval_set.get(app_sub=skill)
                rec1.marks = tot_marks
                rec1.save()
                rec.save()
            else:
                rec = Users.objects.get(uid=usrid)
                skill = req.session.get('skill')
                if skill=='FS':
                    rec.fs_app = 0
                if skill=='UI':
                    rec.ui_app = 0
                if skill=='Python':
                    rec.python_app = 0
                if skill=='IJP':
                    rec.ijp_app = 0
                
                rec1 = rec.approval_set.get(app_sub=skill)
                rec1.submit_st = "Submitted"
                rec1.marks = tot_marks
                
                if tot_marks >= 60:
                    rec1.result = "Cleared"
                rec1.save()
                rec.save()
                
                rec = Users.objects.get(uid=usrid)
                recs = rec.approval_set.exclude(submit_st='Submitted')
                return render(req,"test_home.html",{'uid':usrid, 'userlogin':User_login, 'skills':recs})            
            return HttpResponseRedirect('/proceed_test')
        else:
            rec = Users.objects.get(uid=usrid)
            skill = req.session.get('skill')
            if skill=='FS':
                rec.fs_app = 0
            if skill=='UI':
                rec.ui_app = 0
            if skill=='Python':
                rec.python_app = 0
            if skill=='IJP':
                rec.ijp_app = 0
            
            rec1 = rec.approval_set.get(app_sub=skill)
            rec1.submit_st = "Submitted"
            rec1.marks = tot_marks
            
            if tot_marks >= 60:
                rec1.result = "Cleared"
            rec1.save()
            rec.save()
            
            rec = Users.objects.get(uid=usrid)
            recs = rec.approval_set.exclude(submit_st='Submitted')
            return render(req,"test_home.html",{'uid':usrid, 'userlogin':User_login, 'skills':recs})
    else:
        User_login = False        
        return render(req,'home.html', {'msg':'You are not Logged in', 'userlogin':User_login})

#Test Will Begin from here    
def proceedtest(req):
    req.session['last_activity'] = datetime.datetime.now().second
    # d_time = datetime.datetime.now() - req.session.get('c_time')
    
    if req.session.has_key('UserID'):
        User_login = True
        page_no = int(req.session.get('page_no'))
        cont = rand_ques[page_no]
        return render(req,'test_paper.html',{'page_obj':cont,'page_no':page_no})
    else:
        User_login = False        
        return render(req,'home.html', {'msg':'You are not Logged in', 'userlogin':User_login})

#Start Test 
@never_cache
def start_test(req, skill):
    req.session['last_activity'] = datetime.datetime.now().second
    global rand_ques
    global tot_marks

    if req.session.has_key('UserID'):
        query = ''
        usrid = req.session.get('UserID')
        rec = Users.objects.get(uid=usrid)
        User_login = True
        if skill =='UI':
            if rec.ui_app != 1:
                return render(req,'home.html', {'uid':usrid, 'msg':'You are not allowed to visit that link', 'userlogin':User_login})
        elif skill == 'FS':
            if rec.fs_app != 1:
                return render(req,'home.html', {'uid':usrid, 'msg':'You are not allowed to visit that link', 'userlogin':User_login})
        elif skill == 'Python':
            if rec.python_app != 1:
                return render(req,'home.html', {'uid':usrid, 'msg':'You are not allowed to visit that link', 'userlogin':User_login})
        elif skill == 'IJP':
            if rec.ijp_app != 1:
                return render(req,'home.html', {'uid':usrid, 'msg':'You are not allowed to visit that link', 'userlogin':User_login})

        buz_con = mysql.connector.connect(host='localhost', user='root', password = 'root',database ='buzzart_req')
        buz_cur = buz_con.cursor()
        if skill == "UI":
            query = "select qid, que, level, cr_ans, subject from question where subject = 'HTML' or subject = 'CSS' or subject ='JS'"
        elif skill == "Python":
            query = "select qid, que, level, cr_ans, subject from question where subject = 'PYTHON' or subject = 'Django'"
        elif skill == "FS":
            query = "select qid, que, level, cr_ans, subject from question where subject = 'HTML' or subject = 'CSS' or subject ='JS' or subject ='reactjs' or subject = 'PYTHON' or subject = 'Django'"
        elif skill == "IJP":
            query = "select qid, que, level, cr_ans, subject from question where subject = 'HTML' or subject = 'CSS' or subject ='JS' or subject ='reactjs' or subject = 'PYTHON' or subject = 'Django' or subject ='DevOps'"
        
        buz_cur.execute(query)
        ques = buz_cur.fetchall()
        rques = list(sample(ques, 30))
        for rec in rques:
            rec_ans = Answersheet(uid = usrid, qid = rec[0], cr_ans = rec[3])
            rec_ans.save()
        buz_con.close()
        buz_cur.close()

        #Join Query
        buz_con = mysql.connector.connect(host='localhost', user='root', password = 'root',database ='buzzart_req')
        buz_cur = buz_con.cursor()
        buz_cur.execute("select uid, u.qid, u.cr_ans, u.ch_ans, que, subject, level, ans1, ans2, ans3, ans4 from answersheet as u left join (select q.qid, q.que, subject, level, ans1, ans2, ans3, ans4 from question as q join answers as a on q.qid = a.qid) as qu on qu.qid = u.qid")
        rand_ques = list(buz_cur.fetchall())
        buz_con.close()
        buz_cur.close()

        req.session['page_no'] = 0
        req.session['b_time'] = datetime.datetime.now()
        req.session['skill'] = skill
        tot_marks = 0
        return HttpResponseRedirect('/proceed_test')
    else:
        User_login = False        
        return render(req,'home.html', {'msg':'You are not Logged in', 'userlogin':User_login})

#Test Instructions

@never_cache
def test_rule(req, skill):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.session.has_key('UserID'):
        User_login =True
        usrid = req.session.get('UserID')
        rec = Users.objects.get(uid=usrid)
        if skill =='UI':
            if rec.ui_app != 1:
                return render(req,'home.html', {'uid':usrid,'msg':'You are not allowed to visit that link', 'userlogin':User_login})
        elif skill == 'FS':
            if rec.fs_app != 1:
                return render(req,'home.html', {'uid':usrid,'msg':'You are not allowed to visit that link', 'userlogin':User_login})
        elif skill == 'Python':
            if rec.python_app != 1:
                return render(req,'home.html', {'uid':usrid,'msg':'You are not allowed to visit that link', 'userlogin':User_login})
        elif skill == 'IJP':
            if rec.ijp_app != 1:
                return render(req,'home.html', {'uid':usrid,'msg':'You are not allowed to visit that link', 'userlogin':User_login})

        return render(req,"test.html",{'uid':usrid, 'userlogin':User_login, 'skill':skill})
    else:
        User_login =False
        return render(req,"home.html",{'msg':'You are not logged in','userlogin':User_login})


#Test Home Page
def test_home(req):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.session.has_key('UserID'):
        User_login =True
        usrid = req.session.get('UserID')
        rec = Users.objects.get(uid=usrid)
        recs = rec.approval_set.exclude(submit_st='Submitted')
        return render(req,"test_home.html",{'uid':usrid, 'userlogin':User_login, 'skills':recs})
    else:
        User_login =False
        return render(req,"home.html",{'msg':'You are not logged in','userlogin':User_login})


#Test Results
def test_Results(req):
    if req.user.is_authenticated:
        adminlog = True
        usr_data = Users.objects.filter(status='Old')
        adr_data = Address.objects.filter(status='Old')
        qua_data = Qualifications.objects.filter(status='Old')
        exp_data = Experience.objects.filter(status='Old')
        skl_data = Skills.objects.filter(status='Old')
        res_data = Approval.objects.filter(submit_st='Submitted')
        s_list=['UI','Python','FS','IJP']
        return render(req,'applicants_result.html',{'slist':s_list, 'adminlog':adminlog,'usr':usr_data,'adr':adr_data,'qua':qua_data,'exp':exp_data,'skl':skl_data,'res':res_data})
    else:
        messages.success(req,"You are not logged in")
        adminlog = False
        return render(req,'admin_board.html',{'adminlog':adminlog})
    

#Applicant Approvals
def approvals(req):
    co = 0
    userid=''
    for rq in req.POST:
        if co > 0:
            rq_lst = rq.split('-')
            rec = Users.objects.get(uid=rq_lst[0])
            rec.approval_set.create(uid=rq_lst[0],app_sub = rq_lst[1], alottime=3600)
            userid = rec.uid
            recv_mail = rec.email
            rec.save()
            
            sender_email = "mohfarooqui.bpl@gmail.com"
            password = 'fnrjrzeremaehlhb'

            message = MIMEMultipart("alternative")
            message["Subject"] = "Buzzart Test Link"
            message["From"] = sender_email
            message["To"] = recv_mail
            html_text='''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <style>
                        .main {
                            padding: 10px;
                            font-family: monospace;
                            font-size: 12px;
                        }
                    </style>
                </head>
                <body style="background-color:gainsboro">
                    <div>
                        <img src="/static/Images/Buzzart-Logo.png" width="10%" />
                    </div>
                    <div class="main">
                        <h3>Welcome to Buzzart Software Pvt Ltd</h5>
                        <p>Hello Mr {{ userid }},</p>
                        <p>We welcome to the Buzzart Recruitment Process your text link mentioned below</p>
                        <a href="http://127.0.0.1:8000/log">Click Here to Begin Test</a>
                        <p>Best of luck</p>
                    </div>
                    <br/><br/><br/><br/>
                    <div class="main">
                        <p>Regards</p>
                        <p>HR,</p>
                        <p>Buzzart Softwares,</p>
                        <img src="/static/Images/BS.jpeg" width="10%"/>
                    </div>
                </body>
                </html>
            '''
            part = MIMEText(html_text, "html")
            
            message.attach(part)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, recv_mail, message.as_string()
                )

            rec=Users.objects.get(uid=userid)
            rec.status='Old'
            rec.qualifications_set.update(status='Old')
            rec.address_set.update(status='Old')
            rec.experience_set.update(status='Old')
            rec.skills_set.update(status='Old')
            rec.save()
        co +=1
        
    messages.success(req,'Approval for test done. Confirmation mail sent to candidates.')
    return render(req,'admin_board.html')

#Applicant Views
def applicantview(req):
    if req.user.is_authenticated:
        adminlog = True
        usr_data = Users.objects.filter(status='New')
        adr_data = Address.objects.filter(status='New')
        qua_data = Qualifications.objects.filter(status='New')
        exp_data = Experience.objects.filter(status='New')
        skl_data = Skills.objects.filter(status='New')
        s_list=['UI','Python','FS','IJP']
        return render(req,'applicants_board.html',{'slist':s_list, 'adminlog':adminlog,'usr':usr_data,'adr':adr_data,'qua':qua_data,'exp':exp_data,'skl':skl_data})
    else:
        messages.success(req,"You are not logged in")
        adminlog = False
        return render(req,'admin_board.html',{'adminlog':adminlog})
    

#Logout Admin
def adminLogout(req):
    logout(req)
    messages.success(req,"You are Sucessfully Loged Out :")
    adminlog = False
    return render(req,'admin_board.html',{'adminlog':adminlog})


#Admin Panel
def admin_board(req):
    if req.user.is_authenticated:
        adminlog = True
        return render(req,'admin_board.html',{'adminlog':adminlog})
    else:
        adminlog = False
        return render(req,'admin_board.html',{'adminlog':adminlog})
    
#Admin Login
def adminlogin(req):
    if req.method == 'POST':
        fm = AuthenticationForm(request=req, data =req.POST)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            autUsr = authenticate(username = unm, password = pwd)
            if autUsr is not None:
                messages.success(req, "Admin Panel")
                login(req, autUsr)
                adminlog = True
                return render(req,"admin_board.html",{'adminlog':adminlog})
        else:
            messages.success(req, "Incorrect User ID or Password")
            adminlog = False
            fm = AuthenticationForm()
            return render(req,'AdminLogin.html',{'frm':fm})
    else:
        adminlog = False
        fm = AuthenticationForm()
    return render(req,"AdminLogin.html",{'frm':fm})


def add_quali(req):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.session.has_key('UserID'):
        usrid = req.session.get('UserID')
        User_login =True
        if req.method =="GET":
            r_frm = Quali_Form()
            return render(req,"add_quali.html",{'R_Frm':r_frm})

        if req.method == "POST":
            cert = req.POST['qualification']
            univ = req.POST['university_name']
            iname = req.POST['institute_name']
            fdate = req.POST['from_date']
            tdate = req.POST['to_date']
            per = req.POST['percentage']
            grd = req.POST['grade']
            yer = req.POST['year']
                    
            rec = Users.objects.get(uid=usrid)

            rec.qualifications_set.create(uid = usrid, qualification = cert, university_name = univ, institute_name = iname, from_date = fdate, to_date = tdate, percentage = per, grade = grd, year = yer)
            return render(req,'home.html',{'msg':'Qualification Sucessfully Added','uid':usrid, 'userlogin':User_login})
    else:
        User_login = False
        return render(req,'home.html',{'msg':'You are not logged in', 'userlogin':User_login})


def add_Exp(req):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.session.has_key('UserID'):
        usrid = req.session.get('UserID')
        User_login =True
        if req.method =="GET":
            r_frm = Expr_Form()
            return render(req,"add_expr.html",{'R_Frm':r_frm, 'userlogin':User_login})

        if req.method == "POST":
            tit = req.POST['title']
            comp = req.POST['company']
            yrs = req.POST['years']
            mnt = req.POST['months']
            fdate = req.POST['from_date']
            tdate = req.POST['to_date']
                    
            rec = Users.objects.get(uid=usrid)

            rec.experience_set.create(uid = usrid, title = tit, company = comp, years = yrs, months = mnt, from_date=fdate, to_date = tdate)
            return render(req,'home.html',{'msg':'Experience Sucessfully Added','uid':usrid, 'userlogin':User_login})
    else:
        User_login = False
        return render(req,'home.html',{'msg':'You are not logged in', 'userlogin':User_login})


def add_skills(req):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.session.has_key('UserID'):
        usrid = req.session.get('UserID')
        User_login =True
        if req.method =="GET":
            r_frm = Skills_Form()
            return render(req,"add_skills.html",{'R_Frm':r_frm, 'userlogin':User_login})

        if req.method == "POST":
            sname = req.POST['skill_name']
            expyr = req.POST['experience']
            slvl = req.POST['skill_level']
            rec = Users.objects.get(uid=usrid)
            rec.skills_set.create(uid = usrid, skill_name = sname, skill_type = expyr, skill_level = slvl)
            return render(req,'home.html',{'msg':'Skill Sucessfully Added', 'uid':usrid, 'userlogin':User_login})
    else:
        User_login = False
        return render(req,'home.html',{'msg':'You are not logged in', 'userlogin':User_login})


def home(req):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.session.has_key('UserID'):
        usrid = req.session.get('UserID')
        User_login =True
        return render(req,"home.html",{'msg':'Welcome','uid':usrid, 'userlogin':User_login})
    else:
        User_login =False        
    return render(req,'home.html',{'userlogin':User_login})


@never_cache
def registration(req):
    req.session['last_activity'] = datetime.datetime.now().second
    if req.method =="GET":
        r_frm = Reg_Frm()
        return render(req,"Register.html",{'R_Frm':r_frm})

    if req.method == "POST":
        fnm = req.POST['FirstName']
        lnm = req.POST['LirstName']
        con = req.POST['Contact']
        usrid = req.POST['UserID']
        pwd = req.POST['Password']
        emailid = req.POST['E_mail']
        udob = req.POST['Date_of_Birth']
        add1 = req.POST['Address1']
        add2 = req.POST['Address2']
        add3 = req.POST['Address3']
        pin = req.POST['Pincode']
        city = req.POST['City']
        country = req.POST['country']
        state = req.POST['state']
        pre_org = req.POST['Previous_Organization']
        exp = req.POST['Experience']
        
        ui = req.POST.get('UI_Developer',False)
        if ui=='on':
            ui= True
        
        py = req.POST.get('Python_Developer', False)
        if py=='on':
            py= True
        
        fs = req.POST.get('Full_Stack_Developer',False)
        if fs=='on':
            fs= True
        
        ijp = req.POST.get('IJP',False)
        if ijp=='on':
            ijp= True

        usr = Users(uid=usrid, first_name = fnm, last_name =lnm, mobile =con, email =emailid, password= pwd, dob = udob, t_experience = exp, previous_org = pre_org, ui_app = ui, python_app = py, fs_app=fs, ijp_app = ijp, link=False)
        usr.save()
        rec = Users.objects.get(uid=usrid)

        rec.address_set.create(uid = usrid, address1 = add1, address2 = add2, address3 = add3, pincode = pin, country = country, state = state, city = city)
        return render(req,'home.html',{'msg':'Sucessfully Registered'})

    return render(req,'home.html',{'msg':'Sucessfully Registered'})

@never_cache
def signin(req):
    if req.method =="GET":
        return render(req, "login.html")
    if req.method == "POST":
        usrid = req.POST['usrid']
        pwd = req.POST["pwd"]
        rec = Users.objects.filter(uid = usrid,password = pwd)
        if rec:
            req.session['UserID'] = usrid
            req.session.set_expiry(0)
            req.session['last_activity'] = datetime.datetime.now().second
            # req.session['test'] = False
            User_login =True
            return render(req,"home.html",{'msg':'Welcome','uid':usrid, 'userlogin':User_login})
        else:
            User_login =False
            return render(req,"login.html",{'err':"Invalid Credentials",'userlogin':User_login})

    return render(req, "login.html")


def userlogout(req):
    if req.session.has_key('UserID'):
        del req.session['UserID']
        # del req.session['test']
        del req.session['last_activity']
        User_Login = False
    return render(req,'home.html',{'msg':"Logged out Successfully",'userlogin':User_Login})


#Unused Views
def test_paper(req):        
    # webbroser = webbrowser.get()

    # print(webbroser.basename)
    # # b = webdriver.Chrome(executable_path=r'C:\Program Files\chromewebdriver\chromedriver.exe')
    # # b.maximize_window()

    # class EventListeners(AbstractEventListener):
    #     def before_navigate_to(self, url, driver):
    #         print("before_navigate_to %s" % url)

    #     def after_navigate_to(self, url, driver):
    #         print("after_navigate_to %s" % url)

    #     def before_click(self, element, driver):
    #         print("before_click %s" % element)

    #     def after_click(self, element, driver):
    #         print("after_click %s" %element)

    #     def after_navigate_forward(self, driver):
    #         print("after_navigate_forward")

    #     def before_navigate_forward(self, driver):
    #         print("before_navigate_forward")

    #     def after_navigate_back(self, driver):
    #         print("after_navigate_back")

    #     def before_navigate_back(self, driver):
    #         print("before_navigate_back")

    #     def before_change_value_of(self, element, driver):
    #         print("before_change_value_of")

    # d = EventFiringWebDriver(webbroser,EventListeners())

    # d.get('https://www.cnn.com')
    # d.implicitly_wait(20)
    # d.get('https://www.google.de')
    # d.implicitly_wait(20)
    # d.back()

    # def on_click(x, y, button, pressed):
    #     if pressed:
    #         print('Mouse clicked')
    #         time.sleep(2)
    #         print("Navigation to: %s " % webbroser.current_url)

    # with Listener(on_click=on_click) as listener:
    #     listener.join()

    #wn = req.session[]
    return render(req, 'test_paper.html')


# Function Based Pagination
# def proceed_test(req):
#     #req.session['last_activity'] = datetime.datetime.now().second
#     if req.session.has_key('UserID'):
#         usrid = req.session.get('UserID')
#         User_login = True
#         paginatorObj = Paginator(rand_ques,1,orphans = 0)
#         cur_page = req.GET.get('page')
#         page_context = paginatorObj.get_page(cur_page)  
#         # ans = req.GET.get['answer']
#         # print("Selected Option ",ans)     
#         return render(req,"test_paper.html",{'page_obj':page_context, 'noofpages':paginatorObj.num_pages, 'msg':'Welcome','uid':usrid, 'userlogin':User_login})
#     else:
#         User_login = False        
#         return render(req,'home.html',{'msg':'You are not Logged in', 'userlogin':User_login})

# def send_mail(req):
#     if req.method =='GET':
#         return render(req,'send.html')
#     if req.method =='POST':
#         rec_eml = req.POST['emailid']
#         msg = req.POST['msg']
#         # Create a secure SSL context
#         con = ssl.create_default_context()
#         port = 465  # For SSL
#         smtp_server = "smtp.gmail.com"
#         sender_email = "mohfarooqui.bpl@gmail.com"  # Enter your address
#         password = 'fnrjrzeremaehlhb'
       
#         with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
#             server.login(sender_email, password)
#             server.sendmail(sender_email, rec_eml, msg)
        
#         return render (req, 'home.html',{'msg':'Mail Sent Sussesfully', 'userlogin':User_login})
        
#         # smtp_server = "smtp.mail.yahoo.com"
#         # sender_email = "farooqui_bpl@yahoo.com"
#         # password = "Device*1234"
#         # port = 465  # For starttls
#         # with smtplib.SMTP("smtp.mail.yahoo.com", port=465, context = con) as server:
#         #     server.login(user=sender_email,password=password)
#         #     server.sendmail(from_addr=sender_email,to_addrs=rec_eml,msg=msg)
        

#         # Try to log in to server and send email
#         # try:
#         #     server = smtplib.SMTP(smtp_server,port)
#         #     server.ehlo() # Can be omitted
#         #     server.starttls(context=context) # Secure the connection
#         #     server.ehlo() # Can be omitted
#         #     server.login(sender_email, password)
#         #     server.sendmail(sender_email, rec_eml, msg)
#         #     return render (req, 'home.html',{'msg':'Mail Sent Sussesfully'})
#         #     # TODO: Send email here
#         # except Exception as e:
#         #     # Print any error messages to stdout
#         #     print(e)
#         # finally:
#         #     server.quit() 
#     return render (req,'home.html')