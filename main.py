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
from  urllib.request import urlopen,urlretrieve
from urllib.error import URLError,HTTPError
from json import loads
import wget
from PIL import ImageTk,Image
from tkscrolledframe import ScrolledFrame
import sqlite3
from mylib import *
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
        image = wget.download("http:"+str(account.image))
        image=ImageTk.PhotoImage(size=20,image=Image.open(account.image.split('/')[-1]))
        # l = Button(info_fr,image=image).place(rely=0)
        picture= Label(info_fr, image=image).place(rely=0.3)
        system("rm "+str(account.image.split('/')[-1]))
        account_name=Label(info_fr,text="name: "+str(account.name)).place(rely=0.05,relx=0.6)
        country=Label(info_fr,text="country: "+(str(account.country))).place(rely=0.1,relx=0.6)
        city=Label(info_fr,text="city: "+(str(account.city))).place(rely=0.15,relx=0.6)
        organization=Label(info_fr,text="Organization: "+(str(account.Organization))).place(rely=0.2,relx=0.6)
        friends=Label(info_fr,text="friend of: "+(str(account.friends))).place(rely=0.25,relx=0.6)
        rank=Label(info_fr,text="Rank: "+(str(account.Rank))).place(rely=0.30,relx=0.6)
        rating=Label(info_fr,text="Rating: "+(str(account.Rating))).place(rely=0.35,relx=0.6)
        register=Label(info_fr,text="registered: "+(str(account.registered))).place(rely=0.4,relx=0.6)
        info_fr.pack(pady=1)
        ###############################################################################
        languages_fr=Frame(inner_frame,height=350, width=490, background="#231e1e")
        account.get_problem()
        i=0
        for language in account.languages:
            Label(languages_fr,text=str(language)+":"+str(account.languages[language])).place(relx=0.1,rely=0.05*i)
            i+=1
        languages_fr.pack(pady=1)
        ##############################################
        verdicts_fr=Frame(inner_frame,height=350, width=490, background="#231e1e")
        i=2
        Label(verdicts_fr, text="accepted" + ":" + str(account.verdict["OK"])).place(relx=0.1, rely=0.05)
        for verdict in account.verdict:
            if verdict != "OK":
                Label(verdicts_fr,text=str(verdict)+":"+str(account.verdict[verdict])).place(relx=0.1,rely=0.05*i)
                i+=1
        verdicts_fr.pack(pady=1)
        #################################################
        levels_fr=Frame(inner_frame,height=350, width=490, background="#231e1e")
        i=1
        for level in account.solved_level:
            Label(levels_fr,text=str(level)+":"+str(account.solved_level[level])).place(relx=0.1,rely=0.05*i)
            i+=1
        levels_fr.pack(pady=1)
        #####################################################
        tags_fr=Frame(inner_frame,height=350, width=490, background="#231e1e")
        account.get_problem()
        i=1
        for tag in account.solved_tages:
            Label(tags_fr,text=str(tag)).place(relx=0.1,rely=0.05*i)
            i+=1
        tags_fr.pack(pady=1)
        ######################################################
        extras_fr=Frame(inner_frame,height=350, width=490, background="#231e1e")
        account.get_contest()
        Label(extras_fr,text='tryed: '+str(account.tryed_problem)).place(rely=0.05)
        Label(extras_fr,text='solved problems: '+str(account.tryed_problem-len(account.unsolved_problem))).place(rely=0.1)

        Label(extras_fr,text='nomber of contests: '+str(account.number_of_contests)).place(rely=0.15)
        Label(extras_fr,text='Best rank: '+str(account.Best_Rank)).place(rely=0.2)
        Label(extras_fr,text='worst rank: '+str(account.worst_Rank)).place(rely=0.25)
        Label(extras_fr,text='max up: '+str(account.max_up)).place(rely=0.3)
        Label(extras_fr,text='max down: '+str(account.max_down)).place(rely=0.35)
        extras_fr.pack(pady=1)
        ##############################################
        unsolved_fr=Frame(inner_frame,width=490,height=300,background="#231e1e")
        i=1
        def serach_problem(index,contestid):
            webbrowser.open("http://codeforces.com/problemset/problem/"+str(contestid)+'/'+str(index))
        for problem in account.unsolved_problem:
            print(problem)
            Button(unsolved_fr,text=str(problem['index'])+'-'+str(problem['contestId']),command=lambda:serach_problem(problem['index'],problem['contestId'])).place(rely=0.1*i)
            i+=1
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
        l=Label(warnning,text="not valid handle ").pack()
        warnning.mainloop()
    except URLError:
        warnning = Tk()
        warnning.geometry("300x100")
        l = Label(warnning,text="no internet").pack()
        warnning.mainloop()
