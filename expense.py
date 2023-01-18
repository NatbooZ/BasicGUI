from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


def readcsv():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = list(csv.reader(file))
        # print(fr)
    return fr


GUI = Tk()
GUI.geometry('900x700')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')


FONT1 = ('Angsana New',25)


###########################################################Config TAB1########################################################
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

icon_tab1 = PhotoImage(file='Tab1.png')
icon_tab2 = PhotoImage(file='Tab2.png')

Tab.add(T1,text='บันทึกค่าใช้จ่าย',image=icon_tab1,compound='left')
Tab.add(T2,text='ประวัติค่าใช้จ่าย',image=icon_tab2,compound='left')

###########################################################TAB1###############################################################



#############ใส่รูปใน icon#########################
icon = r'C:\Users\GL\OneDrive\Desktop\Basic GUI\expense.png'
iconimage = PhotoImage(file=icon)
L = Label(T1,image=iconimage)
L.pack()


#############ช่องรายการค่าใช้จ่าย###################
L = Label(T1,text='รายการค่าใช้จ่าย',font=(None,30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(T1,textvariable=v_expense,font=FONT1)
E1.pack(pady=5)

###############ช่องกรอกค่าใช้จ่าย###################
L = Label(T1,text='จำนวนเงิน (บาท)',font=(None,30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(T1,textvariable=v_amount,font=FONT1)
E2.pack(pady=5)



##################ปุมบันทึกข้อมูล##################

def SaveData(event=None):
    expense = v_expense.get()
    amount = float (v_amount.get())
    timestamp = datetime.now().strftime('%Y-%B-%d %X')
    data = [expense,amount,timestamp]
    writecsv(data)
    v_expense.set('')
    v_amount.set('')
    E1.focus()

E2.bind('<Return>',SaveData)  #.ให้กด enter = save
E1.bind('<Return>',lambda x: E2.focus()) #ฟังก์ชั่นพิเศษ โดยไม่ต้องสร้างฟังก์ชั่น

#ใส่ favarite
def Fav1(event=None):
    v_expense.set('น้ำเต้าหู้')
    v_amount.set('15')

GUI.bind('<F1>',Fav1)



B1 = ttk.Button(T1,text='บันทึกข้อมูล',command=SaveData)
B1.pack(ipadx=20,ipady=10,pady=5)

########################################################TAB 2###############################################################

#ค่ารถไฟฟ้า BTS,20,2023-01-11 8:00:05
header = ['ลำดับ','รายการ','ค่าใช้จ่าย','วัน-เวลา']
hwidth = [70,300,90,300]

table = ttk.Treeview(T2,columns=header,show='headings',height=20)
table.pack()



#size,font
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,15))
style.configure('Treeview',font=(None,15),rowheight=30) #rowheight บรรทัดใหญ่ขึ้น , Treeview ตาราง



#ปรับตำแหน่งให้อยูกลาง,ซ้าย,ขวา
table.column('ค่าใช้จ่าย',anchor=E)
table.column('รายการ',anchor=CENTER)
table.column('วัน-เวลา',anchor=E)

for h,w in zip(header,hwidth):  #zip ตือใส่ค่าให้อยู่ใน list เดียวกัน
    table.column(h,width=w)
    table.heading(h,text=h)

# table.insert('','end',values=['A','B','C','D'])
data = readcsv()
for i,d in enumerate(data,start=1):   #enumerate คือ การใส่ลำดับอัตโนมัติ
    table.insert('','end',values=[i,d[0],d[1],d[2]])


########################################################TAB 2###############################################################

GUI.mainloop()