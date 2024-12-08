from firebase_admin import db, credentials, initialize_app
import platform

class CheckCounter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CheckCounter, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            if platform.system() == "Windows":
                cred = credentials.Certificate("private/counter-script-firebase-adminsdk-c4vb0-f5029176fa.json")
            else:
                cred = credentials.Certificate("/etc/secrets/counter-script-firebase-adminsdk-c4vb0-f5029176fa.json")

            initialize_app(cred, {"databaseURL": "https://counter-script-default-rtdb.firebaseio.com"})

            self.initialized = True

    def call(self, number = 0):
        db_ref = db.reference(str(number))
        current = db_ref.get()
        next_value = 0

        if current == None:
            current = 0

        next_value = current + 1

        db_ref.set(next_value)

        return current

if __name__ == "__main__":
    print(CheckCounter().call(3))