####################
def compare_result(handle1,handle2):
    #url = "https://userpic.codeforces.com/591099/avatar/e5d251220ca54303.jpg"

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
    #########################################################################################################
    info1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    image = wget.download("http:" + str(account1.image))
    image = ImageTk.PhotoImage(size=20, image=Image.open(account1.image.split('/')[-1]))
    # l = Button(info1_fr,image=image).place(rely=0)
    picture = Label(info1_fr, image=image).place(rely=0.3)
    system("rm " + str(account1.image.split('/')[-1]))
    account_name = Label(info1_fr, text="name: " + str(account1.name)).place(rely=0.05, relx=0.6)
    country = Label(info1_fr, text="country: " + (str(account1.country))).place(rely=0.1, relx=0.6)
    city = Label(info1_fr, text="city: " + (str(account1.city))).place(rely=0.15, relx=0.6)
    organization = Label(info1_fr, text="Organization: " + (str(account1.Organization))).place(rely=0.2, relx=0.6)
    friends = Label(info1_fr, text="friend of: " + (str(account1.friends))).place(rely=0.25, relx=0.6)
    rank = Label(info1_fr, text="Rank: " + (str(account1.Rank))).place(rely=0.30, relx=0.6)
    rating = Label(info1_fr, text="Rating: " + (str(account1.Rating))).place(rely=0.35, relx=0.6)
    register = Label(info1_fr, text="registered: " + (str(account1.registered))).place(rely=0.4, relx=0.6)
    info1_fr.grid(column=0,row=0,pady=1,padx=1)
                                    #####################################
    info2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    image2 = wget.download("http:" + str(account2.image))
    image2= ImageTk.PhotoImage(size=20, image=Image.open(account2.image.split('/')[-1]))
    # l = Button(info2_fr,image=image).place(rely=0)
    picture = Label(info2_fr, image=image2).place(rely=0.3)
    system("rm " + str(account2.image.split('/')[-1]))
    account_name = Label(info2_fr, text="name: " + str(account2.name)).place(rely=0.05, relx=0.6)
    country = Label(info2_fr, text="country: " + (str(account2.country))).place(rely=0.1, relx=0.6)
    city = Label(info2_fr, text="city: " + (str(account2.city))).place(rely=0.15, relx=0.6)
    organization = Label(info2_fr, text="Organization: " + (str(account2.Organization))).place(rely=0.2, relx=0.6)
    friends = Label(info2_fr, text="friend of: " + (str(account2.friends))).place(rely=0.25, relx=0.6)
    rank = Label(info2_fr, text="Rank: " + (str(account2.Rank))).place(rely=0.30, relx=0.6)
    rating = Label(info2_fr, text="Rating: " + (str(account2.Rating))).place(rely=0.35, relx=0.6)
    register = Label(info2_fr, text="registered: " + (str(account2.registered))).place(rely=0.4, relx=0.6)

    info2_fr.grid(column=1,row=0,pady=1,padx=1)
    ####################################################################################################################
    languages1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    account1.get_problem()
    account2.get_problem()
    i = 1
    for language in account1.languages:
        Label(languages1_fr, text=str(language) + ":" + str(account1.languages[language])).place(relx=0.1, rely=0.05 * i)
        i += 1
    languages1_fr.grid(column=0,row=1,pady=1,padx=1)
                                        #######################################
    languages2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    i = 1
    for language in account2.languages:
        Label(languages2_fr, text=str(language) + ":" + str(account2.languages[language])).place(relx=0.1, rely=0.05 * i)
        i += 1
    languages2_fr.grid(column=1,row=1,pady=1,padx=1)
    ####################################################################################################################
    verdicts1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    i = 2
    Label(verdicts1_fr, text="accepted" + ":" + str(account1.verdict["OK"])).place(relx=0.1, rely=0.05)
    for verdict in account1.verdict:
        if verdict != "OK":
            Label(verdicts1_fr, text=str(verdict) + ":" + str(account1.verdict[verdict])).place(relx=0.1, rely=0.05 * i)
            i += 1
    verdicts1_fr.grid(column=0, row=2, pady=1, padx=1)
                                    ##################################################
    verdicts2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    i = 2
    Label(verdicts2_fr, text="accepted" + ":" + str(account2.verdict["OK"])).place(relx=0.1, rely=0.05)
    for verdict in account1.verdict:
        if verdict != "OK":
            Label(verdicts2_fr, text=str(verdict) + ":" + str(account2.verdict[verdict])).place(relx=0.1, rely=0.05 * i)
            i += 1
    verdicts2_fr.grid(column=1, row=2, pady=1, padx=1)
    ####################################################################################################################
    level1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    i = 1
    for level in account1.solved_level:
        Label(level1_fr, text=str(level) + ":" + str(account1.solved_level[level])).place(relx=0.1, rely=0.05 * i)
        i += 1
    level1_fr.grid(row=3,column=0,  pady=1, padx=1)
                                    ###############################################
    level2_fr=Frame(inner_compare_frame,width=390,height=200,bg="#231e1e",)
    i = 1
    for level in account2.solved_level:
        Label(level2_fr, text=str(level) + ":" + str(account2.solved_level[level])).place(relx=0.1, rely=0.05 * i)
        i += 1
    level2_fr.grid(row=3,column=1,  pady=1, padx=1)
    ####################################################################################################################
    tags1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    account1.get_problem()
    i = 1
    for tag in account1.solved_tages:
        Label(tags1_fr, text=str(tag)).place(relx=0.1, rely=0.05 * i)
        i += 1
    tags1_fr.grid(row=4,column=0,  pady=1, padx=1)
                                ################################################
    tags2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    account2.get_problem()
    i = 1
    for tag in account2.solved_tages:
        Label(tags2_fr, text=str(tag)).place(relx=0.1, rely=0.05 * i)
        i += 1
    tags2_fr.grid(row=4,column=1,  pady=1, padx=1)
    ####################################################################################################################
    extras1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    account1.get_contest()
    Label(extras1_fr, text='tryed: ' + str(account1.tryed_problem)).place(rely=0.05)
    Label(extras1_fr, text='solved problems: ' + str(account1.tryed_problem - len(account1.unsolved_problem))).place(rely=0.1)
    Label(extras1_fr, text='nomber of contests: ' + str(account1.number_of_contests)).place(rely=0.15)
    Label(extras1_fr, text='Best rank: ' + str(account1.Best_Rank)).place(rely=0.2)
    Label(extras1_fr, text='worst rank: ' + str(account1.worst_Rank)).place(rely=0.25)
    Label(extras1_fr, text='max up: ' + str(account1.max_up)).place(rely=0.3)
    Label(extras1_fr, text='max down: ' + str(account1.max_down)).place(rely=0.35)
    extras1_fr.grid(row=5,column=0,  pady=1, padx=1)
                                        ############################################
    extras2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    account2.get_contest()
    Label(extras2_fr, text='tryed: ' + str(account2.tryed_problem)).place(rely=0.05)
    Label(extras2_fr, text='solved problems: ' + str(account2.tryed_problem - len(account2.unsolved_problem))).place(rely=0.1)
    Label(extras2_fr, text='nomber of contests: ' + str(account2.number_of_contests)).place(rely=0.15)
    Label(extras2_fr, text='Best rank: ' + str(account2.Best_Rank)).place(rely=0.2)
    Label(extras2_fr, text='worst rank: ' + str(account2.worst_Rank)).place(rely=0.25)
    Label(extras2_fr, text='max up: ' + str(account2.max_up)).place(rely=0.3)
    Label(extras2_fr, text='max down: ' + str(account2.max_down)).place(rely=0.35)
    extras2_fr.grid(row=5,column=1,  pady=1, padx=1)
    ####################################################################################################################
    unsolved1_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    i = 1

    def serach_problem(index, contestid):
        webbrowser.open("http://codeforces.com/problemset/problem/" + str(contestid) + '/' + str(index))

    for problem in account1.unsolved_problem:
        print(problem)
        Button(unsolved1_fr, text=str(problem['index']) + '-' + str(problem['contestId']),
               command=lambda: serach_problem(problem['index'], problem['contestId'])).place(rely=0.1 * i)
        i += 1
    unsolved1_fr.grid(row=6,column=0,  pady=1, padx=1)
                                            ####################################
    unsolved2_fr=Frame(inner_compare_frame,width=390,height=300,bg="#231e1e",)
    i = 1

    def serach_problem(index, contestid):
        webbrowser.open("http://codeforces.com/problemset/problem/" + str(contestid) + '/' + str(index))

    for problem in account2.unsolved_problem:
        print(problem)
        Button(unsolved2_fr, text=str(problem['index']) + '-' + str(problem['contestId']),
               command=lambda: serach_problem(problem['index'], problem['contestId'])).place(rely=0.1 * i)
        i += 1
    unsolved2_fr.grid(row=6,column=1,  pady=1, padx=1)

    compare_window.mainloop()
