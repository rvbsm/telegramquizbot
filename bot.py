from var import *
import telebot
from telebot import types
import logging
from sqldb import SQLData

# Logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN)
db = SQLData('db.db')

# Changes the number of completed questions
def answerp():
	result = db.get_answer()
	global ans
	ans = convert(result)
	ans += 1

# Convert list to int
def convert(result):
	s = [str(i) for i in result]
	res = int("".join(s))
	return(res)

# One-time execution of tasks
def complete():
	if quest == 1:
		result = db.check_q1()
		global q1
		q1 = convert(result)
		q1 += 1
	elif quest == 2:
		result = db.check_q2()
		global q2
		q2 = convert(result)
		q2 += 1
	elif quest == 3:
		result = db.check_q3()
		global q3
		q3 = convert(result)
		q3 += 1
	elif quest == 4:
		result = db.check_q4()
		global q4
		q4 = convert(result)
		q4 += 1
	elif quest == 5:
		result = db.check_q5()
		global q5
		q5 = convert(result)
		q5 += 1
	else:
		pass

# Get variables from database 
def vars():
	result = db.check_q1()
	global q1
	q1 = convert(result)
	result = db.check_q2()
	global q2
	q2 = convert(result)
	result = db.check_q3()
	global q3
	q3 = convert(result)
	result = db.check_q4()
	global q4
	q4 = convert(result)

# Command /start
@bot.message_handler(commands=['start'])
def start(message):
	if not db.answer_exists(message.from_user.id):
		db.add_answer(message.from_user.id, 0)
		markup = types.InlineKeyboardMarkup()
		quest = types.InlineKeyboardButton('Задания', url='t.me/latotyad')
		markup.add(quest)
		bot.send_message(message.from_user.id, startm, reply_markup=markup, parse_mode='MarkdownV2')
	else:
		result = db.get_answer()
		ans = convert(result)
		markup = types.InlineKeyboardMarkup()
		quest = types.InlineKeyboardButton('Задания', url='t.me/latotyad')
		markup.add(quest)
		bot.send_message(message.from_user.id, '👾*Выполненых заданий\: {}*'.format(int(ans)), reply_markup=markup, parse_mode='MarkdownV2')

# Command /score
@bot.message_handler(commands=['score'])
def score(message):
	result = db.get_answer()
	ans = convert(result)
	markup = types.InlineKeyboardMarkup()
	quest = types.InlineKeyboardButton('Задания', url='t.me/latotyad')
	markup.add(quest)
	bot.send_message(message.from_user.id, '👾*Выполненых заданий\: {}*'.format(int(ans)), reply_markup=markup, parse_mode='MarkdownV2')

# First Question
@bot.message_handler(content_types=['text'])
def questions(message):
	vars()
	if message.text == answer_1 and q1 == 0:
		answerp()
		global quest
		quest = 1
		complete()
		db.update_q1(message.from_user.id, q1)
		db.update_answer(message.from_user.id, ans)
		bot.send_message(message.from_user.id, message_1, parse_mode='MarkdownV2')
	elif message.text == answer_2 and q2 == 0:
		answerp()
		quest = 2
		complete()
		db.update_q2(message.from_user.id, q2)
		db.update_answer(message.from_user.id, ans)
		bot.send_message(message.from_user.id, message_2, parse_mode='MarkdownV2')
	elif message.text == answer_3 and q3 == 0:
		answerp()
		quest = 3
		complete()
		db.update_q3(message.from_user.id, q3)
		db.update_answer(message.from_user.id, ans)
		bot.send_message(message.from_user.id, message_3, parse_mode='MarkdownV2')
	else:
		bot.send_message(message.from_user.id, no, parse_mode='MarkdownV2')

""" TEMPLATE FOR ANSWERS; n = number of question
	elif message.text == answer_n and qn == 0:
		answerp()
		global quest
		quest = n
		complete()
		db.update_qn(message.from_user.id, qn)
		db.update_answer(message.from_user.id, message_n, parse_mode='MarkdownV2')
"""

# Bot polling
if __name__ == '__main__':
	bot.polling(none_stop=False, interval=3, timeout=20)
	while True:
		pass