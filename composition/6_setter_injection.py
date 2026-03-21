"""
SETTER INJECTION
"""

class Service:
    def set_db(self, db):
        self.db = db

    def process(self):
        self.db.save()


class DB:
    def save(self):
        print("Saved")


service = Service()
service.set_db(DB())
service.process()