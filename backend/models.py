# from flask_login import UserMixin
# from __init__ import db

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))


from __init__ import db
from flask_security import UserMixin, RoleMixin
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Roles_Users(db.Model):
    __tablename__ = "roles_users"
    id = Column(Integer(), primary_key=True)
    user_id = Column("user_id", Integer(), ForeignKey("user.id"))
    role_id = Column("role_id", Integer(), ForeignKey("role.id"))


class Role(db.Model, RoleMixin):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    # last_login_at = Column(DateTime())
    # current_login_at = Column(DateTime())
    # last_login_ip = Column(String(100))
    # current_login_ip = Column(String(100))
    # login_count = Column(Integer)
    active = Column(Boolean())
    # premium = Column(Boolean())
    # fs_uniquifier = Column(String(255), unique=True, nullable=False)
    # confirmed_at = Column(DateTime())
    roles = relationship(
        "Role", secondary="roles_users", backref=backref("users", lazy="dynamic")
    )


# CREATE TABLE IF NOT EXISTS User(
#     id INT AUTO_INCREMENT NOT NULL,
#     email VARCHAR(250),
#     username VARCHAR(250),
#     PASSWORD VARCHAR(250),
#     active BOOLEAN,
#     primary key (id)
# ); CREATE TABLE IF NOT EXISTS Role(
#     id INT AUTO_INCREMENT NOT NULL,
#     NAME VARCHAR(250),
#     description VARCHAR(250),
#     primary key (id)
# ); 
# CREATE TABLE IF NOT EXISTS Roles_users(
#     id INT AUTO_INCREMENT NOT NULL,
#     user_id INT,
#     role_id INT,
#     primary key (id),
# );

    # CONSTRAINT FK_PersonOrder2 FOREIGN KEY(role_id) REFERENCES Role(id),
    # CONSTRAINT FK_PersonOrder1 FOREIGN KEY(user_id) REFERENCES User(id)


# INSERT INTO `Roles_users` ( `user_id`, `role_id`) VALUES
# (1, 1);

# INSERT INTO `Role` (`NAME`, `description`) VALUES
# ('Admin', 'creating residents and editting views');
