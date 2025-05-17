import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Digita código de la acción: ") # Acá podemos usar acción EC

data = yfinance.Ticker(ticker).history("6mo")
cierre = data.Close

maxima = round(cierre.max(), 2)
minima = round(cierre.min(), 2)
valor_medio = round(cierre.mean(), 2) # media

destinatario = "erikaceciliaochoa@gmail.com"
asunto = "Análisis acciones últimos 6 meses" 
mensaje = f"""
Hola Zai,
Accá te envio el analisis de las acciones de los últimos 6 meses de {ticker}:
Cotización máxima: USD {maxima}
Cotización mínima: USD {minima}
Valor medio : USD {valor_medio}

Cualquier cosa me cuentas.

Erika
"""

#Abrir el navegador para ir a gmail
webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
time.sleep(3) #3 segundos

pyautogui.PAUSE = 3

# Click en el botón redactar/compose
pyautogui.click(84, 183)

# Escribir el destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Escribir el asunto
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Escribir el mensaje
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

# Click botón enviar
pyautogui.click(859, 697)

# Cerrar gmail
pyautogui.hotkey("ctrl", "f4")