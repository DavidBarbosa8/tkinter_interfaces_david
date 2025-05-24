import tkinter as tk
ventana = tk.Tk()

# Establecemos el título de la ventana
ventana.title("Mi ventana")

# Establecemos el tamaño de la ventana
ventana.geometry("600x400")

# Establecemos el color de fondo de la ventana
ventana.configure(bg="lightblue")

labelframe = tk.LabelFrame(ventana, text = "Grupo de Widgets", bg = "yellow", padx = 10, pady = 10)
labelframe.configure(width = 300, height = 200)
labelframe.pack()

# Crea un marco (frame) dentro de la ventana principal
frame1 = tk.Frame(ventana)
#Establecemos tamaño, color de fondo y borde del frame
frame1.configure(width = 300, height = 200, bg = "red", bd = 5)
frame1.pack() 

frame2 = tk.Frame(ventana)
frame2.configure(width = 100, height = 100, bg = "blue", bd = 5)
#Colocamos el marco en la ventana principal, utilizando el metodo pack para organizarlo


boton = tk.Button(frame1, text="Hola", bg="yellow", fg="black")
boton.pack()
frame2.pack()
# Creamos el bucle para mantener la ventana abierta
ventana.mainloop()



