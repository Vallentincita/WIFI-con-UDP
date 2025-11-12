import network
import socket
import time

# Conexión Wi-Fi
SSID = "NOMBRE_DE_TU_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while not wlan.isconnected():
    time.sleep(1)

print("Conectado a Wi-Fi:", wlan.ifconfig())

# Configura el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Cambia esta IP por la que imprimió el servidor
SERVER_IP = "192.168.1.123"
PORT = 5005

while True:
    msg = input("Escribe un mensaje para enviar: ")
    sock.sendto(msg.encode(), (SERVER_IP, PORT))
    print("Mensaje enviado!")
