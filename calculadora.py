# Importamos las librerías que necesitamos
import tkinter as tk                    # Para crear ventanas y botones
from tkinter import ttk                 # Para pestañas y elementos más bonitos
from tkinter import messagebox          # Para mostrar mensajes de error o éxito
from datetime import datetime           # Para trabajar con fechas

# Creamos nuestra clase principal (es como una plantilla para nuestra calculadora)
class CalculadoraSimple:
    def __init__(self, ventana_principal):
        # Guardamos la ventana principal para usarla después
        self.ventana = ventana_principal
        
        # Configuramos cómo se ve nuestra ventana
        self.ventana.title("Mi Calculadora")  # El título que aparece arriba
        self.ventana.geometry("400x300")      # Tamaño: 400 de ancho x 300 de alto
        self.ventana.configure(bg="#222831")  # Fondo general oscuro

        # Creamos las pestañas (como las pestañas de un navegador web)
        self.pestanas = ttk.Notebook(ventana_principal)
        # Las pegamos a toda la ventana
        self.pestanas.pack(fill="both", expand=True, padx=10, pady=10)

        # Ahora creamos cada pestaña una por una
        self.crear_pestaña_monedas()
        self.crear_pestaña_temperatura()
        self.crear_pestaña_fechas()
    
    # PESTAÑA 1: CONVERSIÓN DE MONEDAS
    def crear_pestaña_monedas(self):
        # Creamos un marco (como una hoja en blanco) para esta pestaña
        marco_monedas = tk.Frame(self.pestanas, bg="#FF7043")  # Naranja fuerte
        self.pestanas.add(marco_monedas, text="Monedas")

        # Título grande y bonito
        titulo = tk.Label(marco_monedas, text="Convertir Pesos Colombianos",
                          font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#FF5733")
        titulo.pack(pady=10)

        # Creamos una caja de texto donde el usuario escribirá la cantidad
        tk.Label(marco_monedas, text="Escribe cuántos pesos colombianos tienes:",
                 bg="#FF7043", fg="#FFFFFF").pack(pady=5)
        self.caja_pesos = tk.Entry(marco_monedas, width=20, bg="#FFF3E0", fg="#222831")
        self.caja_pesos.pack(pady=5)
        self.caja_pesos.bind("<Return>", lambda event: self.convertir_dinero())

        # Botón que hace la conversión cuando lo presionan
        boton_convertir = tk.Button(marco_monedas, text="Convertir",
                                   command=self.convertir_dinero, bg="#FF8A65", fg="#FFFFFF", activebackground="#FFAB91")
        boton_convertir.pack(pady=10)

        # Aquí mostraremos los resultados
        self.resultado_dolares = tk.Label(marco_monedas, text="Dólares: $0.00", bg="#FF7043", fg="#FFFFFF")
        self.resultado_dolares.pack(pady=2)
        self.resultado_euros = tk.Label(marco_monedas, text="Euros: €0.00", bg="#FF7043", fg="#FFFFFF")
        self.resultado_euros.pack(pady=2)
        self.resultado_yuan = tk.Label(marco_monedas, text="Yuan: ¥0.00", bg="#FF7043", fg="#FFFFFF")
        self.resultado_yuan.pack(pady=2)

    # PESTAÑA 2: CONVERSIÓN DE TEMPERATURA
    def crear_pestaña_temperatura(self):
        # Igual que antes, creamos un marco para esta pestaña
        marco_temp = tk.Frame(self.pestanas, bg="#29B6F6")  # Azul vibrante
        self.pestanas.add(marco_temp, text="Temperatura")

        # Título
        titulo = tk.Label(marco_temp, text="Convertir Temperatura",
                          font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#33C1FF")
        titulo.pack(pady=10)

        # Caja para escribir los grados Celsius
        tk.Label(marco_temp, text="Escribe la temperatura en Grados Celsius:",
                 bg="#29B6F6", fg="#FFFFFF").pack(pady=5)
        self.caja_celsius = tk.Entry(marco_temp, width=20, bg="#E1F5FE", fg="#222831")
        self.caja_celsius.pack(pady=5)
        self.caja_celsius.bind("<Return>", lambda event: self.convertir_temperatura())

        # Botón para convertir
        boton_temp = tk.Button(marco_temp, text="Convertir",
                          command=self.convertir_temperatura, bg="#4FC3F7", fg="#FFFFFF", activebackground="#81D4FA")
        boton_temp.pack(pady=10)

        # Donde mostraremos los resultados
        self.resultado_fahrenheit = tk.Label(marco_temp, text="Fahrenheit: 0°F", bg="#29B6F6", fg="#FFFFFF")
        self.resultado_fahrenheit.pack(pady=2)
        self.resultado_kelvin = tk.Label(marco_temp, text="Kelvin: 0K", bg="#29B6F6", fg="#FFFFFF")
        self.resultado_kelvin.pack(pady=2)

    # PESTAÑA 3: DÍAS ENTRE FECHAS
    def crear_pestaña_fechas(self):
        # Creamos el marco para fechas
        marco_fechas = tk.Frame(self.pestanas, bg="#8E24AA")  # Violeta intenso
        self.pestanas.add(marco_fechas, text="Fechas")

        # Título
        titulo = tk.Label(marco_fechas, text="¿Cuántos días han pasado?",
                          font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#9D33FF")
        titulo.pack(pady=10)

        # Primera fecha
        tk.Label(marco_fechas, text="Primera fecha (día/mes/año):",
                 bg="#8E24AA", fg="#FFFFFF").pack(pady=2)
        tk.Label(marco_fechas, text="Ejemplo: 25/12/2023",
                 font=("Arial", 8), bg="#8E24AA", fg="#FFFFFF").pack(pady=1)
        self.caja_fecha1 = tk.Entry(marco_fechas, width=20, bg="#F3E5F5", fg="#222831")
        self.caja_fecha1.pack(pady=5)

        # Segunda fecha
        tk.Label(marco_fechas, text="Segunda fecha (día/mes/año):",
                 bg="#8E24AA", fg="#FFFFFF").pack(pady=2)
        self.caja_fecha2 = tk.Entry(marco_fechas, width=20, bg="#F3E5F5", fg="#222831")
        self.caja_fecha2.pack(pady=5)
        self.caja_fecha2.bind("<Return>", lambda event: self.calcular_dias())

        # Botón para calcular
        boton_fechas = tk.Button(marco_fechas, text="Calcular días",
                            command=self.calcular_dias, bg="#BA68C8", fg="#FFFFFF", activebackground="#CE93D8")
        boton_fechas.pack(pady=10)

        # Resultado
        self.resultado_dias = tk.Label(marco_fechas, text="Días: 0",
                                  font=("Arial", 11, "bold"), bg="#8E24AA", fg="#FFFFFF")
        self.resultado_dias.pack(pady=5)
    
    # FUNCIÓN QUE CONVIERTE EL DINERO
    def convertir_dinero(self):
        try:  # "Intenta hacer esto, si hay error, ve al except"
            # Obtenemos lo que escribió el usuario
            texto_pesos = self.caja_pesos.get()
            
            # Si no escribió nada, le decimos
            if texto_pesos == "":
                messagebox.showwarning("¡Ups!", "Escribe una cantidad primero")
                return
            
            # Convertimos el texto a número flotante
            pesos = float(texto_pesos)
            
            # Si es negativo, le entregamos una notificación de advertencia
            if pesos < 0:
                messagebox.showwarning("¡Ups!", "El dinero no puede ser negativo")
                return
            
            # Aquí están las tasas de cambio (cuántos pesos vale cada moneda)
            # Estos números cambian en la vida real, pero usamos estos como ejemplo
            pesos_por_dolar = 4000    # 1 dólar = 4000 pesos
            pesos_por_euro = 4300     # 1 euro = 4300 pesos  
            pesos_por_yuan = 550      # 1 yuan = 550 pesos
            
            # Hacemos las divisiones para convertir
            dolares = pesos / pesos_por_dolar
            euros = pesos / pesos_por_euro
            yuan = pesos / pesos_por_yuan
            
            # Actualizamos los textos que ve el usuario
            # :.2f significa "muestra solo 2 decimales"
            self.resultado_dolares.config(text=f"Dólares: ${dolares:.2f}")
            self.resultado_euros.config(text=f"Euros: €{euros:.2f}")
            self.resultado_yuan.config(text=f"Yuan: ¥{yuan:.2f}")
            
            # Le decimos que todo salió bien
            messagebox.showinfo("¡Listo!", "Conversión exitosa")
            
        except:  # Si hubo cualquier error
            messagebox.showerror("Error", "Escribe solo números, por favor")
    
    # FUNCIÓN QUE CONVIERTE LA TEMPERATURA
    def convertir_temperatura(self):
        try:  # Intentamos hacer la conversión
            # Obtenemos los grados Celsius que escribió
            texto_celsius = self.caja_celsius.get()
            
            # Si no escribió nada
            if texto_celsius == "":
                messagebox.showwarning("¡Ups!", "Escribe una temperatura primero")
                return
            
            # Convertimos a número
            celsius = float(texto_celsius)
            
            # Verificamos que no sea demasiado frío (cero absoluto = -273.15°C)
            if celsius < -273.15:
                messagebox.showwarning("¡Ups!", "Esa temperatura es imposible")
                return
            
            # FÓRMULAS PARA CONVERTIR:
            # Celsius a Fahrenheit: (C × 9/5) + 32
            fahrenheit = (celsius * 9/5) + 32
            
            # Celsius a Kelvin: C + 273.15
            kelvin = celsius + 273.15
            
            # Mostramos los resultados
            self.resultado_fahrenheit.config(text=f"Fahrenheit: {fahrenheit:.1f}°F")
            self.resultado_kelvin.config(text=f"Kelvin: {kelvin:.1f}K")
            
            # Mensaje de éxito
            messagebox.showinfo("¡Listo!", "Conversión exitosa")
            
        except:  # Si algo salió mal
            messagebox.showerror("Error", "Escribe solo números, por favor")
    
    # FUNCIÓN QUE CALCULA LOS DÍAS ENTRE FECHAS
    def calcular_dias(self):
        try:  # Intentamos calcular
            # Obtenemos las dos fechas que escribió
            fecha1_texto = self.caja_fecha1.get()
            fecha2_texto = self.caja_fecha2.get()
            
            # Si alguna está vacía
            if fecha1_texto == "" or fecha2_texto == "":
                messagebox.showwarning("¡Ups!", "Escribe las dos fechas")
                return
            
            # Convertimos el texto a fechas reales
            # strptime significa "convierte este texto a fecha"
            # %d/%m/%Y significa día/mes/año
            fecha1 = datetime.strptime(fecha1_texto, "%d/%m/%Y")
            fecha2 = datetime.strptime(fecha2_texto, "%d/%m/%Y")
            
            # Calculamos la diferencia entre las fechas
            diferencia = fecha2 - fecha1
            
            # Obtenemos solo los días (puede ser negativo si fecha2 es anterior)
            dias = diferencia.days
            
            # Si es negativo, lo convertimos a positivo
            if dias < 0:
                dias = dias * -1  # Multiplicar por -1 lo hace positivo
            
            # Mostramos el resultado
            self.resultado_dias.config(text=f"Días transcurridos: {dias}")
            
            # Mensaje de éxito
            messagebox.showinfo("¡Listo!", f"Han pasado {dias} días")
            
        except:  # Si la fecha está mal escrita
            messagebox.showerror("Error", 
                               "Escribe las fechas así: 25/12/2023")

# AQUÍ EMPIEZA EL PROGRAMA PRINCIPAL
def main():
    # Creamos la ventana principal
    ventana_principal = tk.Tk()
    
    # Creamos nuestra calculadora y le pasamos la ventana
    mi_calculadora = CalculadoraSimple(ventana_principal)
    
    # Iniciamos el programa (esto mantiene la ventana abierta)
    ventana_principal.mainloop()

# Esta línea significa "si ejecutan este archivo directamente, ejecuta main()"
if __name__ == "__main__":
    main()