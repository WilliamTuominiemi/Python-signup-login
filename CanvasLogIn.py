import tkinter as tk

root= tk.Tk()

c_width = 400
c_height = 300

canvas1 = tk.Canvas(root, width = c_width, height = c_height)
canvas1.pack()

uFile = 'username.txt'
pFile = 'password.txt'

def SignUp():
    def SignedIn():
        username = entry1.get()
        password = entry2.get()

        if len(username) == 0 or len(password) == 0:
            label1 = tk.Label(root, text= "Can't leave field empty")
            canvas1.create_window(c_width / 2, c_height / 2 + 50, window=label1)
        else:
            print(username)
            print(password)

            uIsAvailable = "true"
            
            file1 = open(uFile, 'r') 
            Lines = file1.readlines() 
            count = 0
            for line in Lines:
                print("Line{}: {}".format(count, line.strip()), " ", username) 
                if line.strip() == username:
                    label1 = tk.Label(root, text= "Username not available")
                    canvas1.create_window(c_width / 2, c_height / 2 + 50, window=label1)
                    uIsAvailable = "false"
                    
            if uIsAvailable == "true":
                print("creating new user")
                
                f=open(pFile, 'a')
                f.write("\n"+password)
                
                f=open(uFile, 'a')
                f.write("\n"+username)
                
                f.close()
                LogIn()

          
    canvas1.delete("all")

    canvas1.create_text(c_width / 2, 25, text="Sign up")
    
    canvas1.create_text(c_width / 2, 100, text="Enter your username")

    entry1 = tk.Entry (root) 
    canvas1.create_window(c_width / 2, 125, window=entry1)
    
    canvas1.create_text(c_width / 2, 150, text="Enter your password")

    entry2 = tk.Entry (root) 
    canvas1.create_window(c_width / 2, 175, window=entry2)

    button1 = tk.Button(text='Sign up', command=SignedIn)
    canvas1.create_window(c_width / 2, 225, window=button1)

    button1 = tk.Button(text='Back', command=Menu)
    canvas1.create_window(c_width / 2, 275, window=button1)

def LogIn():
    def LoggedIn():
        u_index = 0
        p_index = 1
        
        username = entry1.get()
        password = entry2.get()

        d_password = ""
        d_username = ""
        
        u_f=open(uFile,'r') 
        for line in u_f:
            d_username = line.strip
            print(d_username, " ", username)
            if d_username == username:
                break
            u_index = u_index + 1
            
        p_f=open(pFile)
        lines=p_f.readlines()
        d_password = lines[u_index-1]
        if password == d_password:
            canvas1.delete("all")
            canvas1.create_text(c_width / 2, 50, text="Welcome back " + username)

            button1 = tk.Button(text='Menu', command=Menu)
            canvas1.create_window(c_width / 2, 275, window=button1)
            
            def paint( event ):
               python_green = "#476042"
               x1, y1 = ( event.x - 5), ( event.y - 5 )
               x2, y2 = ( event.x + 5), ( event.y + 5 )
               canvas1.create_oval( x1, y1, x2, y2, fill = python_green )

            canvas1.bind( "<B1-Motion>", paint )
        else:
            print("password and username index don't match")
            label1 = tk.Label(root, text= "Incorrect username or password")
            canvas1.create_window(c_width / 2, c_height / 2 + 50, window=label1)          
            
        u_f.close()    
        
    canvas1.delete("all")

    canvas1.create_text(c_width / 2, 25, text="Log in")
    
    canvas1.create_text(c_width / 2, 100, text="Enter your username")

    entry1 = tk.Entry (root) 
    canvas1.create_window(c_width / 2, 125, window=entry1)

    canvas1.create_text(c_width / 2, 150, text="Enter your password")

    entry2 = tk.Entry (root) 
    canvas1.create_window(c_width / 2, 175, window=entry2)

    button1 = tk.Button(text='Log in', command=LoggedIn)
    canvas1.create_window(c_width / 2, 225, window=button1)

    button1 = tk.Button(text='Back', command=Menu)
    canvas1.create_window(c_width / 2, 275, window=button1)



def Menu():
    canvas1.delete("all")
    
    button1 = tk.Button(text='Log in', command=LogIn)
    canvas1.create_window(c_width / 2, c_height / 2 - 20, window=button1) 

    button2 = tk.Button(text='Sign up', command=SignUp)
    canvas1.create_window(c_width / 2, c_height / 2 + 20, window=button2)

Menu()

