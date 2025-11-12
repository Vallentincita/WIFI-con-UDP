import network
import socket
import time
from machine import Pin, I2C
from struct import unpack

# --- Configuración del MPU6050 ---
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # Usa GP5 (SCL) y GP4 (SDA)
MPU_ADDR = 0x68

# Despierta el sensor (quita modo sleep)
i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')

def leer_gyro():
    # Leer los registros del giroscopio (0x43 a 0x48)
    datos = i2c.readfrom_mem(MPU_ADDR, 0x43, 6)
    gx, gy, gz = unpack(">hhh", datos)
    return gx / 131, gy / 131, gz / 131  # Convierte a grados/segundo

# --- Conecta al Wi-Fi ---
SSID = "NOMBRE_DE_TU_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando a Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)

print("✅ Conectado a Wi-Fi:", wlan.ifconfig())

# --- Configura el socket UDP ---
SERVER_IP = "192.168.1.123"  # 👉 Cambia por la IP del servidor
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# --- Bucle principal ---
while True:
    gx, gy, gz = leer_gyro()
    mensaje = f"GYRO -> X:{gx:.2f}, Y:{gy:.2f}, Z:{gz:.2f}"
    sock.sendto(mensaje.encode(), (SERVER_IP, PORT))
    print("Enviado:", mensaje)
    time.sleep(1)
