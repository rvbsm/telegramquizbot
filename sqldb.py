import sqlite3

class SQLData:

	def __init__(self, database):
		# Connect to database
		self.connection = sqlite3.connect(database, check_same_thread=False)
		self.cursor = self.connection.cursor()

	def get_answer(self):
		# Get completed questions
		result = self.cursor.execute("SELECT ans FROM correct").fetchall()
		for i in result:
			return [i[0] for i in result]

	def answer_exists(self, user_id):
		# Check if there is already a user in the database
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `correct` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))

	def add_answer(self, user_id, ans):
		# Add new user to database
		with self.connection:
			return self.cursor.execute("INSERT INTO `correct` (`user_id`, `ans`) VALUES(?,?)", (user_id,ans))

	def update_answer(self, user_id, ans):
		# Update completed questions by user in database
		with self.connection:
			return self.cursor.execute("UPDATE `correct` SET `ans` = ? WHERE `user_id` = ?", (ans, user_id))

# 1 Question
	# Get execution value
	def check_q1(self):
		with self.connection:
			result = self.cursor.execute("SELECT q1 FROM correct").fetchall()
			for i in result:
				return [i[0] for i in result]

	# Mark question completion
	def update_q1(self, user_id, q1):
		with self.connection:
			return self.cursor.execute("UPDATE correct SET q1 = ? WHERE user_id = ?", (q1, user_id))

# 2 Question
	def check_q2(self):
		with self.connection:
			result = self.cursor.execute("SELECT q2 FROM correct").fetchall()
			for i in result:
				return [i[0] for i in result]

	def update_q2(self, user_id, q2):
		with self.connection:
			return self.cursor.execute("UPDATE correct SET q2 = ? WHERE user_id = ?", (q2, user_id))

# 3 Question
	def check_q3(self):
		with self.connection:
			result = self.cursor.execute("SELECT q3 FROM correct").fetchall()
			for i in result:
				return [i[0] for i in result]

	def update_q3(self, user_id, q3):
		with self.connection:
			return self.cursor.execute("UPDATE correct SET q3 = ? WHERE user_id = ?", (q3, user_id))

# 4 Question
	def check_q4(self):
		with self.connection:
			result = self.cursor.execute("SELECT q4 FROM correct").fetchall()
			for i in result:
				return [i[0] for i in result]

	def update_q4(self, user_id, q4):
		with self.connection:
			return self.cursor.execute("UPDATE correct SET q4 = ? WHERE user_id = ?", (q4, user_id))

# 5 Question
	def check_q5(self):
		with self.connection:
			result = self.cursor.execute("SELECT q5 FROM correct").fetchall()
			for i in result:
				return [i[0] for i in result]

	def update_q5(self, user_id, q5):
		with self.connection:
			return self.cursor.execute("UPDATE correct SET q5 = ? WHERE user_id = ?", (q5, user_id))

# Close connection with Database
	def close(self):
		self.connection.close()