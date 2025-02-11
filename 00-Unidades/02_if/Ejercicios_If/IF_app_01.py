import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Nelson
apellido:Chuquen
---
Ejercicio: if_01
---
Enunciado:
Al presionar el botón 'Mostrar', se deberá obtener el contenido de la caja de texto txt_edad,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad = self.txt_edad.get()

        numero_entero = int(edad)

        mensaje_mayor = "Usted tiene {0} años".format(numero_entero)

        mensaje_menor = "Usted no tiene 18 años, Usted tiene {0} años".format(numero_entero)

        if(numero_entero == 18):
            alert(title="Mensaje", message=mensaje_mayor)
        else:
            alert(title="Mensaje", message=mensaje_menor)
        




         
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()