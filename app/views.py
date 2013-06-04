from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
import twitter
from twitter import Api, Status
import time
from models import Tweet
#import other necessary files

@app.route('/')
@app.route('/nodb')
def index():
	search_term = "bills.com"
	print search_term
	api = Api(consumer_key='uy3Utit3PhWPmM5284sh7w',
			consumer_secret='zA6ps76R3ID2oRXXdUjQ7jsPgcmXD1rPsNYVSw', 
			access_token_key='61793468-PoarjfBLEa8KxtmFvNcLwFlvSGsh03U2LyNbroXye',
			access_token_secret='qg6cEIa33rX725oVAqmN4CtIgG0fmuPeI7pb2Vjeyxs')
	results = api.GetSearch(search_term)
	print results[0]
	tweets = []
	for r in results:
		user = r.GetUser()
		text = r.GetText()
		seconds_ago = r.GetCreatedAtInSeconds()
		hours_ago = ConvertTime(seconds_ago)
		source_url = r.GetSource()
		screenname = user.GetScreenName()
		image = user.GetProfileImageUrl()
		tweet = {"text": text, "hours_ago":hours_ago, "screenname": screenname}
		tweets.append(tweet)
	return render_template("index.html", tweets = tweets)

@app.route('/db')
def db():
	search_term = "bills.com"
	print search_term
	api = Api(consumer_key='uy3Utit3PhWPmM5284sh7w',
			consumer_secret='zA6ps76R3ID2oRXXdUjQ7jsPgcmXD1rPsNYVSw', 
			access_token_key='61793468-PoarjfBLEa8KxtmFvNcLwFlvSGsh03U2LyNbroXye',
			access_token_secret='qg6cEIa33rX725oVAqmN4CtIgG0fmuPeI7pb2Vjeyxs')
	results = api.GetSearch(search_term)
	tweets = []
	for r in results:
		user = r.GetUser()
		text = r.GetText()
		seconds_ago = r.GetCreatedAtInSeconds()
		hours_ago = ConvertTime(seconds_ago)
		source_url = r.GetSource()
		screenname = user.GetScreenName()
		image = user.GetProfileImageUrl()
		tweet = {"text": text, "hours_ago":hours_ago, "screenname": screenname}
		tweets.append(tweet)
		#Add each tweet to database.
		t = Tweet( author= screenname, body = text, is_read = False )
		db.session.add(t)
	db.session.commit()
	return render_template("index.html", )

def ConvertTime(epoch):
	return time.strftime('About %H hours ago', time.gmtime(epoch))

@app.route('/mark_as_read/<tweet>')
def mark_as_read(tweet):
	#get tweet id 
	#mark as read in the db
	return 'marked as read'