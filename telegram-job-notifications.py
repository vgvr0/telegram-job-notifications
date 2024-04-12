import telebot, sqlite3
from telebot import types

# Replace 'YOUR_API_TOKEN' with the actual token provided by @BotFather
API_TOKEN = 'XXXXXXXXXXXXXXXXXXX'
bot = telebot.TeleBot(API_TOKEN)

user_choices = {}

# Handler for the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    surname = message.from_user.last_name
    alias = message.from_user.username

    # Print user data ¡
    print(f"User ID: {user_id}")
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Alias: {alias}")

    # Send welcome message and the category keyboard
    bot.reply_to(message, f"Hello {name}! What category would you like to receive job alerts for?",
                 reply_markup=teclado.k_category())

# General handler with category, experience and salary
@bot.message_handler(func=lambda message: True)
def handle_categories(message):
    user_id = message.from_user.id
    if user_id not in user_choices:
        # Store the category choice
        user_choices[user_id] = {"category": message.text}
        # Show job experience options
        reply_markup = teclado.k_experience()
        bot.reply_to(message, "Select your job experience:", reply_markup=reply_markup)

    elif "experience" not in user_choices[user_id]:
        # Store the job experience choice
        user_choices[user_id]["experience"] = message.text
        # Show salary options
        reply_markup = teclado.k_salary()
        bot.reply_to(message, "Select your desired salary:", reply_markup=reply_markup)

    elif "salary" not in user_choices[user_id]:
        # Store the salary choice
        user_choices[user_id]["salary"] = message.text

        # Save the user preferences to the JSON file and the database
        add_user_preferences_to_database(user_id, user_choices[user_id])

        # Show the user preferences
        category = user_choices[user_id]["category"]
        experience = user_choices[user_id]["experience"]
        salary = user_choices[user_id]["salary"]
        
        preferences_message = f"Your preferences:\n\nCategory: {category}\nExperience: {experience} years \nSalary: {salary} thousand €"
        bot.reply_to(message, preferences_message, reply_markup=None)

# Connect to the database using SQLite3 and save user_choices
def add_user_preferences_to_database(user_id, preferences):
    conn = sqlite3.connect('user_preferences.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_preferences (
                        user_id INTEGER PRIMARY KEY,
                        category TEXT,
                        experience TEXT,
                        salary TEXT
                    )''')

    category = preferences["category"]
    experience = preferences["experience"]
    salary = preferences["salary"]

    cursor.execute('''INSERT INTO user_preferences (user_id, category, experience, salary)
                      VALUES (?, ?, ?, ?)''', (user_id, category, experience, salary))
    
    conn.commit()
    conn.close()

# Class to generate keyboard options
class KeyboardCreator:
    def k_category(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        categories = ["Data Engineer", "Data Scientist", "Data Analyst", "Machine Learning Engineer", "Others"]
        for category in categories:
            keyboard.add(category)
        return keyboard

    def k_experience(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        experience_options = ["Less than 2 years", "2-5 years", "More than 5 years"]
        for option in experience_options:
            keyboard.add(option)
        return keyboard

    def k_salary(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        salary_options = ["<18", "18-30", "30-55", ">55"]
        for option in salary_options:
            keyboard.add(option)
        return keyboard

teclado = KeyboardCreator()

# Run the bot
bot.polling()