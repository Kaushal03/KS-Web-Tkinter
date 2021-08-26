#######################################################  WEB TKINTER ####################################################### 
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image  
import tkinter.font as tkFont
from googlesearch import search
import webbrowser
import time
import os
    
############################################################################################################
login_id=Tk()
login_id.geometry("1600x800+0+0") 
login_id.title("LOGIN ID")
login_id.configure(bg='light green')

##########################################################################################################
localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION
lblDateTime=Label(font=("arial",20,"bold"),text=localtime,fg="dark green",bg='light green',bd=10,anchor="w")
lblDateTime.pack()
#########################################################################################################
Label(login_id,font=("arial",20,"bold"),fg='dark green',bg='light green' ,text="ENTER THE BELOW DETAILS TO VERIFY").pack()
Label(login_id, text="Login Id",font=('arial',40),fg='dark green',bg='light green').pack()
entry_1 = Entry(login_id, font=('arial',40),bg='light green',fg='dark green')
entry_1.pack()
Label(login_id, text="Password",font=('arial',40),fg='dark green', bg='light green').pack()
entry_2 = Entry(login_id, font=('arial',40),show="*",bg='light green',fg='dark green')
entry_2.pack()
############################################################################################################################
def printMsg():
    if((entry_1.get()=='Kaushal' and entry_2.get()=='844') or (entry_1.get()=='Ks' and entry_2.get()=='744') or (entry_1.get()=='Tiger' and entry_2.get()=='944') ):
        tkinter.messagebox.showinfo('login result', 'CONGRATULATIONS!! LOGIN SUCCESSFUL')
        createWindow()
    else:
        tkinter.messagebox.showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

