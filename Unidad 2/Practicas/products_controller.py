import tkinter as tk
from tkinter import messagebox,ttk

class ProductosApp:
    def __init__ (self,username):
        self.username=username
        self.root=tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("600x400")
        self.root.resizable(True,True)