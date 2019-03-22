from tkinter import *
def btnclick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)
def clear():
    global operator
    operator=""
    text_Input.set("")
def equal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""
cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

textDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30, insertwidth=4,bg="light blue",justify="right").grid(columnspan=4)
botton_7 =Button(cal,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),text="7",command=lambda:btnclick(7)).grid(row=1,column=0)
botton_8 =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="8",command=lambda:btnclick(8)).grid(row=1,column=1)
botton_9 =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="9",command=lambda:btnclick(9)).grid(row=1,column=2)
botton_div =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="/",command=lambda:btnclick("/")).grid(row=1,column=3)
botton_6 =Button(cal,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),text="6",command=lambda:btnclick(6)).grid(row=2,column=0)
botton_5 =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="5",command=lambda:btnclick(5)).grid(row=2,column=1)
botton_4 =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="4",command=lambda:btnclick(4)).grid(row=2,column=2)
botton_mul =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="*",command=lambda:btnclick("*")).grid(row=2,column=3)
botton_3 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda:btnclick(3)).grid(row=3,column=0)
botton_2 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text = "2",command=lambda:btnclick(2)).grid(row=3,column=1)
botton_1 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text = "1",command=lambda:btnclick(1)).grid(row=3,column=2)
botton_sub =Button(cal,padx=16,pady=16,bd=8,fg="black", font=('arial',20,'bold'),text="-",command=lambda:btnclick("-")).grid(row=3,column=3)
botton_c =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="C",command=clear).grid(row=4,column=0)
botton_0 =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="0",command=lambda:btnclick(0)).grid(row=4,column=1)
botton_eq =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="=",command=equal).grid(row=4,column=2)
botton_ad =Button(cal,padx=16,pady=16,bd=8,fg="black" , font=('arial',20,'bold'),text="+",command=lambda:btnclick("+")).grid(row=4,column=3)
cal.mainloop()
