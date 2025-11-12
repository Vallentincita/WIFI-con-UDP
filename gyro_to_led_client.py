import network
import socket
import time
from machine import Pin, I2C
from struct import unpack

# --- Configuración del MPU6050 ---
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
MPU_ADDR = 0x68
i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')  # Despierta el sensor

def leer_gyro():
    datos = i2c.readfrom_mem(MPU_ADDR, 0x43, 6)
    gx, gy, gz = unpack(">hhh", datos)
    return gx / 131, gy / 131, gz / 131  # Conversión a °/s

# --- Conexión Wi-Fi ---
SSID = "NOMBRE_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando a Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
print("✅ Conectado a Wi-Fi:", wlan.ifconfig())

# --- Configura UDP ---
SERVER_IP = "192.168.1.123"  # 👉 cambia por la IP del servidor
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# --- Bucle principal ---
while True:
    gx, gy, gz = leer_gyro()
    print(f"GX={gx:.2f}, GY={gy:.2f}, GZ={gz:.2f}")
    
    # Detección de movimiento brusco
    if abs(gx) > 150 or abs(gy) > 150 or abs(gz) > 150:
        msg = "LED_ON"
    else:
        msg = "LED_OFF"
    
    sock.sendto(msg.encode(), (SERVER_IP, PORT))
    print("Enviado:", msg)
    time.sleep(0.5)
