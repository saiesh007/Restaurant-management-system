from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog

# ========================== Total Button Code ==========================
def total_bills():

        # ***** Drinks Items price *****
        lassi_price = 30
        coffee_price = 20
        tea_price = 15
        juice_price = 50
        shakes_price = 80
        milk_price = 20
        water_price = 10
        liquor_price = 150

        # ***** Foods Items Price *****
        roti_price = 15
        spring_rolls_price = 220
        paneer_makhni_price = 250
        paratha_price = 40
        butter_chicken_price = 280
        dragon_chicken_price = 260
        dum_biryani_price = 280
        rice_price = 50


        # ***** Drinks Item quantity *****
        lassi_q = lassi_qty.get()
        coffee_q = coffee_qty.get()
        tea_q = tea_qty.get()
        juice_q = juice_qty.get()
        shakes_q = shakes_qty.get()
        milk_q = milk_qty.get()
        water_q = water_qty.get()
        liquor_q = liquor_qty.get()

        # ***** Foods Item quantity *****
        roti_q = roti_qty.get()
        spring_rolls_q = spring_rolls_qty.get()
        paneer_makhni_q = paneer_makhni_qty.get()
        paratha_q = paratha_qty.get()
        butter_chicken_q = butter_chicken_qty.get()
        dragon_chicken_q = dragon_chicken_qty.get()
        dum_biryani_q = dum_biryani_qty.get()
        rice_q = rice_qty.get()


        # ***** Drinks Items Validation *****
        if lassi_var.get() == 0:
                lassi_q = 0
        elif lassi_var.get() == 1 and lassi_qty.get() == "":
                messagebox.showerror("error","please fill the lassi quantity")
                lassi_q = 0

        if coffee_var.get() == 0:
                coffee_q = 0
        elif coffee_var.get() == 1 and coffee_qty.get() == "":
                messagebox.showerror("error","please fill the coffee quantity")
                coffee_q = 0

        if tea_var.get() == 0:
                tea_q = 0
        elif tea_var.get() == 1 and tea_qty.get() == "":
                messagebox.showerror("error","please fill the tea quantity")
                tea_q = 0

        if juice_var.get() == 0:
                juice_q = 0
        elif juice_var.get() == 1 and juice_qty.get() == "":
                messagebox.showerror("error","please fill the juice quantity")
                juice_q = 0

        if shakes_var.get() == 0:
                shakes_q = 0
        elif shakes_var.get() == 1 and shakes_qty.get() == "":
                messagebox.showerror("error","please fill the shakes quantity")
                shakes_q = 0

        if milk_var.get() == 0:
                milk_q = 0
        elif milk_var.get() == 1 and milk_qty.get() == "":
                messagebox.showerror("error","please fill the milk quantity")
                milk_q = 0

        if water_var.get() == 0:
                water_q = 0
        elif water_var.get() == 1 and water_qty.get() == "":
                messagebox.showerror("error","please fill the water quantity")
                water_q = 0

        if liquor_var.get() == 0:
                liquor_q = 0
        elif liquor_var.get() == 1 and liquor_qty.get() == "":
                messagebox.showerror("error","please fill the liquor quantity")
                liquor_q = 0

        
        # ***** Foods Items Validation *****
        if roti_var.get() == 0:
                roti_q = 0
        elif roti_var.get() == 1 and roti_qty.get() == "":
                messagebox.showerror("error","please fill the Roti quantity")
                roti_q = 0

        if spring_rolls_var.get() == 0:
                spring_rolls_q = 0
        elif spring_rolls_var.get() == 1 and spring_rolls_qty.get() == "":
                messagebox.showerror("error","please fill the spring rolls quantity")
                coffee_q = 0

        if paneer_makhni_var.get() == 0:
                paneer_makhni_q = 0
        elif paneer_makhni_var.get() == 1 and paneer_makhni_qty.get() == "":
                messagebox.showerror("error","please fill the Paneer makhni quantity")
                paneer_makhni_q = 0

        if paratha_var.get() == 0:
                paratha_q = 0
        elif paratha_var.get() == 1 and paratha_qty.get() == "":
                messagebox.showerror("error","please fill the Paratha quantity")
                paratha_q = 0

        if butter_chicken_var.get() == 0:
                butter_chicken_q = 0
        elif butter_chicken_var.get() == 1 and butter_chicken_qty.get() == "":
                messagebox.showerror("error","please fill the butter chicken quantity")
                butter_chicken_q = 0

        if dragon_chicken_var.get() == 0:
               dragon_chicken_q = 0
        elif dragon_chicken_var.get() == 1 and dragon_chicken_qty.get() == "":
                messagebox.showerror("error","please fill the dragon_chicken quantity")
                dragon_chicken_q = 0

        if dum_biryani_var.get() == 0:
                dum_biryani_q = 0
        elif dum_biryani_var.get() == 1 and dum_biryani_qty.get() == "":
                messagebox.showerror("error","please fill the Dum Biryani quantity")
                dum_biryani_q = 0

        if rice_var.get() == 0:
                rice_q = 0
        elif rice_var.get() == 1 and rice_qty.get() == "":
                messagebox.showerror("error","please fill the Rice quantity")
                rice_q = 0
        
        
        # ***** Total Drinks Items Price *****
        total_lassi_price = lassi_price * int(lassi_q)
        total_coffee_price = coffee_price * int(coffee_q)
        total_tea_price = tea_price * int(tea_q)
        total_juice_price = juice_price * int(juice_q)
        total_shakes_price = shakes_price * int(shakes_q)
        total_milk_price = milk_price * int(milk_q)
        total_water_price = water_price * int(water_q)
        total_liquor_price = liquor_price * int(liquor_q)

        # ***** Total Drinks cost *****
        total_drinks_cost = total_lassi_price + total_coffee_price + total_tea_price + total_juice_price + total_shakes_price + total_milk_price + total_water_price + total_liquor_price

        if drinks_cost.get() != "":
                drinks_cost.delete(0,"end")
                drinks_cost.insert("end",total_drinks_cost)
        else:
                drinks_cost.insert("end",total_drinks_cost)

        
        # ***** Total Foods Items Price *****
        total_roti_price = roti_price * int(roti_q)
        total_spring_rolls_price = spring_rolls_price * int(spring_rolls_q)
        total_paneer_makhni_price = paneer_makhni_price * int(paneer_makhni_q)
        total_paratha_price = paratha_price * int(paratha_q)
        total_butter_chicken_price = butter_chicken_price * int(butter_chicken_q)
        total_dragon_chicken_price = dragon_chicken_price * int(dragon_chicken_q)
        total_dum_biryani_price = dum_biryani_price * int(dum_biryani_q)
        total_rice_price = rice_price * int(rice_q)

         # ***** Total Foods cost *****
        total_foods_cost = total_roti_price + total_spring_rolls_price + total_paneer_makhni_price + total_paratha_price + total_butter_chicken_price + total_dragon_chicken_price + total_dum_biryani_price + total_rice_price

        if foods_cost.get() != "":
                foods_cost.delete(0,"end")
                foods_cost.insert("end",total_foods_cost)
        else:
                foods_cost.insert("end",total_foods_cost)

        
        # ***** Service charge *****
        if service_charge_cost.get() != "":
                service_charge_cost.delete(0,"end")
                service_charge_cost.insert(0,"30")
        else:
                service_charge_cost.insert(0,"30")
        
        fc =  int(foods_cost.get())
        dc = int(drinks_cost.get())

        total_paid_gst = fc+dc
        total_paid_gst = total_paid_gst * 8 / 100


        if paid_gst_cost != "":
                paid_gst_cost.delete(0,"end")
                paid_gst_cost.insert(0,total_paid_gst)
        else:
                paid_gst_cost.insert(0,total_paid_gst)

        
        total_sub_cost = fc+dc+int(service_charge_cost.get())

        if sub_total_cost.get() != "":
                sub_total_cost.delete(0,"end")
                sub_total_cost.insert(0,total_sub_cost)
        else:
                sub_total_cost.insert(0,total_sub_cost)


        if total_cost_cost.get() != "":
                total_cost_cost.delete(0,"end")
                total_cost_cost.insert(0,float(total_sub_cost + total_paid_gst))
        else:
                total_cost_cost.insert(0,float(total_sub_cost + total_paid_gst))

        

         # =====================  Total Bill Receipt ===========================
        date = datetime.now().date()
        if bill_details.get(1.0,"end") != "":
                bill_details.delete(1.0,"end")
                bill_details.insert(1.0,f" Billno-{random.randint(100,1000)}\t{date}  =====================  Items(q) \t \tAmount  ===================== \n {'Lassi ('+str(lassi_q) + ')' + '         ' + str(int(lassi_q) * lassi_price) + '   '  if lassi_var.get() == 1 else''}{'coffee ('+str(coffee_q) + ')' + '        ' + str(int(coffee_q) * coffee_price) + '  '  if coffee_var.get() == 1 else ''}{ ' tea ('+str(tea_q) + ')' + '           ' + str(int(tea_q) * tea_price) + '  '  if tea_var.get() == 1 else''}{' juice ('+str(juice_q) + ')' + '         ' + str(int(juice_q) * juice_price) + '   '  if juice_var.get() == 1 else''}{'shakes('+str(shakes_q) + ')' + '         ' + str(int(shakes_q) * shakes_price) + '   '  if shakes_var.get() == 1 else''}{'milk('+str(milk_q) + ')' + '           ' + str(int(milk_q) * milk_price) + '   '  if milk_var.get() == 1 else''}{'water('+str(water_q) + ')' + '          ' + str(int(water_q) * water_price) + '   '  if water_var.get() == 1 else''}{'liquor('+str(liquor_q) + ')' + '        ' + str(int(liquor_q) * liquor_price) + '   '  if liquor_var.get() == 1 else''}{'roti('+str(roti_q) + ')' + '            ' + str(int(roti_q) * roti_price) + '  '  if roti_var.get() == 1 else''}{'Spring Rolls('+str(spring_rolls_q) + ')' + '    ' + str(int(spring_rolls_q) * spring_rolls_price) + ' '  if spring_rolls_var.get() == 1 else''}{'Panner Makhni('+str(paneer_makhni_q) + ')' + '   ' + str(int(paneer_makhni_q) * paneer_makhni_price) + ' '  if paneer_makhni_var.get() == 1 else''}{'paratha('+str(paratha_q) + ')' + '         ' + str(int(paratha_q) * paratha_price) + '  '  if paratha_var.get() == 1 else''}{'Butter Chicken('+str(butter_chicken_q) + ')' + '  ' + str(int(butter_chicken_q) * butter_chicken_price) + ' '  if butter_chicken_var.get() == 1 else''}{'Dragon Chicken('+str(dragon_chicken_q) + ')' + '  ' + str(int(dragon_chicken_q) * dragon_chicken_price) + ' '  if dragon_chicken_var.get() == 1 else''}{'Dum Biryani('+str(dum_biryani_q) + ')' + '     ' + str(int(dum_biryani_q) * dum_biryani_price) + ' '  if dum_biryani_var.get() == 1 else''}{'Rice('+str(rice_q) + ')' + '            ' + str(int(rice_q) * rice_price) + '  '  if rice_var.get() == 1 else''}service charge     {service_charge_cost.get()}\n GST             {paid_gst_cost.get()}\n ===================== \n total          {total_cost_cost.get()}\n =====================")
        

        

