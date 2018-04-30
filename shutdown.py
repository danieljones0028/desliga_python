#!/usr/bin/python3
#
# https://docs.python.org/3/library/tkinter.html
import tkinter as tk 
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.desligar = tk.Button(self, text="OK", height=2, width=53, fg="black", bg="dark grey",
                                command=self.desliga)
        self.desligar.pack(side="left")

        self.cancelar = tk.Button(self, text="Cancelar", height=2, width=53, fg="black", bg="dark grey",
                              command=root.destroy)
        self.cancelar.pack(side="right")

    def desliga(self):
        subprocess.call(["/usr/bin/python3","/usr/bin/decisao.py"])
        subprocess.call(["/sbin/init","0"])

root = tk.Tk()
root.title('Desligamento iniciado...')
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()