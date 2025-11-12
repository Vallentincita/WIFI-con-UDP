import network
import socket
import time

# --- Conexión Wi-Fi ---
SSID = "NOMBRE_DE_TU_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando a Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)

ip = wlan.ifconfig()[0]
print("✅ Servidor listo en IP:", ip)

# --- Configura el socket UDP ---
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, PORT))

print(f"📡 Escuchando en {ip}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(data.decode())
