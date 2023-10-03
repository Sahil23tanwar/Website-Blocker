from tkinter import *
root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Website Blocker")
Label(root,text='Website Blocker').pack()
host_path='C:\Windows\System32\drivers\etc\hosts'
ip_address='127.0.0.1';
Label(root,text='Enter Website').place(x=5,y=60)
Websites=Text(root,height='2',width='40')
Websites.place(x=140,y=60)

def Blocker():
    website_lists=Websites.get(1.0,END)
    Website=list(website_lists.split(","))
    with open (host_path,'r+') as host_file:
        file_content=host_file.read()
        for web in Website:
            if web in file_content:
                Label(root,text="Already Passed").place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(root,text="Blocked").place(x=230,y=200)
                
block=Button(root,text='Block',command=Blocker,pady=5,width=6,bg='royal blue',activebackground='sky blue')
block.place(x=230,y=150)  
root=mainloop()
