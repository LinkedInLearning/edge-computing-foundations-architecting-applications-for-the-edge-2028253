from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GuestbookMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "message": self.message}
