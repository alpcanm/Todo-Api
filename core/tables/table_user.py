from __init__ import db
from datetime import datetime
from core.models.model_user import UserModel


class TableUser(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mail = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    password = db.Column(db.String(64))
    phone_number = db.Column(db.String(15))
    photo_url = db.Column(db.String(300))
    mail_verified = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name

    @classmethod
    def defineTable(cls, dictUser: UserModel):
        return cls(
            name=dictUser.name,
            surname=dictUser.surname,
            mail=dictUser.mail,
            password=dictUser.password,
            phone_number=dictUser.phone_number,
            created_at=dictUser.created_at,
            mail_verified=dictUser.mail_verified,
            photo_url=dictUser.photo_url)
