from firebase_admin import db, credentials, initialize_app

class CheckCounter:
    @staticmethod
    def call(number = 0):
        cred = credentials.Certificate("private/counter-script-firebase-adminsdk-c4vb0-f5029176fa.json")
        initialize_app(cred, {"databaseURL": "https://counter-script-default-rtdb.firebaseio.com"})

        db_ref = db.reference(str(number))
        current = db_ref.get()
        next_value = 0

        if current == None:
            current = 0

        next_value = current + 1

        db_ref.set(next_value)

        return current

if __name__ == "__main__":
    print(CheckCounter.call(3))