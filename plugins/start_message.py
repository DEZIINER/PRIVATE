import datetime

command("start")
def start_command(update, context):
    user_id = update.message.from_user.id
    current_time = datetime.datetime.now()
    greeting = get_greeting(current_time.hour)
    context.bot.send_message(chat_id=user_id, text=f"Good {greeting}! Welcome to my bot. How can I assist you?")

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"
      
