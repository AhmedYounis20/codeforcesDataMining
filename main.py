########################################################################
# search sction:
#   main button ===> search_Button
#        search_Button goes to frame1
#    search section has : F,   go_BUTTON, getting_handle, choosen_frame
#   go_Button goes to search_result :
#   it has 7 fram
#
#
#
#
#
#
from tkinter import *
import webbrowser
from  urllib.request import urlopen
from urllib.error import URLError,HTTPError
from json import loads
import requests
import shutil
from PIL import ImageTk,Image
from tkscrolledframe import ScrolledFrame
from mylib import get_all
from os import system
#####################################################(search class) #################################
'''class get_all: 
    def __init__(self,handle):
        self.handle= handle
        self.info_url = "https://codeforces.com/api/user.info?handles="+str(handle)
        self.status_url="https://codeforces.com/api/user.status?handle=amy2532001"+str(handle)
        self.contests_url='https://codeforces.com/api/user.rating?handle=' +str(handle)
    infofile=loads(urlopen(info_url))
    def get_info(self):
'''


######################################################(functions)#######################################################################
def search_result( handle ):##### pop up of search window
    #url = "https://userpic.codeforces.com/591099/avatar/e5d251220ca54303.jpg"
    try :
        account=get_all(handle)
        res_file = Toplevel()
        res_file.geometry("520x700")
        res_sf = ScrolledFrame(res_file, width=500, height=700, bg="#231e1e", scrollbars="vertical", )
        res_sf.pack(expand=1, fill="y", )
        res_sf.bind_arrow_keys(res_file)
        res_sf.bind_scroll_wheel(res_file)
        inner_frame = res_sf.display_widget(Frame)  ## main window
        inner_frame.config(background="black", )
        ##############################################################################
        info_fr = Frame(inner_frame, height=350, width=490, background="#231e1e")
        account.get_info()
        
        downloaded_avatar = requests.get(account.image, stream=True,headers={'User-agent': 'Mozilla/5.0'})
        if downloaded_avatar.status_code == 200:
            with open(account.image.split('/')[-1], 'wb') as f:
                downloaded_avatar.raw.decode_content = True
                shutil.copyfileobj(downloaded_avatar.raw, f)
        image=ImageTk.PhotoImage(size=20,image=Image.open(account.image.split('/')[-1]))
        # l = Button(info_fr,image=image).place(rely=0)
        picture= Label(info_fr, image=image).place(rely=0.25,relx=0.05)
        system("del /f "+str(account.image.split('/')[-1]))
        account_name=Label(info_fr,text="name: "+str(account.name)).place(rely=0.05, relx=0.3)
        country=Label(info_fr,text="country: "+(str(account.country))).place(rely=0.15, relx=0.3)
        city=Label(info_fr,text="city: "+(str(account.city))).place(rely=0.25, relx=0.3)
        organization=Label(info_fr,text="Organization: "+(str(account.Organization))).place(rely=0.35, relx=0.3)
        friends=Label(info_fr,text="friend of: "+(str(account.friends))).place(rely=0.45, relx=0.3)
        rank=Label(info_fr,text="Rank: "+(str(account.Rank))).place(rely=0.55, relx=0.3)
        rating=Label(info_fr,text="Rating: "+(str(account.Rating))).place(rely=0.65, relx=0.3)
        register=Label(info_fr,text="registered: "+(str(account.registered))).place(rely=0.75, relx=0.3)
        info_fr.pack(pady=1)
        ###############################################################################
        account.get_problem()
        languages_fr=Frame(inner_frame,height=30*len(account.languages)+20, width=490, background="#231e1e")
        i=3
        Label(languages_fr,text="languages:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0,relx=0)
        for language in account.languages:
            Label(languages_fr,text=str(language)+":"+str(account.languages[language]), fg='white', bg="#231e1e").place(relx=0.1,rely=0.5/len(account.languages)*i)
            i+=1
        languages_fr.pack(pady=1)
        ##############################################
        vlen=50*len(account.verdict)+10
        verdicts_fr=Frame(inner_frame,height=vlen, width=490, background="#231e1e")
        i=3
        Label(verdicts_fr,text="verdicts:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0,relx=0)
        for verdict in account.verdict:
            if  verdict == "OK": Label(verdicts_fr, text="accepted" + ":" + str(account.verdict["OK"]),fg='white', bg="#231e1e").place(relx=0.1, rely=0.3/len(account.verdict)*i)
            if verdict != "OK":
                Label(verdicts_fr,text=str(verdict)+":"+str(account.verdict[verdict]),fg='white', bg="#231e1e").place(relx=0.1,rely=0.3/len(account.verdict)*i)
            i+=2
        verdicts_fr.pack(pady=1)
        #################################################
        llen=50*len(account.solved_level)+10
        levels_fr=Frame(inner_frame,height=llen, width=490, background="#231e1e")
        i=5
        Label(levels_fr,text="levels:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0,relx=0)
        for level in account.solved_level:
            Label(levels_fr, fg='white', bg="#231e1e",text=str(level)+":"+str(account.solved_level[level])).place(relx=0.1,rely=0.3/(len(account.solved_level))*i)
            i+=2
        levels_fr.pack(pady=1)
        #####################################################
        t_height = 100 * len(account.solved_tages)/6
        tags_fr = Frame(inner_frame, width=490, height=t_height, bg="#231e1e", )
        t = Label(tags_fr, text="tags:", font=('arial', 20), fg='red', bg="#231e1e").place(rely=0.0, relx=0)
        i = 2
        j = 0
        for tag in account.solved_tages:
            Label(tags_fr, text=str(tag), bg='#2' + str(i * j + 10) + 'e1e', fg='#F' + str(i * j + 10) + 'e1e').place(rely=(1.5/len(account.solved_tages)) * i, relx=0.5 * j)
            if j < 1:
                j += 1
            else:
                j = 0
                i += 1
        tags_fr.pack(pady=1)
        ######################################################
        extras_fr=Frame(inner_frame,height=350, width=490, background="#231e1e")
        account.get_contest()
        t = Label(extras_fr, text="Extra:", font=('arial', 20), fg='red', bg="#231e1e").place(rely=0.0, relx=0)
        Label(extras_fr,text='tryed: '+str(account.tryed_problem) ,fg='white', bg="#231e1e").place(rely=0.15)
        Label(extras_fr, fg='white', bg="#231e1e",text='solved problems: '+str(account.tryed_problem-len(account.unsolved_problem))).place(rely=0.25)

        Label(extras_fr, fg='white', bg="#231e1e",text='nomber of contests: '+str(account.number_of_contests)).place(rely=0.35)
        Label(extras_fr, fg='white', bg="#231e1e",text='Best rank: '+str(account.Best_Rank)).place(rely=0.45)
        Label(extras_fr, fg='white', bg="#231e1e",text='worst rank: '+str(account.worst_Rank)).place(rely=0.55)
        Label(extras_fr, fg='white', bg="#231e1e",text='max up: '+str(account.max_up)).place(rely=0.65)
        Label(extras_fr, fg='white', bg="#231e1e",text='max down: '+str(account.max_down)).place(rely=0.75)
        extras_fr.pack(pady=1)
        ##############################################
        unslen = 30 * (len(account.unsolved_problem) + 1) / 2 + 100

        unsolved_fr=Frame(inner_frame,width=490,height=unslen,background="#231e1e")
        i=5
        def serach_problem(index,contestid):
            webbrowser.open("http://codeforces.com/problemset/problem/"+str(contestid)+'/'+str(index))
        j=0
        unstext = Label(unsolved_fr, text="unsolved practice problems:", font=('arial', 20)).place(rely=0, relx=0)
        print(len(account.unsolved_problem))
        for problem in account.unsolved_problem:
            Button(unsolved_fr,bg='brown',text=str(problem['index'])+'-'+str(problem['contestId']),command=lambda:serach_problem(problem['index'],problem['contestId'])).place(rely=0.05*i,relx=0.5*j)
            if j==1:
                j=-1
            if j==-1:
                i+=3

            j+=1

        unsolved_fr.pack(pady=1)
        # image = wget.download("http:"+str(account.image))
        # image=ImageTk.PhotoImage(Image.open(account.image.split('/')[-1]))
        # cann = Label(fr, width=20, height=10, borderwidth=0, highlightthickness=0, relief='ridge', text='hi', bg='white')
        # cann.pack()
        # cann.place(relx=0.01, rely=0.2)
        # system("rm "+account.image.split('/')[-1])
        # can = Canvas(inner_frame,bg='black')
        # can.create_window(0, 0, anchor=NW, window=fr)
        # can.pack(pady=0, padx=0)

        # can.pack()
        res_file.mainloop()
        # inner_frame.
        ###############################################################
       # get_all(handle)

    except HTTPError :
        warnning=Tk()
        warnning.geometry("300x100")
        warnning.title('warnning')
        warnning.configure(bg="pink")
        warnning.iconbitmap('error.ico')
        l=Label(warnning,text="not valid handle ",font=('arial',20),fg='red',bg="pink").pack()
        warnning.mainloop()
    except URLError:
        warnning = Tk()
        warnning.geometry("300x100")
        warnning.configure(bg="gray")
        warnning.iconbitmap('error.ico')
        warnning.title('warnning')
        l = Label(warnning,text="please check internet",font=('arial',20),fg='red',bg='gray').pack()
        warnning.mainloop()
    return account
####################
def compare_result(handle1,handle2):
    #url = "https://userpic.codeforces.com/591099/avatar/e5d251220ca54303.jpg"
    try:
        account1=get_all(handle1)
        account1.get_info()
        account2=get_all(handle2)
        account2.get_info()
        compare_window = Toplevel()
        compare_window.geometry("810x700")
        compare_scroll = ScrolledFrame(compare_window, width=800, height=700, bg="#231e1e", scrollbars="vertical", )
        compare_scroll.pack(expand=1, fill="y", )
        compare_scroll.bind_arrow_keys(compare_window)
        compare_scroll.bind_scroll_wheel(compare_window)
        inner_compare_frame = compare_scroll.display_widget(Frame)  ## main window
        inner_compare_frame.config(background="black", )
        ##############################################              1           ###########################################################
        info1_fr=Frame(inner_compare_frame,width=390,height=250,bg="#231e1e",)
        downloaded_avatar = requests.get(account1.image, stream=True,headers={'User-agent': 'Mozilla/5.0'})
        if downloaded_avatar.status_code == 200:
            with open(account1.image.split('/')[-1], 'wb') as f:
                downloaded_avatar.raw.decode_content = True
                shutil.copyfileobj(downloaded_avatar.raw, f)        
        image = ImageTk.PhotoImage(size=20, image=Image.open(account1.image.split('/')[-1]))
        # l = Button(info1_fr,image=image).place(rely=0)
        picture = Label(info1_fr, image=image).place(rely=0.25,relx=0.05)
        system("del /f " + str(account1.image.split('/')[-1]))
        account_name = Label(info1_fr, text="name: " + str(account1.name)).place(rely=0.05, relx=0.3)
        country = Label(info1_fr, text="country: " + (str(account1.country))).place(rely=0.15, relx=0.3)
        city = Label(info1_fr, text="city: " + (str(account1.city))).place(rely=0.25, relx=0.3)
        organization = Label(info1_fr, text="Organization: ").place(rely=0.35, relx=0.3)
        orgnization_info=Label(info1_fr,text=(str(account1.Organization))).place(rely=0.45,relx=0.38)
        friends = Label(info1_fr, text="friend of: " + (str(account1.friends))).place(rely=0.55, relx=0.3)
        rank = Label(info1_fr, text="Rank: " + (str(account1.Rank))).place(rely=0.65, relx=0.3)
        rating = Label(info1_fr, text="Rating: " + (str(account1.Rating))).place(rely=0.75, relx=0.3)
        register = Label(info1_fr, text="registered: " + (str(account1.registered))).place(rely=0.85, relx=0.3)
        info1_fr.grid(column=0,row=0,pady=1,padx=1)
                                        ####################2#################
        info2_fr=Frame(inner_compare_frame,width=390,height=250,bg="#231e1e",)
        downloaded_avatar = requests.get(account2.image, stream=True,headers={'User-agent': 'Mozilla/5.0'})
        if downloaded_avatar.status_code == 200:
            with open(account2.image.split('/')[-1], 'wb') as f:
                downloaded_avatar.raw.decode_content = True
                shutil.copyfileobj(downloaded_avatar.raw, f)        
        image2= ImageTk.PhotoImage(size=20, image=Image.open(account2.image.split('/')[-1]))
        # l = Button(info2_fr,image=image).place(rely=0)
        picture = Label(info2_fr, image=image2).place(rely=0.25,relx=0.05)
        system("del /f " + str(account2.image.split('/')[-1]))
        account_name = Label(info2_fr, text="name: " + str(account2.name)).place(rely=0.05, relx=0.3)
        country = Label(info2_fr, text="country: " + (str(account2.country))).place(rely=0.15, relx=0.3)
        city = Label(info2_fr, text="city: " + (str(account2.city))).place(rely=0.25, relx=0.3)
        organization = Label(info2_fr, text="Organization: ").place(rely=0.35, relx=0.3)
        organization_info=Label(info2_fr,text= (str(account2.Organization))).place(rely=0.45,relx=0.38)
        friends = Label(info2_fr, text="friend of: " + (str(account2.friends))).place(rely=0.55, relx=0.3)
        rank = Label(info2_fr, text="Rank: " + (str(account2.Rank))).place(rely=0.65, relx=0.3)
        rating = Label(info2_fr, text="Rating: " + (str(account2.Rating))).place(rely=0.75, relx=0.3)
        register = Label(info2_fr, text="registered: " + (str(account2.registered))).place(rely=0.85, relx=0.3)

        info2_fr.grid(column=1,row=0,pady=1,padx=1)
        ####################################################################################################################
        account1.get_problem()
        account2.get_problem()
        languages1_fr=Frame(inner_compare_frame,width=390,height=30*max(len(account2.languages),len(account1.languages))+80,bg="#231e1e",)
        v=Label(languages1_fr,text="languages:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)

        i = 4
        for language in account1.languages:
            Label(languages1_fr, text=str(language) + ":    " + str(account1.languages[language]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05 * i)
            i += 2
        languages1_fr.grid(column=0,row=1,pady=1,padx=1)
                                            #######################################
        languages2_fr=Frame(inner_compare_frame,width=390,height=30*max(len(account2.languages),len(account1.languages))+80,bg="#231e1e",)
        l2=Label(languages2_fr,text="languages:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)

        i = 4
        for language in account2.languages:
            Label(languages2_fr, text=str(language) + ":" + str(account2.languages[language]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05 * i)
            i += 2
        languages2_fr.grid(column=1,row=1,pady=1,padx=1)
        ####################################################################################################################
        verdicts1_fr=Frame(inner_compare_frame,width=390,height=30*max(len(account2.verdict),len(account1.verdict))+60,bg="#231e1e",)
        v=Label(verdicts1_fr,text="verdicts:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)

        i = 3
        if "OK" in account1.verdict :Label(verdicts1_fr, text="accepted" + ":" + str(account1.verdict["OK"]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05*i)
        else :Label(verdicts1_fr, text="accepted:   0",bg='#231e1e',fg='white').place(relx=0.1, rely=0.05*i)
        i=5
        for verdict in account1.verdict:
            if verdict != "OK":
                Label(verdicts1_fr, text=str(verdict) + ":" + str(account1.verdict[verdict]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05 * i)
                i+=2
        verdicts1_fr.grid(column=0, row=2, pady=1, padx=1)
                                        ##################################################
        verdicts2_fr=Frame(inner_compare_frame,width=390,height=30*max(len(account2.verdict),len(account1.verdict))+60,bg="#231e1e",)
        v=Label(verdicts2_fr,text="verdicts:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)

        i = 3
        if "OK" in account2.verdict :Label(verdicts2_fr, text="accepted" + ":" + str(account2.verdict["OK"]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05*i)
        else :Label(verdicts2_fr, text="accepted:   0",bg='#231e1e',fg='white').place(relx=0.1, rely=0.05*i)
        i=5
        for v in account2.verdict:
            if v != "OK":
                Label(verdicts2_fr, text=str(v) + ":" + str(account2.verdict[v]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05 * i)
                i += 2

        verdicts2_fr.grid(column=1, row=2, pady=1, padx=1)
        ####################################################################################################################
        level1_fr=Frame(inner_compare_frame,width=390,height=60*max(len(account2.solved_level),len(account1.solved_level)),bg="#231e1e")
        l1=Label(level1_fr,text="levels:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)

        i = 4
        for level in account1.solved_level:
            Label(level1_fr, text=str(level) + ":" + str(account1.solved_level[level]),bg='#231e1e',fg='white').place(relx=0.1, rely=0.05 * i)
            i += 1
        level1_fr.grid(row=3,column=0,  pady=1, padx=1)
                                        ###############################################
        level2_fr=Frame(inner_compare_frame,width=390,height=60*max(len(account2.solved_level),len(account1.solved_level)),bg="#231e1e",)
        l2=Label(level2_fr,text="levels:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)
        i = 3
        for level in account2.solved_level:
            Label(level2_fr, text=str(level) + ":" + str(account2.solved_level[level]),bg='#231e1e',fg='white').place(relx=0.1, y=20*i)
            i += 1
        level2_fr.grid(row=3,column=1,  pady=1, padx=1)
        ####################################################################################################################
        account1.get_problem()
        account2.get_problem()
        t_height=100*max(len(account2.solved_tages),len(account1.solved_tages))/6
        tags1_fr=Frame(inner_compare_frame,width=390,height=t_height,bg="#231e1e",)
        t=Label(tags1_fr,text="tags:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)
        i = 3
        j = 0
        for tag in account1.solved_tages:
            Label(tags1_fr, text=str(tag),bg='#2'+str(i*j+10)+'e1e',fg='#F'+str(i*j+10)+'e1e').place(y=(0.02/300)*h*i*400,x=0.5*j*400)
            if j < 1:
                j+=1
            else :
                j=0
                i+=1
        tags1_fr.grid(row=4,column=0,  pady=1, padx=1)
                                    ################################################

        tags2_fr=Frame(inner_compare_frame,width=390,height=t_height,bg="#231e1e",)
        t=Label(tags2_fr,text="tags:",font=('arial',20),fg='red',bg="#231e1e").place(rely=0.0,relx=0)
        #t1=Frame(tags2_fr,bg='#231e1e')
        i = 3
        j=0
        for tag in account2.solved_tages:
            Label(tags2_fr, text=str(tag),bg='#2'+str(i*j+10)+'e1e',fg='#F'+str(i*j+10)+'e1e').place(y=(0.02/300)*h*i*400,x=0.5*j*400)
            if j < 1:
                j+=1
            else :
                j=0
                i+=1
        #t1.pack()
        tags2_fr.grid(row=4,column=1,  pady=1, padx=1)
        ####################################################################################################################
        extras1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
        account1.get_contest()
        Label(extras1_fr, text='tryed: ' + str(account1.tryed_problem),fg='red',bg="#231e1e").place(rely=0.05)
        Label(extras1_fr, text='solved problems: ' + str(account1.tryed_problem - len(account1.unsolved_problem)),fg='red',bg="#231e1e").place(rely=0.15)
        Label(extras1_fr, text='nomber of contests: ' + str(account1.number_of_contests),fg='red',bg="#231e1e").place(rely=0.25)
        Label(extras1_fr, text='Best rank: ' + str(account1.Best_Rank),fg='red',bg="#231e1e").place(rely=0.35)
        Label(extras1_fr, text='worst rank: ' + str(account1.worst_Rank),fg='red',bg="#231e1e").place(rely=0.45)
        Label(extras1_fr, text='max up: ' + str(account1.max_up),fg='red',bg="#231e1e").place(rely=0.55)
        Label(extras1_fr, text='max down: ' + str(account1.max_down),fg='red',bg="#231e1e").place(rely=0.65)
        extras1_fr.grid(row=5,column=0,  pady=1, padx=1)
                                            ############################################
        extras2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
        account2.get_contest()
        Label(extras2_fr, text='tryed: ' + str(account2.tryed_problem),fg='red',bg="#231e1e").place(rely=0.05)
        Label(extras2_fr, text='solved problems: ' + str(account2.tryed_problem - len(account2.unsolved_problem)),fg='red',bg="#231e1e").place(rely=0.15)
        Label(extras2_fr, text='nomber of contests: ' + str(account2.number_of_contests),fg='red',bg="#231e1e").place(rely=0.25)
        Label(extras2_fr, text='Best rank: ' + str(account2.Best_Rank),fg='red',bg="#231e1e").place(rely=0.35)
        Label(extras2_fr, text='worst rank: ' + str(account2.worst_Rank),fg='red',bg="#231e1e").place(rely=0.45)
        Label(extras2_fr, text='max up: ' + str(account2.max_up),fg='red',bg="#231e1e").place(rely=0.55)
        Label(extras2_fr, text='max down: ' + str(abs(account2.max_down)),fg='red',bg="#231e1e").place(rely=0.65)
        extras2_fr.grid(row=5,column=1,  pady=1, padx=1)
        ####################################################################################################################
        unsolved1_fr=Frame(inner_compare_frame,width=390,height=30*max(len(account1.unsolved_problem),len(account2.unsolved_problem))/1.5+40,bg="#231e1e",)
        i = 4
        def serach_problem(index, contestid):
            webbrowser.open("http://codeforces.com/problemset/problem/" + str(contestid) + '/' + str(index))

        un1= Label(unsolved1_fr, text='unsolved:', font=('arial',20),bg="#231e1e",fg='red' ).place(rely=0.0,relx=0)
        j=0
        for problem in account1.unsolved_problem:
            Button(unsolved1_fr,bg='brown',text=str(problem['index'])+'-'+str(problem['contestId']),command=lambda:serach_problem(problem['index'],problem['contestId'])).place(rely=0.05*i,relx=0.5*j)
            if j==1:
                j=-1
            if j==-1:   
                i+=3

            j+=1
        unsolved1_fr.grid(row=6,column=0,  pady=1, padx=1)
                                                ####################################
        unsolved2_fr=Frame(inner_compare_frame,width=390,height=30*max(len(account1.unsolved_problem),len(account2.unsolved_problem))/1.5+40,bg="#231e1e",)
        i = 4
        def serach_problem(index, contestid):
            webbrowser.open("http://codeforces.com/problemset/problem/" + str(contestid) + '/' + str(index))
        un2= Label(unsolved2_fr, text='unsolved:', font=('arial',20),bg="#231e1e",fg='red' ).place(rely=0.0,relx=0)
        j=0
        for problem in account2.unsolved_problem:
            Button(unsolved2_fr,bg='brown',text=str(problem['index'])+'-'+str(problem['contestId']),command=lambda:serach_problem(problem['index'],problem['contestId'])).place(rely=0.05*i,relx=0.5*j)
            if j==1:
                j=-1
            if j==-1:
                i+=3

            j+=1
        unsolved2_fr.grid(row=6,column=1,  pady=1, padx=1)

        compare_window.mainloop()
    except HTTPError:
        warnning = Tk()
        warnning.geometry("300x100")
        warnning.title('warnning')
        warnning.configure(bg="pink")
        warnning.iconbitmap('error.ico')
        l = Label(warnning, text="not valid handle ", font=('arial', 20), fg='red', bg="pink").pack()
        warnning.mainloop()
    except URLError:
        warnning = Tk()
        warnning.geometry("300x100")
        warnning.configure(bg="gray")
        warnning.iconbitmap('error.ico')
        warnning.title('warnning')
        l = Label(warnning, text="please check internet", font=('arial', 20), fg='red', bg='gray').pack()
        warnning.mainloop()
########################################################################################################################
def weekly_rateing(handle_for_rate):
    try:
        phase=get_all(handle_for_rate)
        phase.get_problem()
        phase.get_probelms_for_phase()
        def search_max_problem(id,level):
            webbrowser.open("http://codeforces.com/problemset/problem/"+level+'/'+str(id))
        weekly_window = Toplevel()
        weekly_window.geometry("505x700")
        weekly_window.title('weekly raiting')
        week_scroll = ScrolledFrame(weekly_window, width=494, height=700, bg="#231e1e", scrollbars="vertical", )
        week_scroll.pack(expand=1, fill="y", )
        week_scroll.bind_arrow_keys(weekly_window)
        week_scroll.bind_scroll_wheel(weekly_window)
        inner_week_frame = week_scroll.display_widget(Frame)  ## main window
        inner_week_frame.config(background="black", )
                                ##############################################
        info_fr = Frame(inner_week_frame, height=350, width=490, background="#231e1e")
        phase.get_info()
        downloaded_avatar = requests.get(phase.image, stream=True,headers={'User-agent': 'Mozilla/5.0'})
        if downloaded_avatar.status_code == 200:
            with open(phase.image.split('/')[-1], 'wb') as f:
                downloaded_avatar.raw.decode_content = True
                shutil.copyfileobj(downloaded_avatar.raw, f)  
        image = ImageTk.PhotoImage(size=20, image=Image.open(phase.image.split('/')[-1]))
        # l = Button(info_fr,image=image).place(rely=0)
        picture = Label(info_fr, image=image).place(rely=0.25, relx=0.05)
        system("del /f " + str(phase.image.split('/')[-1]))
        account_name = Label(info_fr, text="name: " + str(phase.name)).place(rely=0.05, relx=0.3)
        country = Label(info_fr, text="country: " + (str(phase.country))).place(rely=0.15, relx=0.3)
        city = Label(info_fr, text="city: " + (str(phase.city))).place(rely=0.25, relx=0.3)
        organization = Label(info_fr, text="Organization: " + (str(phase.Organization))).place(rely=0.35, relx=0.3)
        friends = Label(info_fr, text="friend of: " + (str(phase.friends))).place(rely=0.45, relx=0.3)
        rank = Label(info_fr, text="Rank: " + (str(phase.Rank))).place(rely=0.55, relx=0.3)
        rating = Label(info_fr, text="Rating: " + (str(phase.Rating))).place(rely=0.65, relx=0.3)
        register = Label(info_fr, text="registered: " + (str(phase.registered))).place(rely=0.75, relx=0.3)
        info_fr.pack(pady=1)
        info_fr.pack(pady=1)
        phase.phase1_info()
        phase1_fr = Frame(inner_week_frame, width=490, height=300, bg="#231e1e", )
        cur1=Label(phase1_fr,text="Phase1:",font=('arial',30),bg='#231e1e',fg='red').place(relx=0,rely=0.05)

        solved1=Label(phase1_fr,text="problems solved: "+str(len(phase.phase1_solved)), bg="#231e1e").place(relx=0,rely=0.22)
        submittions1=Label(phase1_fr,text="Submitions: "+str(phase.phase1_submitions), bg="#231e1e").place(relx=0,rely=0.32)
        mxrated1=Label(phase1_fr,text="Matx Rate Problem: "+str(phase.phase1_max_rated_problem), bg="#231e1e").place(relx=0,rely=0.42)
        av1=Label(phase1_fr,text="problems Average Rate : "+str(phase.phase1_av), bg="#231e1e").place(relx=0,rely=0.52)
        const1=Label(phase1_fr,text="contests Participation: "+str(phase.phase1_contestcount), bg="#231e1e").place(relx=0,rely=0.62)
        vir1=Label(phase1_fr,text="virtual participation: "+str(phase.phase1_virtual_count), bg="#231e1e").place(relx=0,rely=0.72)

        phase1_fr.pack(pady=1)


        #######################################################################################
        phase.phase2_info()
        phase2_fr = Frame(inner_week_frame, width=490, height=300, bg="#231e1e", )
        cur2=Label(phase2_fr,text="Phase2:",font=('arial',30),bg='#231e1e',fg='red').place(relx=0,rely=0.05)

        solved2=Label(phase2_fr,text="problems solved: "+str(len(phase.phase2_solved)), bg="#231e1e").place(relx=0,rely=0.22)
        submittions2=Label(phase2_fr,text="Submitions: "+str(phase.phase2_submitions), bg="#231e1e").place(relx=0,rely=0.32)
        mxrated2=Label(phase2_fr,text="Matx Rate Problem: "+str(phase.phase2_max_rated_problem), bg="#231e1e").place(relx=0,rely=0.42)
        av2=Label(phase2_fr,text="problems Average Rate : "+str(phase.phase2_av), bg="#231e1e").place(relx=0,rely=0.52)
        conts2=Label(phase2_fr,text="contests Participation: "+str(phase.phase2_contestcount), bg="#231e1e").place(relx=0,rely=0.62)
        vir2=Label(phase2_fr,text="virtual participation: "+str(phase.phase2_virtual_count), bg="#231e1e").place(relx=0,rely=0.72)

        phase2_fr.pack(pady=1)

        ###############################################

        phase.phase3_info()
        phase3_fr = Frame(inner_week_frame, width=490, height=300, bg="#231e1e" )
        cur3=Label(phase3_fr,text="Phase3:",font=('arial',30),bg='#231e1e',fg='red').place(relx=0,rely=0.05)
        solved3=Label(phase3_fr,text="problems solved: "+str(len(phase.phase3_solved)),bg='#231e1e').place(relx=0,rely=0.22)
        submittions3=Label(phase3_fr,text="Submitions: "+str(phase.phase3_submitions),bg='#231e1e').place(relx=0,rely=0.32)
        mxrated3=Label(phase3_fr,text="Matx Rate Problem: "+str(phase.phase3_max_rated_problem),bg='#231e1e').place(relx=0,rely=0.42)
        av3=Label(phase3_fr,text="problems Average Rate : "+str(phase.phase3_av),bg='#231e1e').place(relx=0,rely=0.52)
        const3=Label(phase3_fr,text="contests Participation: "+str(phase.phase3_contestcount),bg='#231e1e').place(relx=0,rely=0.62)
        vir3=Label(phase3_fr,text="virtual participation: "+str(phase.phase3_virtual_count),bg='#231e1e').place(relx=0,rely=0.72)

        phase3_fr.pack(pady=1)

        weekly_window.mainloop()
    except HTTPError:
        warnning = Tk()
        warnning.geometry("300x100")
        warnning.title('warnning')
        warnning.configure(bg="pink")
        warnning.iconbitmap('error.ico')
        l = Label(warnning, text="not valid handle ", font=('arial', 20), fg='red', bg="pink").pack()
        warnning.mainloop()
    except URLError:
        warnning = Tk()
        warnning.geometry("300x100")
        warnning.configure(bg="gray")
        warnning.iconbitmap('error.ico')
        warnning.title('warnning')
        l = Label(warnning, text="please check internet", font=('arial', 20), fg='red', bg='gray').pack()
        warnning.mainloop()

def frame1():
    rootHeight = w.winfo_height()
    F=Frame(w,bg='#231e1e',width=850,height=640)
    getting_handle=Entry(F,width=40,bg="brown",font=("Calibri",16),)
    getting_handle.pack()
    getting_handle.place(relx=0.25,rely=0.15,height=25)
    def go_search():
        search_result(getting_handle.get())
    go_BUTTON=Button(F,text='GO',width=30,height=5,bg='brown',command=go_search)
    go_BUTTON.pack()
    go_BUTTON.place(relx=0.4,rely=0.4)
    F.pack(expand=1,fill='y')
    F.place(relx=0,rely=0)
    choosen_frame=Frame(F,width=230,height=5,bg="red").place(rely=0.99,relx=0.379)
def frame2():





    F2=Frame(w,bg='#231e1e',width=850,height=640)
    getting_handle1 = Entry(F2, width=40, bg="brown", font=("Calibri", 16), )
    getting_handle1.pack()
    getting_handle1.place(relx=0.25, rely=0.15, height=25)
    getting_handle2 = Entry(F2, width=40, bg="brown", font=("Calibri", 16), )
    getting_handle2.pack()
    getting_handle2.place(relx=0.25, rely=0.35, height=25)
    go_BUTTON = Button(F2, text='GO', width=30, height=5, bg='brown',command=lambda:compare_result(getting_handle1.get(),getting_handle2.get()))
    go_BUTTON.pack()
    go_BUTTON.place(relx=0.4, rely=0.4)
    F2.pack()
    F2.place(relx=0,rely=0)
    choosen_frame = Frame(F2, width=320, height=5, bg="red").place(rely=0.99,relx=0)
def frame3():
    rootHeight = w.winfo_height()
    F3=Frame(w,bg='#231e1e',width=850,height=640)
    getting_handle=Entry(F3,width=40,bg="brown",font=("Calibri",16),)
    getting_handle.pack()
    getting_handle.place(relx=0.25,rely=0.15,height=25)

    go_BUTTON=Button(F3,text='GO',width=30,height=5,bg='brown',command=lambda:weekly_rateing(getting_handle.get()))
    go_BUTTON.pack()
    go_BUTTON.place(relx=0.4,rely=0.4)
    F3.pack(expand=1,fill='y')
    F3.place(relx=0,rely=0)
    choosen_frame=Frame(F3,width=295,height=5,bg="red").place(rely=0.99,relx=0.65)

#################################################################################################################################################
if __name__=="__main__":
    #######################################################(GUI design)####################################################################
    w = Tk()
    w.title("codeforces")
    w.geometry('850x700+300+10')
    w.resizable(width=False, height=0)
    w.configure(background="#231e1e")
    h=w.winfo_screenheight()
    d=w.winfo_screenwidth()
    w.iconbitmap('code.ico')
    # img = Image("photo", file="codeforces-telegram-square.png")
    # w.tk.call('wm','iconphoto',w._w, img)
    ####################################################
    search_Button = Button(w, text="search", bg='#13120c', relief='flat', activebackground="#231e1e",border=0, fg='white',width=40, default='normal', command=frame1)
    search_Button.pack(side="bottom")
    search_Button.place(rely=0.914, relx=0.35, height=60)
    #################################
    compare_Button = Button(master=w, text="compare", width=45, bg='#13120c', activebackground="#231e1e",border=0, fg='white', relief='flat', command=frame2)
    compare_Button.pack(side="bottom")
    compare_Button.place(rely=0.914, height=60, )
    #############################################
    weekly_rate= Button(w, text="weekly rate ", width=43, bg='#13120c', activebackground="#231e1e",border=0, fg='white', relief='flat',command=frame3)
    weekly_rate.pack(side="bottom")
    weekly_rate.place(rely=0.914, relx=0.65, height=60, )
    ########################################
    w.mainloop()