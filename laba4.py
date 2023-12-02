import tkinter as tk

def click(color):
    a.configure(text=color[0])
    b.delete(first=0,last=tk.END)
    b.insert(0,color[1])


window = tk.Tk()
window.geometry('500x300')

a = tk.Label(window)

b = tk.Entry(window)
f = tk.Frame(window)

b1 = tk.Button(f,bg="red",width=8,height=4, command=lambda: click(["Красный","#FF0000"]))
b2 = tk.Button(f,bg="orange",width=8,height=4, command=lambda: click(["Оранжевый","#FF4500"]))
b3 = tk.Button(f,bg="yellow",width=8,height=4, command=lambda: click(["Жёлтый","#FFFF00"]))
b4 = tk.Button(f,bg="green",width=8,height=4, command=lambda: click(["Зеленый","##008000"]))
b5 = tk.Button(f,bg="#ADD8E6",width=8,height=4, command=lambda: click(["Голубой","#ADD8E6"]))
b6 = tk.Button(f,bg="blue",width=8,height=4, command=lambda: click(["Синий","#0000FF"]))
b7 = tk.Button(f,bg="purple",width=8,height=4, command=lambda: click(["Фиолетовый","#800080"]))

a.pack(side=tk.TOP)
b.pack(side=tk.TOP)
b1.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)
b3.pack(side=tk.LEFT)
b4.pack(side=tk.LEFT)
b5.pack(side=tk.LEFT)
b6.pack(side=tk.LEFT)
b7.pack(side=tk.LEFT)
f.pack(side=tk.TOP)

window.mainloop()
