import RPi.GPIO as GPIO
import time

# Pines para los LEDs y el buzzer
PIN_LED_VERDE = 18
PIN_LED_ROJO = 23
PIN_BUZZER = 24

# Configuraci�n de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED_VERDE, GPIO.OUT)
GPIO.setup(PIN_LED_ROJO, GPIO.OUT)
GPIO.setup(PIN_BUZZER, GPIO.OUT)

# Funci�n para indicar �xito en el pago (LED verde y sonido de buzzer)
def indicar_exito():
    GPIO.output(PIN_LED_VERDE, GPIO.HIGH)  # Encender LED verde
    buzzer_sonido_exito()  # Sonido de confirmaci�n
    time.sleep(1)  # Mantener por 1 segundo
    GPIO.output(PIN_LED_VERDE, GPIO.LOW)  # Apagar LED verde

# Funci�n para indicar fallo en el pago (LED rojo y sonido de buzzer)
def indicar_fallo():
    GPIO.output(PIN_LED_ROJO, GPIO.HIGH)  # Encender LED rojo
    buzzer_sonido_fallo()  # Sonido de fallo
    time.sleep(1)  # Mantener por 1 segundo
    GPIO.output(PIN_LED_ROJO, GPIO.LOW)  # Apagar LED rojo

# Sonido de buzzer para �xito
def buzzer_sonido_exito():
    GPIO.output(PIN_BUZZER, GPIO.HIGH)  # Encender buzzer
    time.sleep(0.2)  # Mantener encendido por 200 ms
    GPIO.output(PIN_BUZZER, GPIO.LOW)  # Apagar buzzer
    time.sleep(0.1)  # Pausa de 100 ms
    GPIO.output(PIN_BUZZER, GPIO.HIGH)  # Encender buzzer nuevamente
    time.sleep(0.2)
    GPIO.output(PIN_BUZZER, GPIO.LOW)  # Apagar buzzer

# Sonido de buzzer para fallo
def buzzer_sonido_fallo():
    GPIO.output(PIN_BUZZER, GPIO.HIGH)  # Encender buzzer
    time.sleep(0.5)  # Mantener encendido por 500 ms
    GPIO.output(PIN_BUZZER, GPIO.LOW)  # Apagar buzzer
