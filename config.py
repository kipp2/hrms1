import os 

class Config:
	SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/hRmSpayroll'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.urandom(24)

