import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Nelson
apellido: Chuquen
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        precio1_total = float(self.txt_importe_1.get())
        precio2_total = float(self.txt_importe_2.get())
        precio3_total = float(self.txt_importe_3.get())

        suma = (precio1_total + precio2_total + precio3_total)

        mensaje = "El total de la suma de los 3 productos es de {0}".format(suma)

        resultado_total = alert(title="Total de la suma", message=mensaje)
        


    def btn_promedio_on_click(self):
        precio1_promedio = float(self.txt_importe_1.get())
        precio2_promedio = float(self.txt_importe_2.get())
        precio3_promedio = float(self.txt_importe_3.get())

        promedio = (precio1_promedio + precio2_promedio + precio3_promedio) / 3

        mensaje = "El promedio de los 3 productos es de {0}".format(promedio)

        resultado_promedio = alert(title="Total del promedio", message=mensaje)

    def btn_total_iva_on_click(self):
        precio1_iva = float(self.txt_importe_1.get())
        precio2_iva = float(self.txt_importe_2.get())
        precio3_iva = float(self.txt_importe_3.get())

        iva = (precio1_iva + precio2_iva + precio3_iva) * 1.21

        mensaje = "El resultado de los 3 productos + IVA es de {0}".format(iva)

        resultado_iva = alert(title="Total + IVA", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()