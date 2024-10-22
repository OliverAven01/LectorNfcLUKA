import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from adafruit_pn532.i2c import PN532_I2C
from PIL import Image, ImageDraw
import time
import firebase_manager
import indicadores  # Importamos el nuevo m�dulo de indicadores
import playaudio  # Importamos el m�dulo para reproducir audio


# Configura el bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializa la pantalla OLED
oled = SSD1306_I2C(128, 64, i2c)

# Inicializa el PN532 (lector NFC)
pn532 = PN532_I2C(i2c, debug=False)
pn532.SAM_configuration()

# Borra la pantalla y muestra el mensaje inicial
def mostrar_mensaje_inicial():
    oled.fill(0)
    oled.show()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 20), "Realiza el pago", fill=255)
    draw.text((0, 40), "desde aqui", fill=255)
    oled.image(image)
    oled.show()

# Muestra un mensaje con el UID
def mostrar_uid(uid_display):
    oled.fill(0)
    oled.show()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), "Luka -", fill=255)
    draw.text((0, 20), uid_display, fill=255)
    oled.image(image)
    oled.show()

# Muestra confirmaci�n de pago exitoso
def mostrar_confirmacion():
    oled.fill(0)
    oled.show()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 20), "�Pago exitoso!", fill=255)
    draw.text((0, 40), "�Gracias!", fill=255)
    oled.image(image)
    oled.show()

# Muestra un mensaje de error
def mostrar_error():
    oled.fill(0)
    oled.show()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 20), "Error en el pago", fill=255)
    draw.text((0, 40), "Intente de nuevo", fill=255)
    oled.image(image)
    oled.show()

# Funci�n principal
def leer_nfc():
    monto = 5.0  # Monto predeterminado, puede ser din�mico si lo necesitas

    while True:
        mostrar_mensaje_inicial()  # Muestra mensaje inicial
        print("Esperando una tarjeta NFC...")
        uid = pn532.read_passive_target()

        if uid is not None:
            # Convierte el UID a una cadena hexadecimal
            uid_str = [hex(i) for i in uid]
            uid_display = ' '.join(uid_str)
            print(f"Tarjeta detectada con UID: {uid_display}")

            # Muestra el UID en la pantalla OLED
            mostrar_uid(uid_display)

            # Enviar los datos a Firebase
            try:
                firebase_manager.enviar_datos_nfc(uid_display, monto)
                time.sleep(1)  # Pausa antes de mostrar confirmaci�n
                mostrar_confirmacion()  # Muestra confirmaci�n de pago exitoso
                indicadores.indicar_exito()  # Indicar �xito con LED y buzzer
                playaudio.reproducir_exito()  # Reproduce el audio de �xito
            except Exception as e:
                print(f"Error enviando datos a Firebase: {e}")
                mostrar_error()  # Muestra mensaje de error
                indicadores.indicar_fallo()  # Indicar fallo con LED y buzzer
                playaudio.reproducir_error()  # Reproduce el audio de error

            # Pausa para permitir que el usuario vea la confirmaci�n o error
            time.sleep(2)  # Ajusta el tiempo seg�n sea necesario

            # Limpia la pantalla antes de volver al mensaje inicial
            oled.fill(0)
            oled.show()

            # Espera brevemente antes de permitir la siguiente lectura
            time.sleep(1)

if __name__ == "__main__":
    firebase_manager.init_firebase()  # Inicializa Firebase al inicio
    leer_nfc()
