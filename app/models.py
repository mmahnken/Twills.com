from app import db
from hashlib import md5

class Tweet(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String(120), index = True, unique = True)
	body = db.Column(db.String(190), index = True, unique = False)
	is_read = db.Column(db.Boolean)