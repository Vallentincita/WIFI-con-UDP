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
ip = wlan.ifconfig()[0]
port = 5005

# Configura el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))
print(f"Servidor UDP escuchando en {ip}:{port}")

while True:
    data, addr = sock.recvfrom(1024)
    print("Mensaje recibido:", data.decode(), "de", addr)
