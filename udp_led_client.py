import network
import socket
import time

SSID = "NOMBRE_DE_TU_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Conectando...")
    time.sleep(1)

print("✅ Conectado a Wi-Fi")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ⚠️ Cambia esta IP por la IP que imprime tu servidor
SERVER_IP = "192.168.1.123"
PORT = 5005

while True:
    comando = input("Escribe 'on' para encender o 'off' para apagar: ")
    sock.sendto(comando.encode(), (SERVER_IP, PORT))
    print("Comando enviado:", comando)
