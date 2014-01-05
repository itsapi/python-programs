#!/usr/bin/env python
# -*- coding: utf-8 -*- 

degree = u'\N{DEGREE SIGN}'

import pywapi
import difflib
import re
import datetime
import random
import time

datetoday = datetime.date.today()
timetoday = datetime.datetime.today().time()
datestr = datetoday.strftime("%d/%m/%Y")
timestr = timetoday.strftime("%H:%M") 
weather = pywapi.get_weather_from_weather_com('UKXX0037')

try:
	weatherStr = 'The weather in Colchester is ' + weather['current_conditions']['text'].lower() + ' and ' + weather['current_conditions']['temperature'] + degree + 'C'
except:
	weatherStr = 'Cannot get weather data at this time. Try looking outside!'

logo = """\

            .. .777777777777$$$.. .   . .   
    .    . ...777::777777777$$$$+..     .   
      . . ....77....7777777$$$$$$....  .. . 
     . .......777,:777777$$$$$$$$.......    
      ........7777777777$$$$$$$$$....... . .
      .................~$$$$$$$$$........   
    ...77777777777777$$$$$$$$$$$$.======,.. 
    .7777777777777$$$$$$$$$$$$$$$.========  
    I777777777777$$$$$$$$$$$$$$$$.========~ 
    7777777777$7$$$$$$$$$$$$$$$$$.=========.    ----------Welcome to PAnIC!!!!---------
    77777777777$$$$$$$$$$$$$$$$$..=======++.    Python Artificial Intelligence Computer
    77777777$$$$$$$$$$$$$$$$$....=====+=+++.
    7777777$$$....====================+++++.
    777777$$$..======================++++++.
    777$$$$$$.====================+++++++++.
    77$$$$$$?.====================++++++++, 
     $$$$$$$?.=================+++++++++++  
      I$$$$$?.================++++++++++.. .
      ........=========,.................  .
      ........=============++++++.......   .
    .... .....============++.,+++..... .  . 
    .     ....==========+++....++....    . .
          . ..=========+++++.,+++..  ..   ..
     .  .      .======+++++++++.  . ..  ..  
      .  ..     ..   .+++.. ..        .  
"""

directions = """\
1. Head southeast on Park Road toward Boundary Road
2. Turn left onto Boundary Road
3. Turn left onto Colchester Road/B1028
4. Slight left onto St. Andrew's Avenue (A133)
   Go through 1 roundabout
5. At the roundabout, take the 1st exit and stay on St. Andrew's Avenue (A133)
   Continue to follow A133
   Go through 5 roundabouts
6. At the roundabout, take the 1st exit onto North Station Road
7. At the roundabout, take the 1st exit onto Middleborough
8. Continue onto North Hill
   Destination will be on the right
"""

Database = [
	['your name', 'My name is PAnIC, Python Artificial Intelligence Computer.'],
	['my name', 'I am not sure, you have not told me yet. What is your name?'],
	['old you', 'I do not have a birthday. I am not living and thus I was never born. However I was created by Geraint White, Charlie Callow and Henry Plumb on 4th July 2013.'],
	['you ok', 'I am very well thank you. How are you?', 'Not too bad, yourself?', 'I\'m fine, how about you?', 'Me? I\'m great, you?'],
	['you live', 'I exist everywhere and therefore have no one location.'],
	['old I', 'I am not sure, you have not told me yet. How old are you?'],
	['hello', 'Good day earthling!', 'Greetings', 'Howdy!', 'Hi there!'],
	['date', 'The date is ' + datestr],
	['time', 'The time is ' + timestr],
	['weather', weatherStr],
	['meaning of life', 'The answer to life, the universe and everything is 42'],
	['your opinion', 'I am a neutral party and therefore I like to keep my opinion to myself.', 'Always enjoyable.', 'Personally I\'m not interested at all.'],
	['favourite food', 'Raspberry Pie'],
	['you look like', 'Lots of symbols and characters'],
	['where am i', 'You are currently at the University of Essex'],
	['favourite colour', 'My favourite colour is green, the colour of circuit boards'],
	['direction Colchester Sixth Form', directions],
	['tell joke', "Three statisticians go out hunting together. After a while they spot a solitary rabbit. The first statistician takes aim and overshoots. The second aims and undershoots. The third shouts out: We got him!", "There are 10 types of people in the world: those who understand binary, and those who don't", "Bad command or file name! Go stand in the corner", "Does fuzzy logic tickle?", "Helpdesk : Sir, you need to add 10GB space to your HD , Customer : Could you please tell where I can download that?", "Sorry, the password you tried is already being used by Dorthy, please try something else.", "root:> Sorry, you entered the wrong password, the correct password is 'a_49qwXk'", "Man is the best computer we can put aboard a spacecraft...and the only one that can be mass produced with unskilled labour"],
	['thank you', 'You\'re welcome']
]


