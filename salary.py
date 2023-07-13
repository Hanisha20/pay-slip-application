from tkinter import *
from tkinter.font import BOLD 
import time
import csv
from statistics import mean
from tkinter import messagebox

root = Tk()

root2 = Toplevel()

add_employee = Toplevel()

employee_list = Toplevel()

payslip = Toplevel()

personcheck = Toplevel()

# root.geometry('1000x700+300+60')
root.geometry('990x780+260+0')
root2.geometry('500x400+480+200')
add_employee.geometry('1000x628+260+100')
employee_list.geometry('1000x628+260+100')
payslip.geometry('990x780+260+0')
personcheck.geometry('990x780+260+0')

root.state('withdrawn')
root2.state('normal')
add_employee.state('withdrawn')
employee_list.state('withdrawn')
payslip.state('withdrawn')
personcheck.state('withdrawn')


#---------functions----------


#---------login-page----------

def login():
   
    check = un_ent.get()
    check2 = pw_ent.get()
    if check == 'admin' and check2 == 'admin' or check == 'A' and check2 == 'A':
        lblnt1.config(text = 'به صفحه خود خوش آمدید   ')
        lblnt1['fg'] = 'green'
        root.state('normal')
        root2.state('withdrawn')
        
    elif check == '' and check2 == '' :
        lblnt1.config(text = '!نام کاربری یا رمز عبور را وارد نکردید')
        lblnt1['fg'] = 'blue'

    else : 
        lblnt1.config(text = 'نام کاربری یا رمز عبور اشتباه است')
        lblnt1['fg'] = 'red'
        un_ent.delete(0,END)
        pw_ent.delete(0,END)
        un_ent.focus()
def hide(event = None): 
    if pw_ent['show'] == '*':
        pw_ent['show'] = ''
        img4['file'] = 'cheshm.png'
    elif pw_ent['show'] == '' :
        img4['file'] = 'baste.png'
        pw_ent['show'] = '*'
#---------login-page----------


