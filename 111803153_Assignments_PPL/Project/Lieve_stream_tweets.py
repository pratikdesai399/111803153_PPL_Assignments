import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import time
import os
import subprocess

consumer_key = 'zzffHqO7syoqCs2XO8ZoU6V5G'
consumer_secret = 'yHMxaZ1SVJjJlwqheb4BruchbMShdwc6PT0uScSV8G0VNFiJlm'
access_token = '1248528052113424384-Bjq2wJOsrECdlkyMzwnXf9ALcjv0Y3'
access_token_secret = 'WJvrqaIchTju2XrIeeXYwujC3zWRo4dpF9uaxWYSG1vuh'
password = 'Palya2000*'


def connect(username, created_at, tweet, retweet_count, place , location):
	"""
	connect to MySQL database and insert twitter data
	"""
	try:
		con = mysql.connector.connect(host = 'localhost',
		database='twitterdb', user='root', password = password, charset = 'utf8')
		

		if con.is_connected():
			"""
			Insert twitter data
			"""
			cursor = con.cursor()
			# twitter, tweets
			query = "INSERT INTO tweets (username, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s)"
			cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))
			con.commit()
			
			
	except Error as e:
		print(e)

	cursor.close()
	con.close()

	return

# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):
	

	def on_connect(self):
		print("You are connected to the Twitter API")


	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false disconnects the stream
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""
	def on_data(self,data):
		
		try:
			raw_data = json.loads(data)

			if 'text' in raw_data:
				 
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None
				

				location = raw_data['user']['location']

				#insert data just collected into MySQL database
				connect(username, created_at, tweet, retweet_count, place, location)
				print("Tweet colleted at: {} ".format(str(created_at)))
		except Error as e:
			print(e)
            
            
            
            
if __name__== '__main__':

	

	# authentification so we can access twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api =tweepy.API(auth, wait_on_rate_limit=True)

	# create instance of Streamlistener
	listener = Streamlistener(api = api)
	stream = tweepy.Stream(auth, listener = listener)

	track = ['corona']
	
	# choose what we want to filter by
	stream.filter(track = track, languages = ['en'])
