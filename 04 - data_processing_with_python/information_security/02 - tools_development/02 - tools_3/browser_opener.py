"""
    Programa que utiliza das bibliotecas 'webbrowser' e 'tkinter' para implementar uma
    ferramente gráfica para abrir um site específico.
"""
import webbrowser
from tkinter import *

root = Tk()

root.title('Open browser')
root.geometry('300x200')


def google():
    webbrowser.open('www.google.com')


my_google = Button(root, text='Open Google', command=google).pack(pady=20)
root.mainloop()
