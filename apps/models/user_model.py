from apps.models import BaseModel
from exts import db


class Users(BaseModel):
    __tablename__ = 'users'
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

