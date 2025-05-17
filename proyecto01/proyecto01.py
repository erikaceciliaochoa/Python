
from gettext import install
import fpdf
import pip


pip 
install 
fpdf

#! pip install fpdf

proyecto = input("Digita la descripcion del proyecto: ")
horas_estimadas = input("Digita la cantidadd de horas estimadas: ")
valor_hora = input("Digita el valor de la hora trabajada: ")
tiempo_estimado = input("Digita el pazo estimado: ")
#Mi primer proyecto con Python
#120
#80
#2 meses
valor_total = int(horas_estimadas) * int(valor_hora)

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", 0, 0)

pdf.text(115, 145, proyecto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, tiempo_estimado)
pdf.text(115, 205, str(valor_total))

pdf.output("presupuesto.pdf")
print("Presupuesto generado con éxito!!!")
