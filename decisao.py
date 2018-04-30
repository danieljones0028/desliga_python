#!/usr/bin/python3
import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.desligar = tk.Button(self, text="NÃO", height=2, width=53, fg="black", bg="dark grey",
                                command=self.desliga)
        self.desligar.pack(side="right")

        self.cancelar = tk.Button(self, text="SIM", height=2, width=53, fg="black", bg="dark grey",
                              command=root.destroy)
        self.cancelar.pack(side="left")

    def desliga(self):
        subprocess.call(["bash","mata-shutdown.sh"])
        subprocess.call(["bash","mata-decisao.sh"])

root = tk.Tk()
root.title('Você quer Realmente Desligar o Computador?')
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()