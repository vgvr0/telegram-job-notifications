# Telegram Job Alert Bot

This Telegram bot allows users to set their job preferences and receive job alerts based on their chosen category, experience level, and salary range.

## Getting Started

These instructions will help you set up and run the Telegram Job Alert Bot on your local machine.

### Prerequisites

- Python 3 installed on your machine
- SQLite3 database engine

### Installing

1. Clone this repository to your local machine.

```
git clone https://github.com/yourusername/telegram-job-alert-bot.git
```

2. Navigate to the project directory.

```
cd telegram-job-alert-bot
```

3. Install the required Python packages using pip.

```
pip install -r requirements.txt
```

4. Replace `'YOUR_API_TOKEN'` with your actual Telegram Bot API token obtained from @BotFather.

```python
API_TOKEN = 'YOUR_API_TOKEN'
```

### Usage

1. Run the bot script.

```
python bot.py
```

2. Start a conversation with the bot in Telegram by searching for its username and sending the `/start` command.

3. Follow the prompts to select your job preferences, including category, experience level, and desired salary.

4. Once you have selected your preferences, the bot will save them and provide you with a confirmation message.

### Data Storage

- User preferences are stored in a SQLite3 database named `user_preferences.db`.
- The bot does not store any sensitive user information and only saves job preferences provided by the user.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
