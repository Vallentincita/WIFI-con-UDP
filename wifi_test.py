import network
import time

# Configura tus credenciales Wi-Fi
SSID = "NOMBRE_DE_TU_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

# Activa la interfaz Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Espera hasta que se conecte
print("Conectando a Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)

print("✅ Conectado a Wi-Fi!")
print("Dirección IP:", wlan.ifconfig()[0])
