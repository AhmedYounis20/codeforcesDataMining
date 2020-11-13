'''
{"id":86780823,
"contestId":298,
"creationTimeSeconds":1594670378,
"relativeTimeSeconds":2147483647,
"problem":
{
"contestId":298,
"index":"A",
"name":"Snow Footprints",
"type":"PROGRAMMING",
"points":500.0,
"rating":1300,
"tags":["greedy","implementation"]},
"author":{"contestId":298,"members":[{"handle":"amy2532001"}],"participantType":"PRACTICE","ghost":false,"startTimeSeconds":1366385400},
"programmingLanguage":"GNU C++17",
"verdict":"OK",
"testset":"TESTS","passedTestCount":23,"timeConsumedMillis":62,"memoryConsumedBytes":3788800},
'''
'''from mylib import get_all
from collections import OrderedDict
a=get_all("moharby12")
a.get_problem()
x=OrderedDict(sorted(a.solved_level.items()))
for i in a.verdict:
    print (i,a.verdict[i])
print(len(a.solved_tages))
import wget
from PIL import Image as I, ImageTk
from tkinter import *
image = wget.download(str('http://userpic.codeforces.com/591099/avatar/e5d251220ca54303.jpg'))
image = ImageTk.PhotoImage(file=I.open('e5d251220ca54303.jpg'))
info_frame=tk()

can = Label(info_frame, width=150, height=150, borderwidth=0, highlightthickness=0, relief='ridge', image=image)
can.pack()
can.place(relx=0.01, rely=0.2)
info_frame.mainloop()
system("rm " + 'http://userpic.codeforces.com/591099/avatar/e5d251220ca54303.jpg'.split('/')[-1])
from tkinter import *
from PIL import ImageTk,Image
from tkscrolledframe import ScrolledFrame

def tr():
    #account=get_all(handle)
    res_file =Tk()
    res_file.geometry("520x700")
    res_sf = ScrolledFrame(res_file, width=500, height=700,bg="#231e1e", scrollbars="vertical",)
    res_sf.pack(side="top", fill="y",pady=1)
    res_sf.bind_arrow_keys(res_file)
    res_sf.bind_scroll_wheel(res_file)
    inner_frame = res_sf.display_widget(Frame)## main window
    info_fr = Frame(inner_frame, height=400, width=490, background="#231e1e")
    image = Image.open("e5d251220ca54303.jpg")
    image = ImageTk.PhotoImage(image)
    # l = Button(info_fr,image=image).place(rely=0)
    b = Label(info_fr, image=image).place(rely=0.3)
    info_fr.pack(pady=1)
    info_fre = Frame(inner_frame, height=400, width=490, background="#231e1e")
    image = Image.open("e5d251220ca54303.jpg")
    image = ImageTk.PhotoImage(image)
    # l = Button(info_fr,image=image).place(rely=0)
    b = Label(info_fr, image=image).place(rely=0.3)
    info_fre.pack(pady=1)
    res_file.mainloop()
    ##############################################
tr()
from mylib import *
from datetime import datetime
n=datetime.now()
b=datetime.fromtimestamp(1599484170)
print((n-b).days)
'''
from mylib import *

a=get_all('amy2532001')
a.get_problem()
a.get_probelms_for_phase()
a.phase1_info()
for i in a.phase1:
    print(i)
    print("-------------------\n")
print('#######################')
for i  in a.phase1_solved:
    print(i)
    print("-------------------\n")
print("**********************\n",a.phase1_average)