# ========= Save button Code ================

def save():
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        if root.filename is None:
                return
        file_save =  str(bill_details.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()


# ===== Drinks checkbutton validation =====
def lassi_chk():
        if lassi_var.get() == 1:
                lassi_qty['state'] = "normal"
                lassi_qty['bg'] = '#e01f38'
                lassi_qty['fg'] = "white"
                
        else:
                lassi_qty['state'] = "disabled"


def coffee_chk():
        if coffee_var.get() == 1:
                coffee_qty['state'] = "normal"
                coffee_qty['bg'] = '#e01f38'
                coffee_qty['fg'] = "white"
        else:
                coffee_qty['state'] = "disabled"

def tea_chk():
        if tea_var.get() == 1:
                tea_qty['state'] = "normal"
                tea_qty['bg'] = '#e01f38'
                tea_qty['fg'] = "white"
        else:
                tea_qty['state'] = "disabled"

def juice_chk():
        if juice_var.get() == 1:
                juice_qty['state'] = "normal"
                juice_qty['bg'] = '#e01f38'
                juice_qty['fg'] = "white"
        else:
                juice_qty['state'] = "disabled"

def shakes_chk():
        if shakes_var.get() == 1:
                shakes_qty['state'] = "normal"
                shakes_qty['bg'] = '#e01f38'
                shakes_qty['fg'] = "white"
        else:
                shakes_qty['state'] = "disabled"

def milk_chk():
        if milk_var.get() == 1:
                milk_qty['state'] = "normal"
                milk_qty['bg'] = '#e01f38'
                milk_qty['fg'] = "white"
        else:
                milk_qty['state'] = "disabled"

def water_chk():
        if water_var.get() == 1:
                water_qty['state'] = "normal"
                water_qty['bg'] = '#e01f38'
                water_qty['fg'] = "white"
        else:
                water_qty['state'] = "disabled"

def liquor_chk():
        if liquor_var.get() == 1:
                liquor_qty['state'] = "normal"
                liquor_qty['bg'] = '#e01f38'
                liquor_qty['fg'] = "white"
        else:
                liquor_qty['state'] = "disabled"



# ===== Foods checkbutton validation =====

def roti_chk():
        if roti_var.get() == 1:
                roti_qty['state'] = "normal"
                roti_qty['bg'] = '#e01f38'
                roti_qty['fg'] = "white"
                
        else:
                roti_qty['state'] = "disabled"

def spring_rolls_chk():
        if spring_rolls_var.get() == 1:
                spring_rolls_qty['state'] = "normal"
                spring_rolls_qty['bg'] = '#e01f38'
                spring_rolls_qty['fg'] = "white"
        else:
               spring_rolls_qty['state'] = "disabled"

def paneer_makhni_chk():
        if paneer_makhni_var.get() == 1:
                paneer_makhni_qty['state'] = "normal"
                paneer_makhni_qty['bg'] = '#e01f38'
                paneer_makhni_qty['fg'] = "white"
        else:
                paneer_makhni_qty['state'] = "disabled"

def paratha_chk():
        if paratha_var.get() == 1:
                paratha_qty['state'] = "normal"
                paratha_qty['bg'] = '#e01f38'
                paratha_qty['fg'] = "white"
        else:
                paratha_qty['state'] = "disabled"

def butter_chicken_chk():
        if butter_chicken_var.get() == 1:
                butter_chicken_qty['state'] = "normal"
                butter_chicken_qty['bg'] = '#e01f38'
                butter_chicken_qty['fg'] = "white"
        else:
                butter_chicken_qty['state'] = "disabled"

def dragon_chicken_chk():
        if dragon_chicken_var.get() == 1:
                dragon_chicken_qty['state'] = "normal"
                dragon_chicken_qty['bg'] = '#e01f38'
                dragon_chicken_qty['fg'] = "white"
        else:
                dragon_chicken_qty['state'] = "disabled"

def dum_biryani_chk():
        if dum_biryani_var.get() == 1:
                dum_biryani_qty['state'] = "normal"
                dum_biryani_qty['bg'] = '#e01f38'
                dum_biryani_qty['fg'] = "white"
        else:
                dum_biryani_qty['state'] = "disabled"

def rice_chk():
        if rice_var.get() == 1:
                rice_qty['state'] = "normal"
                rice_qty['bg'] = '#e01f38'
                rice_qty['fg'] = "white"
        else:
                rice_qty['state'] = "disabled"


# ===== Calculator code =====
def nine():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","9")
        else:
                result.insert("end","9")
                
def eight():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","8")
        else:
                result.insert("end","8")

def seven():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","7")
        else:
                result.insert("end","7")

def six():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","6")
        else:
                result.insert("end","6")

def five():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","5")
        else:
                result.insert("end","5")

def four():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","4")
        else:
                result.insert("end","4")

def three():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","3")
        else:
                result.insert("end","3")

def two():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","2")
        else:
                result.insert("end","2")

def one():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","1")
        else:
                result.insert("end","1")

def zero():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","0")
        else:
                result.insert("end","0")

def plus():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","+")
        else:
                result.insert("end","+")

def minus():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","-")
        else:
                result.insert("end","-")

def mul():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","*")
        else:
                result.insert("end","*")

def divide():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","/")
        else:
                result.insert("end","/")

def equal():
        if result.get() == "":
                result.insert("end","error")
        elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0] == "*" or result.get()[0] == "/":
                result.delete(0,"end")
                result.insert("end","error")
        elif 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
        else:
                res = result.get()
                res = eval(res)
                result.insert("end"," = ")
                result.insert("end",res)

