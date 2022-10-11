from os import environ
from telnetlib import LOGOUT
from django.utils.deprecation import MiddlewareMixin
import datetime
from django.shortcuts import render

class SessionExpiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.session.has_key('UserID'):
            last_activity = request.session['last_activity']
            now = datetime.datetime.now().second
            
            #LOGOUT_SECONDS = 3600 if request.session['test'] else 20
            LOGOUT_SECONDS = 60
            if (now - last_activity) > 20:
                del request.session['UserID']
                del request.session['last_activity']
                request.session.clear_expired()
                return render(request,'home.html',{'msg':'Session Expired'})
