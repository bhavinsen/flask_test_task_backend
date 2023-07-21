from app.db import db


class About(db.Model):
    __tablename__ = 'about_table'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text)
    
    def __repr__(self) -> str:
        return str(self.id)
