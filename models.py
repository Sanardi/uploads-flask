from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField

from datamodels.db import db


class User:
    user_id     =   IntegerField( unique=True )
    first_name  =   StringField( max_length=50 )
    last_name   =   StringField( max_length=50 )
    email       =   StringField( max_length=30, unique=True )
    password    =   StringField( )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    

class Course:
    courseID   =   StringField( max_length=10, unique=True )
    title       =  StringField( max_length=100 )
    description =  StringField( max_length=255 )
    credits     =  IntegerField()
    term        =  StringField( max_length=25 )

class Enrollment:
    user_id     =   IntegerField()
    courseID    =   StringField( max_length=10 )