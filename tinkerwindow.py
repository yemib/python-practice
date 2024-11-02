import tkinter as tk
# Create the main window

def buttonf():
    label  = tk.Label(root ,  text=input.get()  ,  font=("Arial"  , 15))
    label.pack(pady=10)

    print("hello guys okay")

def display_text():
    print("You entered:", entry.get())

def on_button_click():
    print("Button clicked!")



root = tk.Tk()
# Set window title
root.title("Hello Tkinter")
# Set window size (width x height)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 500) // 2
y = (screen_height - 400) // 2
""" root.geometry(f"500x400+{x}+{y}")  """ # Centers a 500x400 window on the screen
root.geometry(f"300x300")
root.config(bg="green")
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True, icon)

label = tk.Label(root, text="Hello, Tkinter!" , font=("Arial"  , 40))
label.pack()

input  =  tk.Entry(root)
input.pack()

button  =  tk.Button(root ,  text="button"  ,  bg="black"   ,  fg="white"  , font=("Arial" ,  20) , command=buttonf)
button.pack()

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Add a Button
button = tk.Button(root, text="Submit", command=display_text)
button.pack(pady=10)

# Add a Text widget
text_box = tk.Text(root, height=5, width=25)
text_box.pack(pady=10)

# Add a Canvas with a shape
canvas = tk.Canvas(root, width=200, height=200, bg="lightgrey")
canvas.pack(pady=10)
canvas.create_line(0, 0, 200, 200, fill="blue", width=2)
canvas.create_rectangle(50, 50, 150, 150, outline="red", width=2)

# Start the application
root.mainloop()
