
class DB:
    def save(self):
        print("Saved")

class Service:
    def __init__(self, db):   # 👈 injected
        self.db = db

    def process(self):
        self.db.save()


service = Service(DB())
service.process()