########################################################################################################################
def weekly_rateing(handle_for_rate):
    phase=get_all(handle_for_rate)
    phase.get_problem()
    phase.get_probelms_for_phase()
    def search_max_problem(id,level):
        webbrowser.open("http://codeforces.com/problemset/problem/"+level+'/'+str(id))
    weekly_window = Toplevel()
    weekly_window.geometry("505x700")
    week_scroll = ScrolledFrame(weekly_window, width=494, height=700, bg="#231e1e", scrollbars="vertical", )
    week_scroll.pack(expand=1, fill="y", )
    week_scroll.bind_arrow_keys(weekly_window)
    week_scroll.bind_scroll_wheel(weekly_window)
    inner_week_frame = week_scroll.display_widget(Frame)  ## main window
    inner_week_frame.config(background="black", )
                            ##############################################
    phase1_fr = Frame(inner_week_frame, width=490, height=300, bg="#231e1e", )
    phase.phase1_info()
    solved1=Label(phase1_fr,text='solved: '+str(len(phase.phase1_solved))).place(rely=0.1)

    submittions1=Label(phase1_fr,text='Submissions: '+str(phase.phase1_submitions)).place(rely=0.2)

    max_rated_problem_name1=Label(phase1_fr,text='max rated problem'+str(phase.phase1_max_problem["problem"]['name'])).place(rely=0.3)

    max_rated_problem1=Button(phase1_fr,text=str(phase.phase1_max_rated_problem),command=lambda:search_max_problem(phase.phase1_max_problem['contestId'],phase.phase1_max_problem['problem']['index'])).place(rely=0.3,relx=0.4)

    phase1_fr.pack(pady=1)
    phase2_fr = Frame(inner_week_frame, width=490, height=300, bg="#231e1e", )
    phase2_fr.pack(pady=1)
    phase3_fr = Frame(inner_week_frame, width=490, height=300, bg="#231e1e", )
    phase3_fr.pack(pady=1)
    weekly_window.mainloop()
    #######################################################################################


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
    print('go')
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
    print('go')
def frame3():
    rootHeight = w.winfo_height()
    F3=Frame(w,bg='#231e1e',width=850,height=640)
    getting_handle=Entry(F3,width=40,bg="brown",font=("Calibri",16),)
    getting_handle.pack()
    getting_handle.place(relx=0.25,rely=0.15,height=25)

    go_BUTTON=Button(F3,text='GO',width=30,height=5,bg='brown',command=lambda:weekly_rateing('amy2532001'))
    go_BUTTON.pack()
    go_BUTTON.place(relx=0.4,rely=0.4)
    F3.pack(expand=1,fill='y')
    F3.place(relx=0,rely=0)
    choosen_frame=Frame(F3,width=295,height=5,bg="red").place(rely=0.99,relx=0.65)
    print('go')

#################################################################################################################################################
if __name__=="__main__":
    #######################################################(GUI design)####################################################################
    w = Tk()
    w.title("codeforces")
    w.geometry('850x700+300+10')
    w.resizable(width=False, height=1)
    w.configure(background="#231e1e")
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