def clear():
        result.delete(0,"end")


# ====== Send button code ====================
def Send():
        root = tk.Tk()
        root.geometry('300x400')
        root['bg']="white"

        frame4 = Frame(root,width=300,height=60,relief=RIDGE,borderwidth=5,bg='#e01f38',highlightbackground="white", highlightcolor="white", highlightthickness=2)
        frame4.place(x=0,y=0)
                
        l2 = Label(frame4,text="Send Bill",font=('roboto',22,'bold'),bg='#e01f38',fg="#ffffff")
        l2.place(x=85,y=1)

        frame5 = Frame(root,width=300,height=340,relief=RIDGE,borderwidth=5,bg='#e01f38',highlightbackground="white", highlightcolor="white", highlightthickness=2)
        frame5.place(x=0,y=55)

        innerframe5 = Frame(frame5,width=285,height=325,relief=RIDGE,borderwidth=3,bg='#e01f38',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
        innerframe5.place(x=0,y=0)

        l3 = LabelFrame(innerframe5,text="Send Bill Through SMS",width=270,height=310,borderwidth=3,font=('verdana',10,'bold'),fg='#e01f38',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
        l3.place(x=2,y=2)

        l4 = Label(innerframe5,text="Phone Number",font=('verdana',10,'bold'))
        l4.place(x=40,y=40)

        number = Entry(innerframe5,width=30,borderwidth=2)
        number.place(x=40,y=70)
        
        l5 = Label(innerframe5,text="Bill Details",font=('verdana',10,'bold'))
        l5.place(x=40,y=100)

        b_detail = ScrolledText(innerframe5,width=23,height=7,relief=RIDGE,borderwidth=3)
        b_detail.place(x=40,y=130) 

        b_detail.insert(1.0,bill_details.get(1.0,END))



        def send_bill():
                ph_number = number.get()
                messages = b_detail.get("1.0","end-1c")

                if ph_number == "":
                        messagebox.showerror("Error",'Please fill the phone number')
                elif messages == "":
                        messagebox.showerror("Error",'Bill Details is empty')
                else:
                        url = "https://www.fast2sms.com/dev/bulk"
                        api="" # go to fast2sms.com and paste your Auth key
                        querystring = {"authorization":api,"sender_id":"FSTSMS","message":messages,"language":"english","route":"p","numbers":ph_number}

                        headers = {
                                'cache-control': "no-cache"
                                }
                        requests.request("GET", url, headers=headers, params=querystring)
                        
                
                        messagebox.showinfo("Send SMS",'Bill has been send to your successfully')

                
        send_msg = Button(innerframe5,text="Send Bill",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#2e8de4',fg="white",padx=20,command=send_bill)
        send_msg.place(x=100,y=255)

        root.mainloop()



# ===== Exit button code =====
def exit():
        message = messagebox.askquestion('Exit',"Do you want to exit the application")
        if message == "yes":
                root.destroy()
        else:
                "return"

# ===== clear button code =====
def cleared_bill():
        # ***** Drinks *****
        lassi_qty.delete(0,'end')
        lassi.deselect()
        lassi_qty['state'] = "disabled"

        coffee_qty.delete(0,'end')
        coffee.deselect()
        coffee_qty['state'] = "disabled"
        
        tea_qty.delete(0,'end')
        tea.deselect()
        tea_qty['state'] = "disabled"
        
        juice_qty.delete(0,'end')
        juice.deselect()
        juice_qty['state'] = "disabled"
        
        shakes_qty.delete(0,'end')
        shakes.deselect()
        shakes_qty['state'] = "disabled"
        
        milk_qty.delete(0,'end')
        milk.deselect()
        milk_qty['state'] = "disabled"
        
        water_qty.delete(0,'end')
        water.deselect()
        water_qty['state'] = "disabled"
        
        liquor_qty.delete(0,'end')
        liquor.deselect()
        liquor_qty['state'] = "disabled"

        # ***** Drinks *****
        roti_qty.delete(0,'end')
        roti.deselect()
        roti_qty['state'] = "disabled"
        
        spring_rolls_qty.delete(0,'end')
        spring_rolls.deselect()
        spring_rolls_qty['state'] = "disabled"
        
        paneer_makhni_qty.delete(0,'end')
        paneer_makhni.deselect()
        paneer_makhni_qty['state'] = "disabled"
        
        paratha_qty.delete(0,'end')
        paratha.deselect()
        paratha_qty['state'] = "disabled"
        
        butter_chicken_qty.delete(0,'end')
        butter_chicken.deselect()
        butter_chicken_qty['state'] = "disabled"
        
        dragon_chicken_qty.delete(0,'end')
        dragon_chicken.deselect()
        dragon_chicken_qty['state'] = "disabled"
        
        dum_biryani_qty.delete(0,'end')
        dum_biryani.deselect()
        dum_biryani_qty['state'] = "disabled"
        
        rice_qty.delete(0,'end')
        rice.deselect()
        rice_qty['state'] = "disabled"

        # ***** Total cost *****
        drinks_cost.delete(0,'end')
        foods_cost.delete(0,'end')
        service_charge_cost.delete(0,'end')
        paid_gst_cost.delete(0,'end')
        sub_total_cost.delete(0,'end')
        total_cost_cost.delete(0,'end')

        # ***** Bill Details *****
        bill_details.delete(1.0,'end')


# ===== Main Screen =====
root = tk.Tk()
root.geometry('650x400')
root.maxsize(650,390)
root.minsize(650,390)
root.title("Restaurant Management System")
root.iconbitmap(r'D:\code\Restaurant management system\cafe.ico')

frame = Frame(root,width=650,height=70,relief=RIDGE,borderwidth=5,bg='#e01f38')
frame.place(x=0,y=0)

l1 = Label(frame,text="Restaurant Management System",font=('Comic Sans MS',30,'bold'),bg='#e01f38',fg="#ffffff")
l1.place(x=8,y=4)


# **** Drinks *****
frame1= Frame(root,width=450,height=230,relief=RIDGE,borderwidth=5,bg='#e01f38')
frame1.place(x=0,y=70)

innerframe1 = Frame(frame1,width=150,height=220,relief=RIDGE,borderwidth=3,bg='#e01f38',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe1.place(x=0,y=0)

drinks  = LabelFrame(innerframe1,text="Drinks",width=135,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#e01f38',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
drinks.place(x=2,y=2)


coffee_var = IntVar()
coffee = Checkbutton(drinks,text="Coffee",variable=coffee_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=coffee_chk)
coffee.place(x=2,y=2)

coffee_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
coffee_qty.place(x=74,y=2)

tea_var = IntVar()
tea = Checkbutton(drinks,text="Tea",variable=tea_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=tea_chk)
tea.place(x=2,y=22)
tea_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
tea_qty.place(x=74,y=22)

lassi_var = IntVar()
lassi = Checkbutton(drinks,text="Lassi",variable=lassi_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=lassi_chk)
lassi.place(x=2,y=44)
lassi_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
lassi_qty.place(x=74,y=44)
#lassi_qty.insert(0,"0")


juice_var = IntVar()
juice = Checkbutton(drinks,text="Juice",variable=juice_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=juice_chk)
juice.place(x=2,y=66)
juice_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
juice_qty.place(x=74,y=66)

shakes_var = IntVar()
shakes = Checkbutton(drinks,text="Shake",variable=shakes_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=shakes_chk)
shakes.place(x=2,y=88)
shakes_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
shakes_qty.place(x=74,y=88)

milk_var = IntVar()
milk = Checkbutton(drinks,text="Milk",variable=milk_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=milk_chk)
milk.place(x=2,y=110)
milk_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
milk_qty.place(x=74,y=110)

water_var = IntVar()
water = Checkbutton(drinks,text="Water",variable=water_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=water_chk)
water.place(x=2,y=132)
water_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
water_qty.place(x=74,y=132)

liquor_var = IntVar()
liquor = Checkbutton(drinks,text="Liquor",variable=liquor_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=liquor_chk)
liquor.place(x=2,y=154)
liquor_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
liquor_qty.place(x=74,y=154)


innerframe2 = Frame(frame1,width=290,height=220,relief=RIDGE,borderwidth=3,bg='#e01f38',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe2.place(x=151,y=0)


foods  = LabelFrame(innerframe2,text="Foods",width=275,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#e01f38',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
foods.place(x=2,y=2)


spring_rolls_var = IntVar()
spring_rolls = Checkbutton(foods,text="Spring Rolls",variable=spring_rolls_var,font=('verdana',8,'bold'),command=spring_rolls_chk)
spring_rolls.place(x=2,y=2)
spring_rolls_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
spring_rolls_qty.place(x=140,y=2)

paneer_makhni_var = IntVar()
paneer_makhni = Checkbutton(foods,text="Paneer Makhni",variable=paneer_makhni_var,font=('verdana',8,'bold'),command=paneer_makhni_chk)
paneer_makhni.place(x=2,y=22)
paneer_makhni_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
paneer_makhni_qty.place(x=140,y=22)

butter_chicken_var = IntVar()
butter_chicken = Checkbutton(foods,text="Butter Chicken",variable=butter_chicken_var,font=('verdana',8,'bold'),command=butter_chicken_chk)
butter_chicken.place(x=2,y=44)
butter_chicken_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
butter_chicken_qty.place(x=140,y=44)

dragon_chicken_var = IntVar()
dragon_chicken = Checkbutton(foods,text="Dragon Chicken",variable=dragon_chicken_var,font=('verdana',8,'bold'),command=dragon_chicken_chk)
dragon_chicken.place(x=2,y=66)
dragon_chicken_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
dragon_chicken_qty.place(x=140,y=66)

dum_biryani_var = IntVar()
dum_biryani = Checkbutton(foods,text="Dum Biryani",variable=dum_biryani_var,font=('verdana',8,'bold'),command=dum_biryani_chk)
dum_biryani.place(x=2,y=88)
dum_biryani_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
dum_biryani_qty.place(x=140,y=88)

rice_var = IntVar()
rice = Checkbutton(foods,text="Rice",variable=rice_var,font=('verdana',8,'bold'),command=rice_chk)
rice.place(x=2,y=110)
rice_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
rice_qty.place(x=140,y=110)

roti_var = IntVar()
roti = Checkbutton(foods,text="Roti",variable=roti_var,font=('verdana',8,'bold'),command=roti_chk)
roti.place(x=2,y=130)
roti_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
roti_qty.place(x=140,y=130)

paratha_var = IntVar()
paratha = Checkbutton(foods,text="Paratha",variable=paratha_var,font=('verdana',8,'bold'),command=paratha_chk)
paratha.place(x=2,y=150)
paratha_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
paratha_qty.place(x=140,y=150)


# ***** Foods *****
frame2= Frame(root,width=450,height=90,relief=RIDGE,borderwidth=5,bg='#e01f38')
frame2.place(x=0,y=300)

innerframe3 = Frame(frame2,width=440,height=80,relief=RIDGE,borderwidth=3,bg='#e01f38',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe3.place(x=0,y=0)


cost_of_drinks = Label(innerframe3,text="Cost of Drinks",font=('verdana',8,'bold'))
cost_of_drinks.place(x=2,y=2)
drinks_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
drinks_cost.place(x=130,y=0)

cost_of_foods = Label(innerframe3,text="Cost of Foods",font=('verdana',8,'bold'))
cost_of_foods.place(x=2,y=24)
foods_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
foods_cost.place(x=130,y=22)

service_charge = Label(innerframe3,text="Service Charge",font=('verdana',8,'bold'))
service_charge.place(x=2,y=46)
service_charge_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
service_charge_cost.place(x=130,y=44)


paid_gst = Label(innerframe3,text="Paid gst",font=('verdana',8,'bold'))
paid_gst.place(x=250,y=2)
paid_gst_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
paid_gst_cost.place(x=330,y=0)

sub_total = Label(innerframe3,text="Sub Total",font=('verdana',8,'bold'))
sub_total.place(x=250,y=24)
sub_total_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
sub_total_cost.place(x=330,y=22)

total_cost = Label(innerframe3,text="Total Cost",font=('verdana',8,'bold'))
total_cost.place(x=250,y=46)
total_cost_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
total_cost_cost.place(x=330,y=44)


# ***** Calculator *****
frame3= Frame(root,width=200,height=320,relief=RIDGE,borderwidth=5,bg='#000000')
frame3.place(x=450,y=70)

innerframe4 = Frame(frame3,width=190,height=310,relief=RIDGE,borderwidth=3,bg='#000000',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe4.place(x=0,y=0)


result = Entry(innerframe4,width=28,relief=SUNKEN,borderwidth=3)
result.place(x=2,y=0)

nine = Button(innerframe4,text="9",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=nine)
nine.place(x=0,y=24)
eight = Button(innerframe4,text="8",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=eight)
eight.place(x=48,y=24)
seven = Button(innerframe4,text="7",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=seven)
seven.place(x=96,y=24)
plus = Button(innerframe4,text="+",padx=6,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=plus)
plus.place(x=144,y=24)


six = Button(innerframe4,text="6",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=six)
six.place(x=0,y=50)
five = Button(innerframe4,text="5",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=five)
five.place(x=48,y=50)
four = Button(innerframe4,text="4",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=four)
four.place(x=96,y=50)
minus = Button(innerframe4,text="-",padx=8,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=minus)
minus.place(x=144,y=50)

three = Button(innerframe4,text="3",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=three)
three.place(x=0,y=76)
two = Button(innerframe4,text="2",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=two)
two.place(x=48,y=76)
one = Button(innerframe4,text="1",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=one)
one.place(x=96,y=76)
multiply = Button(innerframe4,text="*",padx=7,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=mul)
multiply.place(x=144,y=76)

zero = Button(innerframe4,text="0",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=zero)
zero.place(x=0,y=102)
clear = Button(innerframe4,text="C",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=clear)
clear.place(x=48,y=102)
equal = Button(innerframe4,text="=",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#2e8de4',fg="white",command=equal)
equal.place(x=96,y=102)
divide = Button(innerframe4,text="/",padx=7,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=divide)
divide.place(x=144,y=102)


bill_details = ScrolledText(innerframe4,width=23,height=9,relief=SUNKEN,borderwidth=3,font=('courier',9,''))
bill_details.place(x=0,y=130)

# **** billing ****

total = Button(innerframe4,text="Total",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#2e8de4',fg="white",command=total_bills)
total.place(x=0,y=275)

save = Button(innerframe4,text="Save",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#2e8de4',fg="white",command=save)
save.place(x=43,y=275)

send = Button(innerframe4,text="Send",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#2e8de4',fg="white",command=Send)
send.place(x=82,y=275)

exit = Button(innerframe4,text="Exit",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#2e8de4',fg="white",command=exit)
exit.place(x=124,y=275)

clr = Button(innerframe4,text="C",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#2e8de4',fg="white",command=cleared_bill)
clr.place(x=160,y=275)

root.mainloop()
