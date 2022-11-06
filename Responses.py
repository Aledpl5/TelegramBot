from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "ciao"):
        return "Hi"

    if user_message in ("who are you", "chi sei?", "who are you?", "chi sei"):
        return "I am ale04 test bot"
    
    if user_message in ("time", "time?"):
        return datetime.now().strftime("%d/%m/%y, %H:%M:%S")
        
    return "Non capisco cosa vuoi fare"