from app import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime)
    title = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    isComplete = db.Column(db.Boolean, default=False)
    
