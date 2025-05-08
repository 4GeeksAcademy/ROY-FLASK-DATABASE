from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(unique=True, nullable =False)
    lastname:Mapped[str]=mapped_column(unique=True, nullable =False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    follow:Mapped[list["Follower"]]=relationship(back_populates="followers")
    followinn:Mapped[list["Follower"]]=relationship(back_populates="following")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Follower(db.Model):
    __tablename__='followwesinout'
    user_from_id:Mapped[int]=mapped_column(ForeignKey('user.id'),primary_key=True)
    user_to_id:Mapped[int]=mapped_column(ForeignKey('user.id'),primary_key=True)
    followers:Mapped["User"]=relationship(back_populates="follow")
    following:Mapped["User"]=relationship(back_populates="followinn")
    

class Posts(db.Model):
    __tablename__='posts'
    id:Mapped[int]=mapped_column(primary_key=True)
   
    medias:Mapped[list["Medias"]]=relationship(back_populates="post")
    

class Medias(db.Model):
   __tablename__='medias'
   id:Mapped[int]=mapped_column(primary_key=True)
   url:Mapped[str]=mapped_column(unique=True, nullable =False)
   type:Mapped[int]=mapped_column(nullable=False)
   post:Mapped["Posts"]=relationship(back_populates="medias")
   post_id:Mapped[int]=mapped_column(ForeignKey('posts.id'))
  