button_1 = Button(login_id, text="Login",font=('arial',30),bg='light green',fg='dark green', command=printMsg).place(x=320,y=420)
button_2 = Button(login_id, text="Quit",font=('arial',30),bg='light green',fg='dark green', command=login_id.destroy).place(x=520,y=420)
######################################################################################################################################    
def createWindow():
    def start():
        global root
        root = Toplevel(ps)
        root.geometry("1600x800+0+0") 
        root.title("KS TECHNOLOGY")
        root.configure(bg="light green")


        Tops=Frame(root,width = 1600,height = 50,bg="light green",relief=SUNKEN)
        Tops.pack(side=TOP)

        f1=Frame(root,width = 550,height = 700,bg="light green",relief=SUNKEN)
        f1.pack(side=LEFT)

        f2=Frame(root,width = 300,height = 700,bg="light green",relief=SUNKEN)
        f2.pack(side=RIGHT)

        localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

        lblInfo=Label(Tops,font=("arial",30,"bold"),text="WELCOME TO THE WORLD OF TECHNOLOGY",bg='light green',fg="dark green",bd=10,anchor="w")
        lblInfo.pack()

        lblDateTime=Label(Tops,font=("arial",20,"bold"),text=localtime,bg='light green',fg="dark green",bd=10,anchor="w")
        lblDateTime.pack()

        lblInfo=Label(Tops,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg='light green',fg="dark green",bd=10,anchor="w")
        lblInfo.pack()


        ###########################################################################################################
        def google():
            webbrowser.open("https://www.google.com",new=1)

        def youtube():
            webbrowser.open("https://www.youtube.com/",new=1)

        def gmail():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox",new=1)

        def netflix():
            webbrowser.open("https://www.netflix.com/in/",new=1)

        def prime():
            webbrowser.open("https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_131|m_Ycxs8vQMc_c386559716838",new=1)

        def whatsapp():
            webbrowser.open("https://web.whatsapp.com/",new=1)

        def instagram():
            webbrowser.open("https://www.instagram.com/accounts/login/",new=1)

        def facebook():
            webbrowser.open("https://www.facebook.com/",new=1)

        def twitter():
            webbrowser.open("https://twitter.com/LOGIN",new=1)
            
        def amazon():
            webbrowser.open("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_2f44qd709m_b&adgrpid=107947399415&hvpone=&hvptwo=&hvadid=459878421769&hvpos=&hvnetw=g&hvrand=933375425558687891&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061980&hvtargid=kwd-19736948676&hydadcr=5716_1738692&gclid=Cj0KCQiAlsv_BRDtARIsAHMGVSZMFLJOG9BwbHq6vJhel3RR-GTnVS-qNoQZqCdhcM6jxoehlIIohj4aAstjEALw_wcB",new=1)
            
        def flipkart():
            webbrowser.open("https://www.flipkart.com/?gclid=Cj0KCQiAlsv_BRDtARIsAHMGVSZ5TsyUKAnYClpe9jefdtUbZUHnNAEDurOqt6Ci6TcHz-gJCYiYhqgaAh9YEALw_wcB&ef_id=Cj0KCQiAlsv_BRDtARIsAHMGVSZ5TsyUKAnYClpe9jefdtUbZUHnNAEDurOqt6Ci6TcHz-gJCYiYhqgaAh9YEALw_wcB:G:s&s_kwcid=AL!739!3!461496258709!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_city_nc_goog",new=1)
            
        def myntra():
            webbrowser.open("https://www.myntra.com/?utm_source=Google&utm_medium=cpc&utm_campaign=Search%20-%20Myntra%20Brand%20(India)&gclid=Cj0KCQiAlsv_BRDtARIsAHMGVSaIaOOgo_OUveLElxaQbZxI2qra3_hANqIrpZ279wzBd09ZBcqWOvIaAiMKEALw_wcB",new=1)

        def python():
            webbrowser.open("https://www.javatpoint.com/python-tutorial",new=1)

        def java():
            webbrowser.open("https://www.javatpoint.com/java-tutorial",new=1)

        def c():
            webbrowser.open("https://www.javatpoint.com/c-programming-language-tutorial",new=1)

        def linux():
            webbrowser.open("https://www.javatpoint.com/linux-tutorial",new=1)

        def cplus():
            webbrowser.open("https://www.javatpoint.com/cpp-tutorial",new=1)

        def sql():
            webbrowser.open("https://www.javatpoint.com/sql-tutorial",new=1)

        def mxplayer():
            webbrowser.open("https://www.mxplayer.in/?utm_source=paid-ext-con-perf-google_sem-web&utm_medium=web&utm_campaign=sem-dweb-100619-traffic_brand-na-generic-multi_multi-multiple-hindi-ext_paid-groupm&utm_cid=68545727484&gclid=Cj0KCQiAlsv_BRDtARIsAHMGVSZoook9TfjZq0p1icQuGDUQarTGVKX43FyemtRVBSs1Obfqp5FQvrwaAlRvEALw_wcB",new=1)

        def hotstar():
            webbrowser.open("https://www.hotstar.com/in",new=1)

        def udemy():
            webbrowser.open("https://www.udemy.com/",new=1)

        def coursera():
            webbrowser.open("https://www.coursera.org/",new=1)

        def corona():
            webbrowser.open("https://www.worldometers.info/coronavirus/",new=1)

        def cricbuzz():
            webbrowser.open("https://www.cricbuzz.com/",new=1)

        def wynk():
            webbrowser.open("https://wynk.in/music",new=1)

        def gaana():
            webbrowser.open("https://gaana.com/",new=1)

        def weather():
            webbrowser.open("https://weather.com/en-IN/weather/today/l/13.10,80.28?par=google&temp=c",new=1)

        def voot():
            webbrowser.open("https://www.voot.com/?utm_source=google_web&utm_medium=search_google&utm_campaign=c_website_search_brand_web_performance&gclid=CjwKCAiAudD_BRBXEiwAudakXzITBTKfS8FKYz4Ubc0KMZxhs8ysmiNCL0plBNo6uqV3gKTCUxv6YhoC8M8QAvD_BwE",new=1)

        def alt():
            webbrowser.open("https://www.altbalaji.com/",new=1)

        def trivago():
            webbrowser.open("https://www.trivago.in/en?themeId=115&iPathId=84780&sem_keyword=hotel%20booking&sem_creativeid=485459029170&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=&sem_param1=&sem_param2=&sem_campaignid=11541397100&sem_adgroupid=116149168487&sem_targetid=kwd-17218370&sem_location=9061980&cip=9119000439&gclid=CjwKCAiAudD_BRBXEiwAudakX85jXa9m-JaF2mJFxSpU6zPJuAlB4hEmh28EaiAafdydriJ4rYpnBBoCGrUQAvD_BwE",new=1)

        def agoda():
            webbrowser.open("https://www.agoda.com/en-in/?site_id=1829958&tag=07a17165-ad8a-d430-7bb0-00ad79913b89&device=c&network=g&adid=464747013592&rand=3326771037170302319&expid=&adpos=&gclid=CjwKCAiAudD_BRBXEiwAudakX6OVdA6vkBgHQ4RjwLevuc0OvKPN2aP6DPhOFyaKard6PbrSS1couRoCiUEQAvD_BwE#",new=1)

        def goibibo():
            webbrowser.open("https://www.goibibo.com/hotels/",new=1)

        def mmt():
            webbrowser.open("https://www.makemytrip.com/hotels/",new=1)

        def yatra():
            webbrowser.open("https://www.yatra.com/hotels/hotels-in-chennai",new=1)

        def ooyo():
            webbrowser.open("https://www.oyorooms.com/",new=1)

        def trainmann():
            webbrowser.open("https://www.trainman.in/",new=1)

        def railyatri():
            webbrowser.open("https://www.railyatri.in/train-ticket?gclid=CjwKCAiAudD_BRBXEiwAudakX-Xr0QaYeJh_Rnq5pvMctTqPu8M1OrZ-6P8uOAss98n_NXyaDvFQFhoCbQMQAvD_BwE",new=1)

        def mmt1():
            webbrowser.open("https://www.makemytrip.com/railways/",new=1)

        def mmt2():
            webbrowser.open("https://www.makemytrip.com/flights/",new=1)

        def goindigo():
            webbrowser.open("https://www.goindigo.in/flight-booking.html",new=1)

        def yatra1():
            webbrowser.open("https://www.yatra.com/flights",new=1)

        def emt():
            webbrowser.open("https://www.easemytrip.com/flights.html",new=1)

        def goibibo1():
            webbrowser.open("https://www.goibibo.com/flights/",new=1)

        def ixigo():
            webbrowser.open("https://www.ixigo.com/?utm_source=Google_Search&utm_medium=paid_search_google&utm_campaign=Ixigo_Brand&gclid=CjwKCAiAudD_BRBXEiwAudakX7I_g5Tqy1dqYvnzYBXlHaCb_doQyfYZSHA2vgJe0-myMekV6EtibhoC7gEQAvD_BwE",new=1)

        def mmt3():
            webbrowser.open("https://www.makemytrip.com/bus-tickets/tirupur-chennai-booking.html?gclid=CjwKCAiAudD_BRBXEiwAudakXzvSa_kWhbETitLRBuUs0cSbYiWBfW1dFLb5ROUH0wxfb9PyOFo5fhoClNsQAvD_BwE&ef_id=CjwKCAiAudD_BRBXEiwAudakXzvSa_kWhbETitLRBuUs0cSbYiWBfW1dFLb5ROUH0wxfb9PyOFo5fhoClNsQAvD_BwE%3AG%3As&cmp=SEM%7CD%7CBUS%7CG%7CDSA%7CDSA_Bus-Home%7C1-DSA-Bus%7CETA%7CRegular%7C381178823458&s_kwcid=AL!1631!3!381178823458!b!!g!!",new=1)

        def redbus():
            webbrowser.open("https://www.redbus.in/?gclid=CjwKCAiAudD_BRBXEiwAudakX9WqEpOtUEgFWkqfpZpYxfWQQ7uov4IqlB1K3FoSbcDvtbvbTNLKjBoC-OQQAvD_BwE",new=1)

        def yatra2():
            webbrowser.open("https://www.yatra.com/bus-booking",new=1)

        def goibibo2():
            webbrowser.open("https://www.goibibo.com/bus/?ef_id=CjwKCAiAudD_BRBXEiwAudakX7t2FlyiHTpdo4_s1oJHne_i0YlvWMFqEJIHxxpLPyCXK2w3GMTc6hoCW2cQAvD_BwE:G:s&utm_source=google&utm_medium=cpc&utm_campaign=Bus-DSA-Domestic_DT&utm_content=Bus-Home-Page&gclid=CjwKCAiAudD_BRBXEiwAudakX7t2FlyiHTpdo4_s1oJHne_i0YlvWMFqEJIHxxpLPyCXK2w3GMTc6hoCW2cQAvD_BwE#home",new=1)

        def ixigo1():
            webbrowser.open("https://www.ixigo.com/buses",new=1)

        def railyatri1():
            webbrowser.open("https://www.railyatri.in/bus-booking",new=1)

        def saavn():
            webbrowser.open("https://www.jiosaavn.com/",new=1)

        def wpdf():
            webbrowser.open("https://smallpdf.com/word-to-pdf",new=1)

        def pdfw():
            webbrowser.open("https://smallpdf.com/pdf-to-word",new=1)

        def jpgpdf():
            webbrowser.open("https://smallpdf.com/jpg-to-pdf",new=1)

        def pdfjpg():
            webbrowser.open("https://smallpdf.com/pdf-to-jpg",new=1)

        def mergepdf():
            webbrowser.open("https://smallpdf.com/merge-pdf",new=1)

        def moresmallpdf():
            webbrowser.open("https://smallpdf.com/",new=1)

        def google_meet():
            webbrowser.open("https://meet.google.com/",new=1)

        def google_classroom():
            webbrowser.open("https://classroom.google.com/h",new=1)

        def zoom():
            webbrowser.open("https://zoom.us/meetings",new=1)

        def microsoft_teams():
            webbrowser.open("https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/log-in",new=1)

        def snapchat():
            webbrowser.open("https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome",new=1)

        def google_flights():
            webbrowser.open("https://www.google.com/travel/flights?tfs=CBwQARoaagwIAhIIL20vMGM4dGsSCjIwMjEtMDEtMjUaGhIKMjAyMS0wMS0yOXIMCAISCC9tLzBjOHRrcAGCAQsI____________AUABSAGYAQE",new=1)

        def google_maps():
            webbrowser.open("https://www.google.com/maps",new=1)

        def ttt():
            import ttttk

        def color_game():
            import colortkinter

        def flame():
            import flametkinter

        def guess():
            import guessnumbertkinter

        def hr():
            webbrowser.open("https://www.hackerrank.com/domains/python",new=1)

        def linkedin():
            webbrowser.open("https://www.linkedin.com/uas/login",new=1)
        
        def lc():
            webbrowser.open("https://leetcode.com/",new=1)

        def gh():
            webbrowser.open("https://github.com/",new=1)

        def rps():
            import rpstk

        def stucor():
            webbrowser.open("https://stucor.in/",new=1)

        def jb():
            webbrowser.open("https://jamboard.google.com/",new=1)

        def telegram():
            webbrowser.open("https://web.telegram.org/#/login",new=1)

        def oracle_sql():
            webbrowser.open("https://livesql.oracle.com/apex/f?p=590:1000",new=1)

        def covid19():
            webbrowser.open("https://www.mygov.in/covid-19",new=1)

        def wtsp():
            webbrowser.open("https://wa.me/+919344404767?text=How%20are%20you%20?",new=1)
            


            

        

            

        
            
    ######################################################################################################################################

        def movies():
            global movie
            movie = Toplevel(root)
            movie.title(" MOVIES")
            movie.geometry("1600x800+0+0")
            movie.configure(bg="light green")

            Tops3=Frame(movie,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops3.pack(side=TOP)

            f13=Frame(movie,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f13.pack(side=LEFT)

            f23=Frame(movie,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f23.pack(side=RIGHT)

            lblInfo=Label(Tops3,font=("arial",40,"bold") ,text="MOVIES",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops3,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops3,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()
            
            btnA=Button(f13,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Netflix",bg="light green",
                    command=netflix,anchor="w",width=10,height=0,compound="c")
            btnA.grid(row=0,column=0)


            btnB=Button(f13,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Amazon Prime",bg="light green",
                    command=prime,anchor="w",width=10,height=0,compound="c")
            btnB.grid(row=0,column=1)

            btnC=Button(f13,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="MX Player",bg="light green",
                    command=mxplayer,anchor="w",width=10,height=0,compound="c")
            btnC.grid(row=0,column=2)



            btnD=Button(f13,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Hotstar",bg="light green",
                    command=hotstar,anchor="w",width=10,height=0,compound="c")
            btnD.grid(row=0,column=3)

            btnE=Button(f13,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="VOOT",bg="light green",
                    command=voot,anchor="w",width=10,height=0,compound="c")
            btnE.grid(row=0,column=4)

            btnF=Button(f13,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="ALT Balaji",bg="light green",
                    command=alt,anchor="w",width=10,height=0,compound="c")
            btnF.grid(row=0,column=5)
            

    ##################################################################################################################################
        def socialmedia():
            global social_media
            social_media = Toplevel(root)
            social_media.title("SOCIAL MEDIA")
            social_media.geometry("1600x800+0+0")
            social_media.configure(bg="light green")

            Tops2=Frame(social_media,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops2.pack(side=TOP)

            f12=Frame(social_media,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f12.pack(side=LEFT)

            f22=Frame(social_media,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f22.pack(side=RIGHT)

            lblInfo=Label(Tops2,font=("arial",40,"bold") ,text="SOCIAL MEDIA",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops2,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops2,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()
            btna=Button(f12,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="WHATSAPP",bg="light green",
                    command=whatsapp,anchor="w",width=10,height=0,compound="c")
            btna.grid(row=0,column=0)
            
            btnb=Button(f12,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="INSTAGRAM",bg="light green",
                    command=instagram,anchor="w",width=10,height=0,compound="c")
            btnb.grid(row=0,column=1)

            
            btnc=Button(f12,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="FACEBOOK",bg="light green",
                    command=facebook,anchor="w",width=10,height=0,compound="c")
            btnc.grid(row=0,column=2)


            btnd=Button(f12,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="TWITTER",bg="light green",
                    command=twitter,anchor="w",width=10,height=0,compound="c")
            btnd.grid(row=0,column=3)

            btne=Button(f12,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="SNAPCHAT",bg="light green",
                    command=snapchat,anchor="w",width=10,height=0,compound="c")
            btne.grid(row=0,column=4)

            btnf=Button(f12,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="TELEGRAM",bg="light green",
                    command=telegram,anchor="w",width=10,height=0,compound="c")
            btnf.grid(row=0,column=5)

    ########################################################################################################################################
        def shopping():
            global shop
            shop=Toplevel(root)
            shop.title("SHOPPING")
            shop.geometry("1600x800+0+0")
            shop.configure(bg="light green")

            
            Tops1=Frame(shop,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops1.pack(side=TOP)

            f11=Frame(shop,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f11.pack(side=LEFT)

            f21=Frame(shop,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f21.pack(side=RIGHT)

            lblInfo=Label(Tops1,font=("arial",40,"bold") ,text="SHOPPING",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops1,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops1,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn1a=Button(f11,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="AMAZON",bg="light green",
                    command=amazon,anchor="w",width=10,height=0,compound="c")
            btn1a.grid(row=0,column=0)


            btn1b=Button(f11,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="FLIPKART",bg="light green",
                    command=flipkart,anchor="w",width=10,height=0,compound="c")
            btn1b.grid(row=0,column=1)


            btn1c=Button(f11,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="MYNTRA",bg="light green",
                    command=myntra,anchor="w",width=10,height=0,compound="c")
            
            btn1c.grid(row=0,column=2)
        ######################################################################################################################

        def coding():
            global code
            code=Toplevel(root)
            code.title("CODING")
            code.geometry("1600x800+0+0")
            code.configure(bg="light green")
            
            Tops4=Frame(code,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops4.pack(side=TOP)

            f14=Frame(code,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f14.pack(side=LEFT)

            f24=Frame(code,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f24.pack(side=RIGHT)

            lblInfo=Label(Tops4,font=("arial",40,"bold") ,text="CODING LANGUAGE",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops4,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops4,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn2a=Button(f14,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="PYTHON",bg="light green",
                    command=python,anchor="w",width=10,height=0,compound="c")
            btn2a.grid(row=0,column=0)

            btn2b=Button(f14,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="JAVA",bg="light green",
                    command=java,anchor="w",width=10,height=0,compound="c")
            btn2b.grid(row=0,column=1)

            btn2c=Button(f14,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="C",bg="light green",
                    command=c,anchor="w",width=10,height=0,compound="c")
            btn2c.grid(row=0,column=2)

            btn2d=Button(f14,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="C++",bg="light green",
                    command=cplus,anchor="w",width=10,height=0,compound="c")
            btn2d.grid(row=0,column=3)

            btn2e=Button(f14,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="LINUX",bg="light green",
                    command=linux,anchor="w",width=10,height=0,compound="c")
            btn2e.grid(row=0,column=4)

            btn2f=Button(f14,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="SQL",bg="light green",
                    command=sql,anchor="w",width=10,height=0,compound="c")
            btn2f.grid(row=0,column=5)

        #################################################################################################################
        def course():
            global csr
            csr=Toplevel(root)
            csr.title("CODING")
            csr.geometry("1600x800+0+0")
            csr.configure(bg="light green")
            
            Tops5=Frame(csr,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops5.pack(side=TOP)

            f15=Frame(csr,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f15.pack(side=LEFT)

            f25=Frame(csr,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f25.pack(side=RIGHT)

            lblInfo=Label(Tops5,font=("arial",40,"bold") ,text="COURSES",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops5,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops5,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn2a=Button(f15,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="UDEMY",bg="light green",
                    command=udemy,anchor="w",width=10,height=0,compound="c")
            btn2a.grid(row=0,column=0)

            btn2b=Button(f15,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="COURSERA",bg="light green",
                    command=coursera,anchor="w",width=10,height=0,compound="c")
            btn2b.grid(row=0,column=1)
        ######################################################################################################################
        def songs():
            global msc
            msc=Toplevel(root)
            msc.title("CODING")
            msc.geometry("1600x800+0+0")
            msc.configure(bg="light green")
            
            Tops6=Frame(msc,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops6.pack(side=TOP)

            f16=Frame(msc,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f16.pack(side=LEFT)

            f26=Frame(msc,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f26.pack(side=RIGHT)

            lblInfo=Label(Tops6,font=("arial",40,"bold") ,bg="light green",text="MUSIC",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops6,font=("arial",20,"bold"),bg="light green",text=localtime,fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops6,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            lblInfo=Label(Tops6,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()


            btn3a=Button(f16,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="WYNK",bg="light green",
                    command=wynk,anchor="w",width=10,height=0,compound="c")
            btn3a.grid(row=0,column=0)

            btn3b=Button(f16,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="GAANA",bg="light green",
                    command=gaana,anchor="w",width=10,height=0,compound="c")
            btn3b.grid(row=0,column=1)

            btn3c=Button(f16,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="SAAVN",bg="light green",
                    command=saavn,anchor="w",width=10,height=0,compound="c")
            btn3c.grid(row=0,column=2)

            msc.mainloop()

            
        ################################################################################################################
        def hotel():
            global ht
            ht=Toplevel(bk)
            ht.title("HOTEL BOOKING")
            ht.geometry("1600x800+0+0")
            ht.configure(bg="light green")

            
            Tops7a=Frame(ht,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops7a.pack(side=TOP)

            f17a=Frame(ht,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f17a.pack(side=LEFT)

            f27a=Frame(ht,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f27a.pack(side=RIGHT)

            lblInfo=Label(Tops7a,font=("arial",40,"bold") ,text="HOTEL BOOKING",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops7a,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops7a,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn4a1=Button(f17a,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Trivago",bg="light green",
                    command=trivago,anchor="w",width=10,height=0,compound="c")
            btn4a1.grid(row=0,column=0)

            btn4a2=Button(f17a,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Agoda",bg="light green",
                    command=agoda,anchor="w",width=10,height=0,compound="c")
            btn4a2.grid(row=0,column=1)

            btn4a3=Button(f17a,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Goibibo",bg="light green",
                    command=goibibo,anchor="w",width=10,height=0,compound="c")
            btn4a3.grid(row=0,column=2)

            btn4a4=Button(f17a,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Make My Trip",bg="light green",
                    command=mmt,anchor="w",width=10,height=0,compound="c")
            btn4a4.grid(row=0,column=3)

            btn4a5=Button(f17a,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Yatra",bg="light green",
                    command=yatra,anchor="w",width=10,height=0,compound="c")
            btn4a5.grid(row=0,column=4)

            btn4a6=Button(f17a,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Ooyo",bg="light green",
                    command=ooyo,anchor="w",width=10,height=0,compound="c")
            btn4a6.grid(row=0,column=5)

        ##################################################################################################################
        def train():
            global tn
            tn=Toplevel(bk)
            tn.title("RAILWAY BOOKING")
            tn.geometry("1600x800+0+0")
            tn.configure(bg="light green")

            
            Tops7b=Frame(tn,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops7b.pack(side=TOP)

            f17b=Frame(tn,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f17b.pack(side=LEFT)

            f27b=Frame(tn,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f27b.pack(side=RIGHT)

            lblInfo=Label(Tops7b,font=("arial",40,"bold") ,text="RAILWAY BOOKING",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops7b,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops7b,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            
            btn4b1=Button(f17b,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Trainmann",bg="light green",
                    command=trainmann,anchor="w",width=10,height=0,compound="c")
            btn4b1.grid(row=0,column=1)

            btn4b2=Button(f17b,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Rail Yatri",bg="light green",
                    command=railyatri,anchor="w",width=10,height=0,compound="c")
            btn4b2.grid(row=0,column=2)

            btn4b3=Button(f17b,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Make My Trip",bg="light green",
                    command=mmt1,anchor="w",width=10,height=0,compound="c")
            btn4b3.grid(row=0,column=3)

        #####################################################################################################################
        def flight():
            global flt
            flt=Toplevel(bk)
            flt.title("AIRLINES BOOKING")
            flt.geometry("1600x800+0+0")
            flt.configure(bg="light green")

            
            Tops7c=Frame(flt,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops7c.pack(side=TOP)

            f17c=Frame(flt,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f17c.pack(side=LEFT)

            f27c=Frame(flt,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f27c.pack(side=RIGHT)

            lblInfo=Label(Tops7c,font=("arial",40,"bold") ,text="AIRLINES BOOKING",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops7c,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops7c,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()


            btn4c1=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Make My Trip",bg="light green",
                    command=mmt2,anchor="w",width=10,height=0,compound="c")
            btn4c1.grid(row=0,column=0)

            btn4c2=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Go Indigo",bg="light green",
                    command=goindigo,anchor="w",width=10,height=0,compound="c")
            btn4c2.grid(row=0,column=1)

            btn4c3=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Yatra",bg="light green",
                    command=yatra1,anchor="w",width=10,height=0,compound="c")
            btn4c3.grid(row=0,column=2)

            btn4c4=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Ease My Trip",bg="light green",
                    command=emt,anchor="w",width=10,height=0,compound="c")
            btn4c4.grid(row=0,column=3)

            btn4c5=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="GOGGLE FLIGHTS",bg="light green",
                    command=google_flights,anchor="w",width=10,height=0,compound="c")
            btn4c5.grid(row=1,column=0)

            btn4c6=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Goibibo",bg="light green",
                    command=goibibo1,anchor="w",width=10,height=0,compound="c")
            btn4c6.grid(row=1,column=1)

            btn4c7=Button(f17c,padx=60,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Ixigo",bg="light green",
                    command=ixigo,anchor="w",width=10,height=0,compound="c")
            btn4c7.grid(row=1,column=2)

        #################################################################################################################
        def bus():
            global bs
            bs=Toplevel(bk)
            bs.title("BUS BOOKING")
            bs.geometry("1600x800+0+0")
            bs.configure(bg="light green")

            
            Tops7d=Frame(bs,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops7d.pack(side=TOP)

            f17d=Frame(bs,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f17d.pack(side=LEFT)

            f27d=Frame(bs,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f27d.pack(side=RIGHT)

            lblInfo=Label(Tops7d,font=("arial",40,"bold") ,bg="light green",text="BUS BOOKING",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops7d,font=("arial",20,"bold"),bg="light green",text=localtime,fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops7d,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn4d1=Button(f17d,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Make My Trip",bg="light green",
                    command=mmt3,anchor="w",width=10,height=0,compound="c")
            btn4d1.grid(row=0,column=0)

            btn4d2=Button(f17d,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="dark green Bus",bg="light green",
                    command=redbus,anchor="w",width=10,height=0,compound="c")
            btn4d2.grid(row=0,column=1)

            btn4d3=Button(f17d,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Yatra",bg="light green",
                    command=yatra2,anchor="w",width=10,height=0,compound="c")
            btn4d3.grid(row=0,column=2)

            btn4d4=Button(f17d,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Goibibo",bg="light green",
                    command=goibibo2,anchor="w",width=10,height=0,compound="c")
            btn4d4.grid(row=0,column=3)

            btn4d5=Button(f17d,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Ixigo",bg="light green",
                    command=ixigo1,anchor="w",width=10,height=0,compound="c")
            btn4d5.grid(row=0,column=4)

            btn4d6=Button(f17d,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Rail Yatri",bg="light green",
                    command=railyatri1,anchor="w",width=10,height=0,compound="c")
            btn4d6.grid(row=0,column=5)

            

            




        ################################################################################################################
        def book():
            global bk
            bk=Toplevel(root)
            bk.title("BOOKING")
            bk.geometry("1600x800+0+0")
            bk.configure(bg="light green")

            
            Tops7=Frame(bk,width = 1600,height = 50,bg='light green',relief=SUNKEN)
            Tops7.pack(side=TOP)

            f17=Frame(bk,width = 550,height = 700,bg='light green',relief=SUNKEN)
            f17.pack(side=LEFT)

            f27=Frame(bk,width = 300,height = 700,bg='light green',relief=SUNKEN)
            f27.pack(side=RIGHT)

            lblInfo=Label(Tops7,font=("arial",40,"bold") ,bg='light green',text="BOOKING",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops7,font=("arial",20,"bold"),text=localtime,bg='light green',fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops7,font=("arial",23,"bold"),bg='light green',text="CLICK YOUR CHOICE ",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn4a=Button(f17,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Hotel",bg="light green",
                    command=hotel,anchor="w",width=10,height=0,compound="c")
            btn4a.grid(row=0,column=0)

            btn4b=Button(f17,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Railway",bg="light green",
                    command=train,anchor="w",width=10,height=0,compound="c")
            btn4b.grid(row=0,column=1)

            btn4c=Button(f17,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Airlines",bg="light green",
                    command=flight,anchor="w",width=10,height=0,compound="c")
            btn4c.grid(row=0,column=2)

            btn4d=Button(f17,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Bus",bg="light green",
                    command=bus,anchor="w",width=10,height=0,compound="c")
            btn4d.grid(row=0,column=3)
        ###################################################################################################################
        def file():
            global fl
            fl=Toplevel(root)
            fl.title("FILE CONVERTER")
            fl.geometry("1600x800+0+0")
            fl.configure(bg="light green")

            
            Tops8=Frame(fl,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops8.pack(side=TOP)

            f18=Frame(fl,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f18.pack(side=LEFT)

            f28=Frame(fl,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f28.pack(side=RIGHT)

            lblInfo=Label(Tops8,font=("arial",40,"bold"),bg="light green" ,text="FILE CONVERTER",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops8,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops8,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            btn5a=Button(f18,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Word to PDF",bg="light green",
                    command=wpdf,anchor="w",width=10,height=0,compound="c")
            btn5a.grid(row=0,column=0)

            btn5b=Button(f18,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="PDF to Word",bg="light green",
                    command=pdfw,anchor="w",width=10,height=0,compound="c")
            btn5b.grid(row=0,column=1)

            btn5c=Button(f18,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="JPG to PDF",bg="light green",
                    command=jpgpdf,anchor="w",width=10,height=0,compound="c")
            btn5c.grid(row=0,column=2)

            btn5d=Button(f18,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="PDF to JPG",bg="light green",
                    command=pdfjpg,anchor="w",width=10,height=0,compound="c")
            btn5d.grid(row=0,column=3)


            btn5e=Button(f18,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="Merge PDF",bg="light green",
                    command=mergepdf,anchor="w",width=10,height=0,compound="c")
            btn5e.grid(row=0,column=4)

            btn5f=Button(f18,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="MORE",bg="light green",
                    command=moresmallpdf,anchor="w",width=10,height=0,compound="c")
            btn5f.grid(row=0,column=5)

            

        ###################################################################################################################
        def online_class():
            global oc
            oc=Toplevel(root)
            oc.title("ONLINE CLASSES")
            oc.geometry("1600x800+0+0")
            oc.configure(bg="light green")

            
            Tops9=Frame(oc,width = 1600,height = 50,bg='light green',relief=SUNKEN)
            Tops9.pack(side=TOP)

            f19=Frame(oc,width = 550,height = 700,bg='light green',relief=SUNKEN)
            f19.pack(side=LEFT)

            f29=Frame(oc,width = 300,height = 700,bg='light green',relief=SUNKEN)
            f29.pack(side=RIGHT)

            lblInfo=Label(Tops9,font=("arial",40,"bold") ,text="ONLINE CLASSES",bg='light green',fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops9,font=("arial",20,"bold"),text=localtime,fg="dark green",bg='light green',bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops9,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",fg="dark green",bg='light green',bd=10,anchor="w")
            lblInfo.pack()

            lblInfo=Label(Tops9,font=("arial",23,"bold"),text="",bg='light green',fg="dark green",bd=10,anchor="w")
            lblInfo.pack()

            canvas = Canvas(Tops9, width=300, height=140)
            canvas.config(bg='light green')
            
            canvas.pack()

            my_image = PhotoImage(file='onlinecls.png')
            my_img = canvas.create_image(0,0, anchor=NW, image=my_image)

            

            btn6a=Button(f19,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="GOOGLE MEET",bg="light green",
                    command=google_meet,anchor="w",width=15,height=0,compound="c")
            btn6a.grid(row=0,column=0)

            btn6b=Button(f19,padx=50,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="GOOGLE CLASSROOM",bg="light green",
                    command=google_classroom,anchor="w",width=15,height=0,compound="c")
            btn6b.grid(row=0,column=1)

            btn6c=Button(f19,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="ZOOM",bg="light green",
                    command=zoom,anchor="w",width=15,height=0,compound="c")
            btn6c.grid(row=0,column=2)

            btn6d=Button(f19,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="MICROSOFT TEAMS",bg="light green",
                    command=microsoft_teams,anchor="w",width=15,height=0,compound="c")
            btn6d.grid(row=0,column=3)

            oc.mainloop()

        ######################################################################################################################
        class MainClass():

            def __init__(self,master):
                self.parent=master
                self.kstech()

            def kstech(self):
                self.Source=StringVar()
                Tops10=Frame(ks,width = 1600,height = 50,bg="light green",relief=SUNKEN)
                Tops10.pack(side=TOP)
                f110=Frame(ks,width = 550,height = 700,bg="light green",relief=SUNKEN)
                f110.pack(side=LEFT)
                f210=Frame(ks,width = 300,height = 700,bg="light green",relief=SUNKEN)
                f210.pack(side=RIGHT)
                lblInfo=Label(Tops10,font=("arial",40,"bold") ,text="KS SEARCH ENGINE",fg="dark green",bg="light green",bd=10,anchor="w")
                lblInfo.pack()

                localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

                lblDateTime=Label(Tops10,font=("arial",20,"bold"),text=localtime,fg="dark green",bg="light green",bd=10,anchor="w")
                lblDateTime.pack()
                label4=Label(Tops10,font=("arial",40,"bold"),text='Enter Your Query', fg= 'dark green',bg="light green",bd=10,anchor="w").pack()
                entry_3=Entry(Tops10,font=('arial',40),bg='light green',fg='dark green', textvariable=self.Source).pack()
                lblInfo=Label(Tops10,font=("arial",40,"bold") ,text="",fg="dark green",bg="light green",bd=10,anchor="w")
                lblInfo.pack()

                btn7a=Button(Tops10,padx=60,pady=16,bd=8,bg="light green",font=("arial",15,"bold"), text="  SEARCH  ",fg="dark green", command=self.search,anchor="w",width=10,height=0,compound="c")
                btn7a.pack()
                btn7b=Button(Tops10,padx=60,pady=16,bd=8,bg="light green",font=("arial",15,"bold"), text=" IMAGE SEARCH  ",fg="dark green", command=self.search1,anchor="w",width=10,height=0,compound="c")
                btn7b.pack()
                btn7c=Button(Tops10,padx=60,pady=16,bd=8,bg="light green",font=("arial",15,"bold"), text=" VIDEO SEARCH  ",fg="dark green", command=self.search2,anchor="w",width=10,height=0,compound="c")
                btn7c.pack()
                btn7d=Button(Tops10,padx=60,pady=16,bd=8,bg="light green",font=("arial",15,"bold"), text=" NEWS SEARCH  ",fg="dark green", command=self.search3,anchor="w",width=10,height=0,compound="c")
                btn7d.pack()
            def search(self):
                webbrowser.open('https://www.google.com/search?q=' + str(self.Source.get()))
            def search1(self):
                webbrowser.open('https://www.google.com/search?tbm=isch&q=' + str(self.Source.get()))
            def search2(self):
                webbrowser.open('https://www.google.com/search?tbm=vid&q=' + str(self.Source.get()))
            def search3(self):
                webbrowser.open('https://www.google.com/search?tbm=nws&q=' + str(self.Source.get()))

        def kaus():
            global ks
            ks=Toplevel(root)
            app=MainClass(ks)
            ks.geometry("1600x800+0+0")
            ks.title('KS SEARCH ENGINE')
            ks.configure(bg="light green")
            ks.mainloop()
        ###########################################################################################################################
        def games():
            global game
            game=Toplevel(root)
            game.title("GAMES")
            game.geometry("1600x800+0+0")
            game.configure(bg="light green")

            
            Tops11=Frame(game,width = 1600,height = 50,bg="light green",relief=SUNKEN)
            Tops11.pack(side=TOP)

            f111=Frame(game,width = 550,height = 700,bg="light green",relief=SUNKEN)
            f111.pack(side=LEFT)

            f211=Frame(game,width = 300,height = 700,bg="light green",relief=SUNKEN)
            f211.pack(side=RIGHT)

            lblInfo=Label(Tops11,font=("arial",40,"bold") ,text="KS GAMING CENTRE",fg="dark green",bg="light green",bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops11,font=("arial",20,"bold"),text=localtime,fg="dark green",bg="light green",bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops11,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",fg="dark green",bg="light green",bd=10,anchor="w")
            lblInfo.pack()

            lblInfo=Label(Tops11,font=("arial",23,"bold"),text=" ",fg="dark green",bg="light green",bd=10,anchor="w")
            lblInfo.pack()


            btn8a=Button(f111,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="TIC TAC TOE",fg="dark green",
                    command=ttt,anchor="w",width=15,height=0,compound="c")
            btn8a.grid(row=0,column=0)

            btn8b=Button(f111,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="COLOR GAME",fg="dark green",
                    command=color_game,anchor="w",width=15,height=0,compound="c")
            btn8b.grid(row=0,column=1)

            btn8c=Button(f111,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="FLAMES",fg="dark green",
                    command=flame,anchor="w",width=15,height=0,compound="c")
            btn8c.grid(row=0,column=2)

            btn8d=Button(f111,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="NUMBER GUESS",fg="dark green",
                    command=guess,anchor="w",width=15,height=0,compound="c")
            btn8d.grid(row=0,column=3)

            btn9d=Button(f111,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="RPS",fg="dark green",
                    command=rps,anchor="w",width=15,height=0,compound="c")
            btn9d.grid(row=1,column=0)

            
        ####################################################################################################################
        def code():
            global cd
            cd=Toplevel(root)
            cd.title("CODING PRACTICE")
            cd.geometry("1600x800+0+0")
            cd.configure(bg="light green")

            
            Tops12=Frame(cd,width = 1600,height = 50,bg='light green',relief=SUNKEN)
            Tops12.pack(side=TOP)

            f112=Frame(cd,width = 550,height = 700,bg='light green',relief=SUNKEN)
            f112.pack(side=LEFT)

            f212=Frame(cd,width = 300,height = 700,bg='light green',relief=SUNKEN)
            f212.pack(side=RIGHT)

            lblInfo=Label(Tops12,font=("arial",40,"bold") ,text="CODING PRACTICE",bg="light green",fg='dark green',bd=10,anchor="w")
            lblInfo.pack()

            localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

            lblDateTime=Label(Tops12,font=("arial",20,"bold"),text=localtime,bg="light green",fg='dark green',bd=10,anchor="w")
            lblDateTime.pack()


            lblInfo=Label(Tops12,font=("arial",23,"bold"),text="CLICK YOUR CHOICE ",bg="light green",fg='dark green',bd=10,anchor="w")
            lblInfo.pack()

            lblInfo=Label(Tops12,font=("arial",23,"bold"),text=" ",bg="light green",fg='light green',bd=10,anchor="w")
            lblInfo.pack()


            btn9a=Button(f112,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="Hackerrank",fg="dark green",
                    command=hr,anchor="w",width=15,height=0,compound="c")
            btn9a.grid(row=0,column=0)

            btn9b=Button(f112,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="Github",fg="dark green",
                    command=gh,anchor="w",width=15,height=0,compound="c")
            btn9b.grid(row=0,column=1)

            btn9c=Button(f112,padx=30,pady=16,bd=8,bg="light green",font=("arial",15,"bold"),text="Leetcode",fg="dark green",
                    command=lc,anchor="w",width=15,height=0,compound="c")
            btn9c.grid(row=0,column=2)
            
    

            

            

            

               

            
               

            


            

        #=======================================================================================================
        btn1=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Google",fg="dark green",bg="light green",
                    command=google,anchor="w",width=10,height=0,compound="c")
        btn1.grid(row=0,column=0)


        btn2=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Youtube",fg="dark green",bg="light green",
                    command=youtube,anchor="w",width=10,height=0,compound="c")
        btn2.grid(row=0,column=1)


        btn3=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Gmail",fg="dark green",bg="light green",
                    command=gmail,anchor="w",width=10,height=0,compound="c")
        btn3.grid(row=1,column=0)


        btn4=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Movies/Series",fg="dark green",bg="light green",
                    command=movies,anchor="w",width=10,height=0,compound="c")
        btn4.grid(row=1,column=1)


        btn5=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Social Media",fg="dark green",bg="light green",
                    command=socialmedia,anchor="w",width=10,height=0,compound="c")
        btn5.grid(row=2,column=0)


        btn6=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Shopping",fg="dark green",bg="light green",
                    command=shopping,anchor="w",width=10,height=0,compound="c")
        btn6.grid(row=2,column=1)
        

        btn7=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Coding",fg="dark green",bg="light green",
                    command=coding,anchor="w",width=10,height=0,compound="c")
        btn7.grid(row=3,column=0)


        btn8=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Course",fg="dark green",bg="light green",
                    command=course,anchor="w",width=10,height=0,compound="c")
        btn8.grid(row=3,column=1)


        btn9=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Corona",fg="dark green",bg="light green",
                    command=corona,anchor="w",width=10,height=0,compound="c")
        btn9.grid(row=0,column=2)


        btn10=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Cricbuzz",fg="dark green",bg="light green",
                    command=cricbuzz,anchor="w",width=10,height=0,compound="c")
        btn10.grid(row=1,column=2)


        btn11=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Music",fg="dark green",bg="light green",
                    command=songs,anchor="w",width=10,height=0,compound="c")
        btn11.grid(row=2,column=2)


        btn12=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Weather",fg="dark green",bg="light green",
                    command=weather,anchor="w",width=10,height=0,compound="c")
        btn12.grid(row=3,column=2)
        

        btn13=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Booking",fg="dark green",bg="light green",
                    command=book,anchor="w",width=10,height=0,compound="c")
        btn13.grid(row=0,column=3)
        

        btn14=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="File Converter",fg="dark green",bg="light green",
                    command=file,anchor="w",width=10,height=0,compound="c")
        btn14.grid(row=1,column=3)
        

        btn15=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="Online Class",fg="dark green",bg="light green",
                    command=online_class,anchor="w",width=10,height=0,compound="c")
        btn15.grid(row=2,column=3)


        btn16=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="KS SEARCH",fg="dark green",bg="light green",
                    command=kaus,anchor="w",width=10,height=0,compound="c")
        btn16.grid(row=3,column=3)
        

        btn17=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="GOOGLE MAPS",fg="dark green",bg="light green",
                    command=google_maps,anchor="w",width=10,height=0,compound="c")
        btn17.grid(row=4,column=0)
        

        btn18=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="GAMES",fg="dark green",bg="light green",
                    command=games,anchor="w",width=10,height=0,compound="c")
        btn18.grid(row=4,column=1)
        

        btn19=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="CODE SITE",fg="dark green",bg="light green",
                    command=code,anchor="w",width=10,height=0,compound="c")
        btn19.grid(row=4,column=2)
        

        btn20=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="STUCOR",fg="dark green",bg="light green",
                    command=stucor,anchor="w",width=10,height=0,compound="c")
        btn20.grid(row=4,column=3)

        btn21=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="JAM BOARD",fg="dark green",bg="light green",
                    command=jb,anchor="w",width=10,height=0,compound="c")
        btn21.grid(row=5,column=0)

        btn22=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="LINKEDIN",fg="dark green",bg="light green",
                    command=linkedin,anchor="w",width=10,height=0,compound="c")
        btn22.grid(row=5,column=1)

        btn23=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="ORACLE SQL",fg="dark green",bg="light green",
                    command=oracle_sql,anchor="w",width=10,height=0,compound="c")
        btn23.grid(row=5,column=2)

        btn24=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="COVID-19",fg="dark green",bg="light green",
                    command=covid19,anchor="w",width=10,height=0,compound="c")
        btn24.grid(row=5,column=3)

        btn25=Button(f1,padx=30,pady=16,bd=8,font=("arial",15,"bold"),text="WHATSAPP",fg="dark green",bg="light green",
                    command=wtsp,anchor="w",width=10,height=0,compound="c")
        btn25.grid(row=0,column=4)
        

        

        

    #######################################################################################################################
    global ps
    ps = Toplevel(login_id)
    ps.geometry("1600x800+0+0") 
    ps.title("KS TECHNOLOGY")
    ps.configure(bg="light green")


    Tops99=Frame(ps,width = 1600,height = 50,bg='light green',relief=SUNKEN)
    Tops99.pack(side=TOP)

    f99=Frame(ps,width = 550,height = 700,bg='light green',relief=SUNKEN)
    f99.pack(side=LEFT)

    f88=Frame(ps,width = 300,height = 700,bg='light green',relief=SUNKEN)
    f88.pack(side=RIGHT)


    lblInfo=Label(Tops99,font=("arial",23,"bold"),text="CREATED BY ",fg="dark green",bg="light green",bd=10,anchor="w")
    lblInfo.pack()

    lblInfo=Label(f99,font=("arial",23,"bold"),text="KAUSHAL SETHIA ",fg="dark green",bg="light green",bd=10,anchor="center")
    lblInfo.grid(row=2,column=6)
    

    canvas = Canvas(Tops99, width=600, height=500)
    canvas.config(bg='light green')
    
    canvas.pack()

    my_image = PhotoImage(file='kspic.png')
    my_img = canvas.create_image(0,0, anchor=NW, image=my_image)
   

    btn99=Button(f88,padx=16,pady=16,bd=8,fg="dark green",font=("arial",15,"bold"),text="NEXT",bg="light green",
                command=start,anchor="w",width=10,height=0,compound="c")
    btn99.pack()

    ps.mainloop()  



    

    


    
############################################################################################################################

    



login_id.mainloop()


###########################################################################################################################