#---------mian-page----------
def List():
    global person , read , listkarmand
    read = open('database/data.csv' , mode = 'r' , encoding = 'utf-8')
    listkarmand = read.readlines()
    for i in range(len(listkarmand)) :
        karmand = listkarmand[i].split(',')
        if i==0:
            lst_lbl2['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl3['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl4['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl5['text']='''{: ^28}'''.format(karmand[11])
        elif i==1:
            lst_lbl7['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl8['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl9['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl10['text']='''{: ^28}'''.format(karmand[11])
        elif i==2:
            lst_lbl12['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl13['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl14['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl15['text']='''{: ^28}'''.format(karmand[11])
        elif i==3:
            lst_lbl17['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl18['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl19['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl20['text']='''{: ^28}'''.format(karmand[11])
        elif i==4:
            lst_lbl22['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl23['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl24['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl25['text']='''{: ^28}'''.format(karmand[11])
        elif i==5:
            lst_lbl27['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl28['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl29['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl30['text']='''{: ^28}'''.format(karmand[11])
        elif i==6:
            lst_lbl32['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl33['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl34['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl35['text']='''{: ^28}'''.format(karmand[11])
        elif i==7:
            lst_lbl37['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl38['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl39['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl40['text']='''{: ^28}'''.format(karmand[11])
        elif i==8:
            lst_lbl42['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl43['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl44['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl45['text']='''{: ^28}'''.format(karmand[11])
        elif i==9:
            lst_lbl47['text']='''{: ^22}'''.format(karmand[1])
            lst_lbl48['text']='''{: ^22}'''.format(karmand[0])
            lst_lbl49['text']='''{: ^25}'''.format(karmand[4])
            lst_lbl50['text']='''{: ^28}'''.format(karmand[11])
        read.close()
    if  employee_list.state != ('normal') :
        root.state('withdrawn')
        employee_list.state('normal')

def CheckId():
    if  personcheck.state != ('normal') :
        root.state('withdrawn')
        personcheck.state('normal')
        codepers_entry.focus()
def AddEmployee():
    if  add_employee.state != ('normal') :
        root.state('withdrawn')
        add_employee.state('normal')
        codelbl_ent.focus()

def BackMenu():
    if  root.state != ('normal'):
        root.state('normal')
        employee_list.state('withdrawn')
    if root.state != ('normal'):
        root.state('normal')
        add_employee.state('withdrawn')
    if root.state != ('normal'):
        root.state('normal')
        payslip.state('withdrawn')
    if root.state != ('normal'):
        root.state('normal')
        personcheck.state('withdrawn')

#---------mian-page----------
#---------addNew-employee-page-funcs--------
def saveinfo():
    CodePersoneli = codelbl_ent.get()
    Nam = namelbl_ent.get()
    NamPedar = fatherlbl_ent.get()
    Tavalod = bornlbl_ent.get()
    ShomareShensname = idnumlbl_ent.get()
    Farzand = childlbl_ent.get()
    Tahsilat = tahsillbl_ent.get()
    PayeHoqoq = hoqoqlbl_ent.get()
    Qarardad = qarardadlbl_ent.get()
    ShoroeQaradad = sqarardadlbl_ent.get()
    PaianQaradad = eqarardadlbl_ent.get()
    telephone = phonelbl_ent.get()
    Tahol = tahollbl_ent.get()
   
    if len(CodePersoneli) == 0 or len(Nam) == 0 or len(NamPedar) == 0 or len(Tavalod) == 0 or len(ShomareShensname) == 0 or len(Farzand) == 0 or len(Tahsilat) == 0 or len(PayeHoqoq) == 0 or len(Qarardad) == 0 or len(ShoroeQaradad) == 0 or len(PaianQaradad) == 0 or len(telephone) == 0 or len(Tahol) == 0 :
        print('ali')
        messagebox.showerror(title='Error', message='تمامی فیلد هارا پر کنید')
    else :               
        messagebox.askquestion('askquestion', 'آيا از ذخيره اطلاعات مطمئن هستيد؟')
        strMoshakhasat = '{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(CodePersoneli, Nam, NamPedar, Tavalod, ShomareShensname, Farzand, Tahsilat, PayeHoqoq, Qarardad, ShoroeQaradad, PaianQaradad, telephone, Tahol)
        f = open('database/data.csv', mode = 'a', encoding="utf-8")
        f.write(strMoshakhasat)
        f.close()
                
        codelbl_ent.delete(0,END)
        namelbl_ent.delete(0,END)
        fatherlbl_ent.delete(0,END)
        bornlbl_ent.delete(0,END)
        idnumlbl_ent.delete(0,END)
        childlbl_ent.delete(0,END)
        tahsillbl_ent.delete(0,END)
        hoqoqlbl_ent.delete(0,END)
        qarardadlbl_ent.delete(0,END)
        sqarardadlbl_ent.delete(0,END)
        eqarardadlbl_ent.delete(0,END)
        phonelbl_ent.delete(0,END)
        tahollbl_ent.delete(0,END)
        codelbl_ent.focus()


    
#---------addNew-employee-page-funcs--------
#---------personCheck-page-funcs--------
def searchId():
    global person_nam_lbl, person_shenasname_lbl, person_child_lbl ,person_status_lbl, lstread ,searchcode ,person, pay_nanm_lbl, pay_shenasname_lbl, pay_child_lbl ,pay_status_lbl ,pay_code_lbl ,hoqoqepaye
    
    searchcode = codepers_entry.get()
    read = open('database/data.csv', mode = 'r', encoding="utf-8")
    lstread = read.readlines()
    for i in range(len(lstread)) :
        person = lstread[i].split(',')
        if person[0] == searchcode :
            person_nam_lbl['text'] = person[1]
            person_shenasname_lbl['text'] = person[4]
            person_child_lbl['text'] = person[5]
            person_status_lbl['text'] ='''{:,}'''.format(int(person[7])) 
            
            hoqoqepaye = person[7]
            roz_entry.focus()
        read.close()
    # read = open('database/data.csv', mode = 'r', encoding="utf-8")
    # lstread = read.readlines()
    # for i in range(len(lstread)) :
    #     person2 = lstread[i].split(',')
    #     if searchcode != person2[0] :
    #         messagebox.showerror('Error' , 'in code mojod nis')
    #         person_nam_lbl['text'] = ''
    #         person_shenasname_lbl['text'] = ''
    #         person_child_lbl['text'] =''
    #         person_status_lbl['text'] =''
    #         codepers_entry.delete(0,END)
    #         codepers_entry.focus()
#---------personCheck-page-funcs--------

#---------payroll-page-funcs--------
def exportbtn():
    
    roz = roz_entry.get()
    date = date_entry.get()
    ezafe = ezafekar_entry.get()
    shab = shabkar_entry.get()
    taatil = taatilkar_entry.get()
    searchId2 = codepers_entry.get()
    if len(searchId2) != 0:

        saatezafe = ezafe
        saattatil = int(taatil)
        saatshab =  int(shab)
        tedadrozKarKard = int(roz)
        ezafekari = int(hoqoqepaye) / 220 * 1.4 * int(saatezafe)
        taatilkari = int(hoqoqepaye) / 220 * 1.4 * int(saattatil)
        shabkari = int(hoqoqepaye) / 220 * 1.35 * int(saatshab)
        bonrefahi = 8500000
        haqmaskan = 6500000
        haqolad = 4170000 * int(person_child_lbl['text'])
        haqBimeKol = int(hoqoqepaye) + int(bonrefahi) + int(haqmaskan)
        bimeSahmHardo = int(int(haqBimeKol) * 0.3) 
        haqBimeKarfarma = int(int(haqBimeKol) * 0.23)
        haqBimeKargar = int(int(haqBimeKol) * 0.07)
        jamKasri = int(haqBimeKargar) 
        jamDaramad = int(hoqoqepaye) + int(ezafekari) + int(taatilkari)+ int(shabkari) + int(bonrefahi) + int(haqmaskan) + int(haqolad)
        mozdrozane = int(int(jamDaramad) / int(tedadrozKarKard))
        mozdsaati = int(int(mozdrozane) / 8)
        KhalesPardakhti = int(jamDaramad) - int(jamKasri)
        
        pay_nanm_lbl['text']=person_nam_lbl['text']
        pay_shenasname_lbl['text'] = person_shenasname_lbl['text']
        pay_child_lbl['text'] = person_child_lbl['text']
        pay_status_lbl['text'] = person_status_lbl['text']
        pay_code_lbl['text'] = searchId2
        
        pay_roz_lbl['text'] = '''{: <15}'''.format(roz)
        pay_ezafe_lbl['text'] ='''{: <15}'''.format(ezafe)
        pay_taatil_lbl['text'] ='''{: <15}'''.format(taatil)
        pay_shab_lbl['text'] ='''{: <15}'''.format(shab)

        pay_bime_lbl1['text'] = '''{:,}'''.format(int(bimeSahmHardo))
        pay_bime_lbl2['text'] = '''{:,}'''.format(int(haqBimeKargar))
        pay_bime_lbl3['text'] = '''{:,}'''.format(int(haqBimeKarfarma))
        pay_rozane_lbl['text'] = '''{:,}'''.format(int(mozdrozane))
        pay_saati_lbl['text'] = '''{:,}'''.format(int(mozdsaati))
        pay_bon_lbl['text'] = '''{:,}'''.format(int(bonrefahi))
        pay_maskan_lbl['text'] = '''{:,}'''.format(int(haqmaskan))
        pay_olad_lbl['text'] = '''{:,}'''.format(int(haqolad))
        pay_kasri_lbl['text'] = '''{:,}'''.format(int(jamKasri))
        pay_daramad_lbl['text'] = '''{:,}'''.format(int(jamDaramad))
        pay_khales_lbl['text'] = '''{:,}'''.format(int(KhalesPardakhti))
        codepers_entry.delete(0,END)
        roz_entry.delete(0,END)
        date_entry.delete(0,END)
        ezafekar_entry.delete(0,END)
        shabkar_entry.delete(0,END)
        taatilkar_entry.delete(0,END)
        person_nam_lbl['text'] = ''
        person_shenasname_lbl['text'] = ''
        person_child_lbl['text'] = ''
        person_status_lbl['text'] = ''
        codepers_entry.focus()

        if  payslip.state != ('normal') :
            personcheck.state('withdrawn')
            payslip.state('normal')

        write=open('database/data2.txt',mode='a',encoding= 'utf-8')
        write.writelines('{},{},{},{},{},{}\n'.format(searchId2,roz,date,ezafe,taatil,shab))

        

#---------payroll-page-funcs--------

#---------employee_list-page-funcs--------



#---------employee_list-page-funcs--------


#---------functions----------

#---------images----------

img1 = PhotoImage(file = 'login.png')
img2 = PhotoImage(file = 'background-main.png')
img4 = PhotoImage(file = 'baste.png')
img5 = PhotoImage(file = 'add-btn.png')
img6 = PhotoImage(file = 'fish.png')
img7 = PhotoImage(file = 'list.png')
img11 = PhotoImage(file = 'background-login.png')
entry_name = PhotoImage(file='Rectangle 1.png')

#---------images----------
#---------login-details----------
login_lbl = Label(root2 , width = 501 , height = 398 , bg = '#ffffff' ,image = img11)

un_ent = Entry(root2,width=28 ,border=0,font=('B Nazanin',10))
pw_ent = Entry(root2 , width = 28 , show = '*' ,border=0,bg='white', font = ('B Nazanin' , 10))
btn = Button(root2 , activebackground='#ffffff' ,bg = '#ffffff', width = 115 , text = 'enter' , command = login , borderwidth= 0 , image = img1)
btn2 = Button(root2 , width = 35, image = img4 , bg = '#ffffff' , activebackground='#ffffff' , borderwidth = 0)
lblnt1 = Label(root2, text = '' , width = 25 , bg = '#ffffff')
un_ent.focus()
un_ent.bind('<Return>', lambda event: pw_ent.focus())
pw_ent.bind('<Return>', lambda event: btn.focus())
btn.bind('<Return>', login)
#---------login-details----------
#---------mainPage-details----------
main_lbl = Label(root,bg = '#ffffff', width = 1000 , height = 792, image = img2 )

add_btn = Button( activebackground='#D7E9F8' , command = AddEmployee , bg = '#D7E9F8', borderwidth= 0, image = img5)
fish_btn = Button( activebackground='#D7E9F8' ,command = CheckId , bg = '#D7E9F8' , borderwidth= 0 , image = img6)
lst_btn = Button( activebackground='#D7E9F8' , command = List , bg = '#D7E9F8', borderwidth= 0 , image = img7)

#---------mainPage-details----------
#---------addNew-employee-Page-details----------
newEmployee_bg = PhotoImage(file = 'bg-newEmployee.png')
code_box = PhotoImage(file = 'code-box.png')
sumbmit_img = PhotoImage(file = 'submit.png')
picture_img = PhotoImage(file = 'picture.png')
select_img = PhotoImage(file = 'selectpic.png')
mainpage_btn = PhotoImage(file = 'backbtn.png')

addNew_lbl = Label(add_employee, bg = '#ffffff', width = 1000 , height = 627 ,  image = newEmployee_bg)

picture_box = Label(add_employee, bg = 'white' , image = picture_img)
picture_box.place(x = 40 , y = 25)

sumbmit = Button(add_employee, height = 55 , bg = 'white' , command = saveinfo ,activebackground = 'white' , borderwidth = 0 , image = sumbmit_img)
back_btn = Button(add_employee, height = 55 , bg = 'white',command = BackMenu, activebackground = 'white' , borderwidth = 0 , image = mainpage_btn )

sumbmit.place(x = 515 , y = 545)
back_btn.place(x = 324 , y = 545)

select_btn = Button(add_employee, bg = 'white' , activebackground = 'white' , borderwidth = 0 , image = select_img)
select_btn.place(x = 155 , y = 41)


codelbl_ent = Entry(add_employee,  width = 13 , border=0 , bg='white', font = ('B Nazanin' , 10) , justify = 'center'  )
codelbl_ent.place(x = 739 , y = 41)
codelbl_ent.focus()
codelbl_ent.bind('<Return>', lambda event: namelbl_ent.focus())

namelbl_ent = Entry(add_employee,  width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10) , justify = 'right'  )
namelbl_ent.place(x = 551, y = 120)
namelbl_ent.bind('<Return>', lambda event: fatherlbl_ent.focus())

fatherlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
fatherlbl_ent.place(x = 551, y = 187)
fatherlbl_ent.bind('<Return>', lambda event: bornlbl_ent.focus())

bornlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
bornlbl_ent.place(x = 551, y = 261)
bornlbl_ent.bind('<Return>', lambda event: idnumlbl_ent.focus())

idnumlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
idnumlbl_ent.place(x = 551, y = 335)
idnumlbl_ent.bind('<Return>', lambda event: childlbl_ent.focus())

childlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
childlbl_ent.place(x = 551, y = 409)
childlbl_ent.bind('<Return>', lambda event: tahsillbl_ent.focus())

tahsillbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
tahsillbl_ent.place(x = 551, y = 483)
tahsillbl_ent.bind('<Return>', lambda event: hoqoqlbl_ent.focus())

hoqoqlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
hoqoqlbl_ent.place(x = 95, y = 118)
hoqoqlbl_ent.bind('<Return>', lambda event: qarardadlbl_ent.focus())

qarardadlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
qarardadlbl_ent.place(x = 95, y = 188)
qarardadlbl_ent.bind('<Return>', lambda event: sqarardadlbl_ent.focus())

sqarardadlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
sqarardadlbl_ent.place(x = 95, y = 262)
sqarardadlbl_ent.bind('<Return>', lambda event: eqarardadlbl_ent.focus())

eqarardadlbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
eqarardadlbl_ent.place(x = 95, y = 336)
eqarardadlbl_ent.bind('<Return>', lambda event: phonelbl_ent.focus())

phonelbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
phonelbl_ent.place(x = 95, y = 410)
phonelbl_ent.bind('<Return>', lambda event: tahollbl_ent.focus())

tahollbl_ent = Entry(add_employee,   width = 28 , border=0 , bg='white', font = ('B Nazanin' , 10),  justify = 'right')
tahollbl_ent.bind('<Return>', lambda event: sumbmit.focus())
tahollbl_ent.place(x = 95, y = 484)
addNew_lbl.place(x = 0 , y = 7)
#---------addNew-employee-Page-details----------

#----------employee's-List-Page----------

#----------employee's-List-photos----------
list_page = PhotoImage(file = 'list-page.png')
#----------employee's-List-photos----------
listlbl = Label(employee_list, bg = '#ffffff', width = 1000 , height = 627 ,  image = list_page )
back_btn = Button(employee_list, bg = 'white',command = BackMenu, height = 55 , activebackground = 'white' , borderwidth = 0 , image = mainpage_btn )
back_btn.place(x = 419 , y = 545 )
listlbl.place(x = 0 , y = 0)
lst_lbl1 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '1', width = 2 , bg = 'white')
lst_lbl1 .place(x =895 , y = 131)
lst_lbl2 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl2 .place(x = 684, y = 131)
lst_lbl3 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 10, bg = 'white')
lst_lbl3 .place(x = 520 , y = 131)
lst_lbl4 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl4 .place(x = 339 , y = 131)
lst_lbl5 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl5 .place(x = 87, y = 131)



lst_lbl6 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '2', width = 2 , bg = 'white')
lst_lbl6 .place(x =895 , y = 173)
lst_lbl7 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl7 .place(x = 684, y = 173)
lst_lbl8 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 10, bg = 'white')
lst_lbl8 .place(x = 520 , y = 173)
lst_lbl9 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl9 .place(x = 339 , y = 173)
lst_lbl10 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl10.place(x = 87, y = 173)



lst_lbl11 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '3', width = 2 , bg = 'white')
lst_lbl11.place(x =895 , y = 214)
lst_lbl12 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl12.place(x = 684, y = 214)
lst_lbl13 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl13.place(x = 520 , y = 214)
lst_lbl14 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl14.place(x = 339 , y = 214)
lst_lbl15 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl15.place(x = 87, y = 214)




lst_lbl16 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '4', width = 2 , bg = 'white')
lst_lbl16.place(x =895 , y = 254)
lst_lbl17 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl17.place(x = 684, y = 254)
lst_lbl18 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl18.place(x = 520 , y = 254)
lst_lbl19 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl19.place(x = 339 , y = 254)
lst_lbl20 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl20.place(x = 87, y = 254)




lst_lbl21 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '5', width = 2 , bg = 'white')
lst_lbl21.place(x =895 , y = 294)
lst_lbl22 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl22.place(x = 684, y = 294)
lst_lbl23 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl23.place(x = 520 , y = 294)
lst_lbl24 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl24.place(x = 339 , y = 294)
lst_lbl25 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl25.place(x = 87, y = 294)




lst_lbl26 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '6', width = 2 , bg = 'white')
lst_lbl26.place(x =895 , y = 334)
lst_lbl27 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl27.place(x = 684, y = 334)
lst_lbl28 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl28.place(x = 520 , y = 334)
lst_lbl29 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl29.place(x = 339 , y = 334)
lst_lbl30 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl30.place(x = 87, y = 334)



lst_lbl31 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '7', width = 2 , bg = 'white')
lst_lbl31.place(x =895 , y = 374)
lst_lbl32 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl32.place(x = 684, y = 374)
lst_lbl33 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl33.place(x = 520 , y = 374)
lst_lbl34 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl34.place(x = 339 , y = 374)
lst_lbl35 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl35.place(x = 87, y = 374)




lst_lbl36 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '8', width = 2 , bg = 'white')
lst_lbl36.place(x =895 , y = 414)
lst_lbl37 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl37.place(x = 684, y = 414)
lst_lbl38 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl38.place(x = 520 , y = 414)
lst_lbl39 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl39.place(x = 339 , y = 414)
lst_lbl40 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl40.place(x = 87, y = 414)




lst_lbl41 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '9', width = 2 , bg = 'white')
lst_lbl41.place(x =895 , y = 454)
lst_lbl42 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13 , bg = 'white')
lst_lbl42.place(x = 684, y = 454)
lst_lbl43 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl43.place(x = 520 , y = 454)
lst_lbl44 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl44.place(x = 339 , y = 454)
lst_lbl45 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl45.place(x = 87, y = 454)




lst_lbl46 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '10', width = 2 , bg = 'white')
lst_lbl46.place(x =895 , y = 494)
lst_lbl47 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width = 13  , bg = 'white')
lst_lbl47.place(x = 684, y = 494)
lst_lbl48 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl48.place(x = 520 , y = 494)
lst_lbl49 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =10 , bg = 'white')
lst_lbl49.place(x = 339 , y = 494)
lst_lbl50 = Label(employee_list, height = 0 , font = ('B Nazanin' , 16), text = '', width =14 , bg = 'white')
lst_lbl50.place(x = 87, y = 494)

#----------employee's-List-Page----------


#----------personCheck-Page----------
#----------personCheck-Page-images---------
personcheck_page = PhotoImage(file = 'bg-personCheck.png')
search_btn = PhotoImage(file = 'search-btn.png')
export_btn = PhotoImage(file = 'export-btn.png')
#----------personCheck-Page-images---------

person_check = Label(personcheck, bg = '#ffffff', width = 1000 , height = 800 ,  image = personcheck_page )
person_check.place(x = 0 , y = 0)

codepers_entry = Entry(personcheck,   width = 18 , border=0 , bg='white', font = ('B Nazanin' , 12),  justify = 'center')
codepers_entry.place(x = 350 , y = 138)
codepers_entry.focus()
codepers_entry.bind('<Return>' , lambda event: roz_entry.focus())

searchbtn = Button(personcheck, bg = 'white', height = 55 ,command = searchId , activebackground = 'white' , borderwidth = 0 , image = search_btn )
searchbtn.place(x = 412 , y = 200)

person_nam_lbl = Label(personcheck , height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
person_nam_lbl.place(x = 604 , y = 412)

person_shenasname_lbl = Label(personcheck , height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
person_shenasname_lbl.place(x = 604 , y = 458)

person_child_lbl = Label(personcheck , height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
person_child_lbl.place(x = 604 , y = 504)

person_status_lbl = Label(personcheck , height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
person_status_lbl.place(x = 604 , y = 550)


roz_entry = Entry(personcheck,   width = 18 , border=0 , bg='white', font = ('B Nazanin' , 12),  justify = 'center')
roz_entry.place(x = 138 , y = 395)
roz_entry.bind('<Return>' , lambda event: date_entry.focus())

date_entry = Entry(personcheck,   width = 18 , border=0 , bg='white', font = ('B Nazanin' , 12),  justify = 'center')
date_entry.place(x = 138 , y = 442)
date_entry.bind('<Return>' , lambda event: ezafekar_entry.focus())

ezafekar_entry = Entry(personcheck,   width = 18 , border=0 , bg='white', font = ('B Nazanin' , 12),  justify = 'center')
ezafekar_entry.place(x = 138 , y = 489)
ezafekar_entry.bind('<Return>' , lambda event: shabkar_entry.focus())

shabkar_entry = Entry(personcheck,   width = 18 , border=0 , bg='white', font = ('B Nazanin' , 12),  justify = 'center')
shabkar_entry.place(x = 138 , y = 537)
shabkar_entry.bind('<Return>' , lambda event: taatilkar_entry.focus())

taatilkar_entry = Entry(personcheck,   width = 18 , border=0 , bg='white', font = ('B Nazanin' , 12),  justify = 'center')
taatilkar_entry.place(x = 138 , y = 583)


back_btn_person = Button(personcheck, bg = 'white', height = 55 ,command = BackMenu, activebackground = 'white' , borderwidth = 0 , image = mainpage_btn )
back_btn_person.place(x = 310 , y = 694)
exportbtn = Button(personcheck, bg = 'white', height = 55 ,command = exportbtn , activebackground = 'white' , borderwidth = 0 , image = export_btn )
exportbtn.place(x = 500 , y = 694)

#----------personCheck-Page----------


#----------payroll-Page----------
#----------payroll-Page-images---------
payroll_page = PhotoImage(file = 'bg-payroll.png')
print_btn_img = PhotoImage(file = 'print-btn.png')

#----------payroll-Page-images---------
payrolllbl = Label(payslip, bg = '#ffffff', width = 1000 , height = 800 ,  image = payroll_page )

pay_nanm_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_nanm_lbl.place(x = 584 , y = 104)

pay_shenasname_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_shenasname_lbl.place(x = 584 , y = 141)

pay_child_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_child_lbl.place(x = 584 , y = 181)

pay_status_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_status_lbl.place(x = 584 , y = 218)

pay_code_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_code_lbl.place(x = 584 , y = 255)





pay_roz_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '',  width = 11 , bg = '#ECECEC')
pay_roz_lbl.place(x = 142 , y = 107)

pay_ezafe_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '',  width = 11 , bg = '#ECECEC')
pay_ezafe_lbl.place(x = 142 , y = 146)

pay_taatil_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '',  width = 11 , bg = '#ECECEC')
pay_taatil_lbl.place(x = 142 , y = 185)

pay_shab_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '',  width = 11 , bg = '#ECECEC')
pay_shab_lbl.place(x = 142 , y = 226)




pay_bime_lbl1 = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_bime_lbl1.place(x = 535 , y = 408)

pay_bime_lbl2 = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_bime_lbl2.place(x = 535 , y = 443)

pay_bime_lbl3 = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_bime_lbl3.place(x = 535 , y = 478)




pay_rozane_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_rozane_lbl.place(x = 175 , y = 400)

pay_saati_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_saati_lbl.place(x = 175 , y = 434)

pay_bon_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_bon_lbl.place(x = 175 , y = 468)

pay_maskan_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_maskan_lbl.place(x = 175 , y = 502)
pay_olad_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#ECECEC')
pay_olad_lbl.place(x = 175 , y = 536)




pay_kasri_lbl = Label(payslip, height = 1 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#DDEEDA')
pay_kasri_lbl.place(x = 541 , y = 597)

pay_daramad_lbl = Label(payslip, height = 1 , font = ('B Nazanin' , 16), text = '', width = 11 , bg = '#DDEEDA')
pay_daramad_lbl.place(x = 541 , y = 638)

pay_khales_lbl = Label(payslip, height = 0 , font = ('B Nazanin' , 17), text = '', width = 11 , bg = '#DDEEDA')
pay_khales_lbl.place(x = 155 , y = 620)


back_btn = Button(payslip, bg = 'white', height = 55 ,command = BackMenu, activebackground = 'white' , borderwidth = 0 , image = mainpage_btn )
print_btn = Button(payslip, bg = 'white', height = 55 , activebackground = 'white' , borderwidth = 0 , image = print_btn_img )
print_btn.place(x = 520 , y = 702 )

back_btn.place(x = 328 , y = 702 )
payrolllbl.place(x = 0 , y = 0)
#----------payroll-Page----------

#---------login-install----------
# un_entry_image.place(x = 35,y=20)
# pw_entry_image.place(x = 35 , y = 60)
# lblfrm.place(x = 190 , y = 130)
# un.place(x = 240 , y = 10)
un_ent.place(x = 115 ,y = 76)
# pw.place(x = 240 , y = 50)
pw_ent.place(x= 115 , y = 129)
btn2.place(x = 62, y = 123)
btn.place(x = 183 , y = 210)
lblnt1.place(x = 150 , y = 290)
login_lbl.place( x = 0 , y = 0)
#---------login-install----------
#---------Main-install----------

main_lbl.place(x = 0 , y = -10)
add_btn.place(x = 94 , y = 619)
fish_btn.place(x = 722 , y = 619)
lst_btn.place(x = 413 , y = 619)


#---------Main-install----------

# un_ent.focus()

#---------login-bind----------
btn2.bind('<Button-1>',hide)
btn2.bind('<ButtonRelease>',hide)
#---------login-bind----------

root2.mainloop()
root.mainloop()
