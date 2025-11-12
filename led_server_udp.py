import network
import socket
import time
from machine import Pin

# --- LED interno ---
led = Pin("LED", Pin.OUT)

# --- Conexión Wi-Fi ---
SSID = "NOMBRE_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando a Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
ip = wlan.ifconfig()[0]
print("✅ Servidor en:", ip)

# --- Configura socket UDP ---
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, PORT))

print("📡 Esperando mensajes UDP...")

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode().strip()
    print("Mensaje recibido:", msg)
    
    if msg == "LED_ON":
        led.value(1)
    elif msg == "LED_OFF":
        led.value(0)