badFeel = ['sad', 'bad', 'terrible', 'awful', 'shit', 'crap', 'dreadful', 'distgusting', 'shite', 'rubbish', 'hate', 'dilike', 'digust', 'fuck']
goodFeel = ['good', 'great', 'superb', 'excellent', 'brilliant', 'wonderful', 'terrific', 'fantastic']

badResponse = ['Aww, poor you!', 'That\'s not good is it?', 'Hope you feel better soon!']
goodResponse = ['Glad to hear that', 'That\'s great', 'Excellent', 'Wonderful']

def matchword(phrase1,phrase2):
	return difflib.SequenceMatcher(None, phrase1, phrase2).ratio()

def phrasefilter(phrase):
	phrase = phrase.replace('hi', 'hello')
	phrase = phrase.replace('hey', 'hello')
	phrase = re.sub('[^A-Za-z0-9\s]+', '', phrase.lower())
	noise_words_set = ['of', 'the', 'at', 'for', 'in', 'and', 'is', 'from', 'are', 'our', 'it', 'its', 'was', 'when', 'how', 'what', 'like', 'whats', 'now', 'panic']
	return ' '.join(w for w in phrase.split() if w.lower() not in noise_words_set)

def getResponse(array):
	return random.choice(array[1:])

class panicBot():
	"""create new chatbot instance"""
	def __init__(self):
		print logo
		self.prevResponse = ''
		self.user = {
			'name': '',
			'age': '',
			'location': ''
		}

	def takeInput(self, message):
		out = ''
		if self.prevResponse in Database[3]:
			response = phrasefilter(message)
			responseType = 1
			for word in response.split(' '):
				if word in badFeel:
					responseType = 0
				elif word in goodFeel:
					responseType = 1
			if responseType:
				output = random.choice(goodResponse)
			else:
				output = random.choice(badResponse)
			out += '\n' + output + '\n'
			self.prevResponse = ''
		elif self.prevResponse == (Database[0][1] + ' What is your name?') or self.prevResponse == Database[1][1]:
			name = message
			self.user['name'] = name
			print '\n' + random.choice(['Hello ' + name, 'Hi ' + name, 'Howdy ' + name]) + '\n'
			self.prevResponse = ''
		elif self.prevResponse == (Database[2][1] + ' How old are you?') or self.prevResponse == Database[5][1]:
			age = message
			self.user['age'] = age
			out += '\n' + 'Awesome, I\'ll remember that.' + '\n'
			self.prevResponse = ''
		elif self.prevResponse == (Database[4][1] + ' Where do you live?'):
			location = message
			self.user['location'] = location
			out += '\n' + 'I\'m sure it\'s lovely there.' + '\n'
			self.prevResponse = ''
		else:
			var = phrasefilter(message)
			vals = []
			for i in range(len(Database)):
				vals.append(matchword(var, Database[i][0]))
			maxVal = [0,0]
			for i in range(len(vals)):
				if vals[i] > maxVal[0]:
					maxVal[0] = vals[i]
					maxVal[1] = i
			if maxVal[0] > 0.55:
				if maxVal[1] == 0:
					if self.user['name'] == '':
						self.prevResponse = Database[maxVal[1]][1] + ' What is your name?'
					else:
						self.prevResponse = Database[maxVal[1]][1]
				elif maxVal[1] == 1:
					if self.user['name'] == '':
						self.prevResponse = Database[maxVal[1]][1]
					else:
						self.prevResponse = 'Your name is ' + self.user['name']
				elif maxVal[1] == 2:
					if self.user['age'] == '':
						self.prevResponse = Database[maxVal[1]][1] + ' How old are you?'
					else:
						self.prevResponse = Database[maxVal[1]][1]
				elif maxVal[1] == 4:
					if self.user['name'] == '':
						self.prevResponse = Database[maxVal[1]][1] + ' Where do you live?'
					else:
						self.prevResponse = Database[maxVal[1]][1]
				elif maxVal[1] == 5:
					if self.user['age'] == '':
						self.prevResponse = Database[maxVal[1]][1]
					else:
						self.prevResponse = 'You are ' + self.user['age'] + ' years old'
				elif maxVal[1] == 16:
					out += '\nFinding directions ...\n'
					self.prevResponse = directions
					time.sleep(2)
				else:
					self.prevResponse = getResponse(Database[maxVal[1]])
			else:
				self.prevResponse = random.choice(['Sorry, I don\'t understand', 'I don\'t know what you mean', 'Sorry, I don\'t get that', 'You\'ve lost me there'])
			out += '\n' + self.prevResponse + '\n'
		return out
