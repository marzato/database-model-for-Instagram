import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__="user"
    id=Column(Integer, primary_key=True)
    email=Column(String(30), nullable=False)
    user_name=Column(String(12), nullable=False)
    first_name=Column(String(24), nullable=False)
    last_name=Column(String(24), nullable=False)
    password=Column(String(16), nullable=False)
    

    posts = relationship('Post', backref="author")
    post_likes = relationship('PostLike', backref = "user")
    comments = relationship('Comment', backref = "author")
    coment_likes = relationship('CommentLike', backref = "author")
    
    class Post(Base):
        __tablename__="post"
        id=Column(Integer,primary_key=True)
        user_id=Column(Integer,ForeignKey("user.id"))
        image_url=Column(String(20), nullable=False)
        date_published=Column(DateTime, nullable=False)
        content = Column(String(500))
        latitude = Column(String(20))
        longitude = Column(String(20))
        
    comments = relationship("Comment", backref = "post")
    likes = relationship("PostLike", backref = "post")


    class PostLike(Base):
        __tablename__ = "post_like"
        id = Column(Integer, primary_key=True) 
        user_id = Column(Integer, ForeignKey("user.id"))
        post_id = Column(Integer, ForeignKey("post.id"))

    class Comment(Base):
        __tablename__ = "comment"
        id= Column(Integer, primary_key=True)
        post_id = Column(Integer, ForeignKey("post.id"))
        user_id = Column(Integer, ForeignKey("user.id"))
        content = Column(String(200), nullable=False)
        date_time = Column(DateTime, nullable=False)

        likes = relationship("ComentLike", backref = "comment")

    class CommentLike(Base):
        __tablename__ = "comment_like"
        id= Column(Integer, primary_key=True)
        comment_id = Column(Integer,ForeignKey("comment.id"))
        user_id = Column(Integer, ForeignKey("user.id"))
        




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')