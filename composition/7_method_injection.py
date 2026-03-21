"""
METHOD INJECTION
"""

class DB:
    def save(self):
        print("Saved")

class Service:
    def process(self, db):
        db.save()


service = Service()
service.process(DB())