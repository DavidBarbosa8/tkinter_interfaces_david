# Importando la libreria tkinter
import tkinter as tk

#Creando una ventana vacia
ventana = tk.Tk()

# Agregamos un titulo a la ventana
ventana.title("Mi primera ventana")

# Cambia las dimensiones de la ventana
ventana.geometry("600x400+900+200") # Puedes modificar donde vas a colocar la ventana cambiando los dos ultimos valores. El primero es el ancho y el segundo la altura. El tercer valor es la distancia desde la izquierda y el cuarto desde arriba.

# Configuramos la ventana para que no se pueda minimizar desde ciertos parametros
ventana.minsize(400,200)

# Llamar el icono que descargaste
# Pagina para descargar iconos: https://icon-icons.com/es/
ventana.iconbitmap("gato.ico")

# Cambiar el color de fondo de la ventana
# COlores disponibles en tkinter: https://patriciaemiguel.com/assets/tkinter_colores.png
ventana.configure(bg="gold3")

# Se utiliza para configurar si la ventana puede ser redimensaionada o no
ventana.resizable(False,True) # El primer valor es para el ancho y el segundo para la altura. Si se coloca en True se puede 
                              #redimensionar y si se coloca en False no se puede redimensionar.

# Agrega transparencia a la ventana	(opcional) siendo el valor 1 el 100% de transparencia y 0 el 0% de transparencia.
ventana.attributes("-alpha", 0.9)  

# Con esta función la ventana se mantiene abierta. Sin este bucle la ventana se cierra inmediatamente
ventana.mainloop()




