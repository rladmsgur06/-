from tkinter import *

win=Tk()
win.title("계산기")
win.geometry("370x500")

def button_click(value):
    current=ent.get() #현재 입력창의 값을 가져오기
    ent.delete(0, END) #입력창 초기화
    ent.insert(0, current+value) #기준 값에 클릭한 값을 추가하여 입력창에 다시 삽입

#버튼 클릭 이벤트 함수

#"="버튼 클릭시 계산 수행 입력창의 수식(eval사용), 결과를 계산하는 함수
def calculate():
    try:
        result=eval(ent.get())
        ent.delete(0, END)
        ent.insert(0, str(result))
    except Exception as e:
        ent.delete(0, END)
        ent.insert(0, "수식을 입력해주세요")

def back():
    re=ent.get()
    ent.delete(len(re, -1,END))

#"c"버튼 
def clear():
    ent.delete(0,END)

ent=Entry(
    win,
    width=20,
    font=("돋움",20),
    borderwidth=5,
    justify="right"
)
ent.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

buttons=['C','<-','%','/',
         '7','8','9','*',
         '4','5','6','-',
         '1','2','3','+',
         '+/-','0','.','=']

c=0
r=1

for i in buttons:
    if i=="=":
        btn=Button(win,text=i,width=6,height=2 , command = calculate,font=("돋움",16,"bold"),relief="raised",bg="#3A01DF",fg="#FFFFFF")
    elif i=="C":
        btn=Button(win,text=i,width=6,height=2,command=clear, font=("돋움",16,"bold"),relief="raised",bg="#4B8A08",fg="#FFFFFF")
    elif i=="<-":
        btn=Button(win,text=i,width=6,height=2,command=back,font=("돋움",16,"bold"),relief="raised",bg="#585858",fg="#FFFFFF")
    else:
        btn=Button(win,text=i,width=6,height=2,command=lambda b=i: button_click(b),font=("돋움",16,"bold"),relief="raised",bg="#FF4000",fg="#FFFFFF")
    btn.config(text=i)
    btn.grid(row=r,column=c,padx=5,pady=5)
    c+=1
    if c==4:
        c=0
        r+=1

win.mainloop()