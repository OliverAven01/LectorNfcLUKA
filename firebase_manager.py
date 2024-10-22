import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa Firebase solo una vez y reutiliza la conexi�n
firebase_app = None
db = None

def init_firebase():
    global firebase_app, db
    if not firebase_admin._apps:  # Verifica si Firebase ya est� inicializado
        cred = credentials.Certificate("luka-80406-firebase-adminsdk-ymnk0-fe576fb5d1.json")
        firebase_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
    return db

def enviar_datos_nfc(uid, monto):
    if db is None:
        init_firebase()  # Aseg�rate de que Firebase est� inicializado
    data = {
        'uid': uid,
        'monto': monto,
        'fecha': firestore.SERVER_TIMESTAMP
    }
    db.collection('nfcTags').add(data)
    print(f'Datos enviados: {data}')