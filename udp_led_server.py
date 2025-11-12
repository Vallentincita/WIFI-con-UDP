import network
import socket
import time
from machine import Pin

# 💡 LED interno de la Pico 2 W
led = Pin("LED", Pin.OUT)

# 🛜 Configuración Wi-Fi
SSID = "NOMBRE_DE_TU_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Conectando...")
    time.sleep(1)

ip = wlan.ifconfig()[0]
print("✅ Conectado a Wi-Fi con IP:", ip)

# ⚙️ Configura el socket UDP
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, PORT))

print(f"Servidor UDP escuchando en {ip}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    mensaje = data.decode().strip().lower()
    print("Mensaje recibido:", mensaje, "de", addr)

    if mensaje == "on":
        led.value(1)
        print("💡 LED interno encendido")
    elif mensaje == "off":
        led.value(0)
        print("💤 LED interno apagado")
    else:
        print("Comando no reconocido")
