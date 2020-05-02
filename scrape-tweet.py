import os
from telegram_send import telegram_bot_sendtext
import datetime
import time

def monstertweet(date_since,date_until):
	print(date_since,date_until)
	query='twint -s virseccon -s bug --since "'+date_since+'" --until "'+date_until+'"' 
	print(query)
	c=os.popen(query).read()
	print(c)
	data=c.split("\n")
	data.pop()

	for i in data:

		s=i.split("EDT")
		s_data=str(s[1]) 
		print(s_data)
		'''# symbol has removed due to inadequate input handling of the telegram api'''	
		s_data=s_data.replace("#",'@')
		print(s_data)
		print(telegram_bot_sendtext(s_data))

if __name__ == "__main__" :

        date_since = datetime.datetime.now()
	date_since=str(date_since).split(".")
	time.sleep(1000)
        date_until = datetime.datetime.now()
        date_until=str(date_until).split(".") 
	monstertweet(date_since[0],date_until[0])



