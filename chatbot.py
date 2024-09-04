from transformers import pipeline

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

def get_response(user_input):
    # Lowercase the input for easier matching
    user_input = user_input.lower()

    # Check for common greetings or simple phrases first
    greetings = ['hi', 'hello', 'hey', 'greetings', 'what’s up']
    
    if user_input in greetings:
        return "Hello! 👋 How can I assist you today? 😊"

    # Check for common farewell phrases
    farewells = ['bye', 'goodbye', 'see you', 'take care']
    
    if any(farewell in user_input for farewell in farewells):
        return "Goodbye! 👋 Have a wonderful day! 🌞"

    # Analyze sentiment for other types of input
    result = sentiment_pipeline(user_input)
    sentiment = result[0]['label']
    
    # Create chatbot response based on sentiment
    if sentiment == 'POSITIVE':
        return "I'm glad you're feeling positive! 😃✨"
    elif sentiment == 'NEGATIVE':
        return "I'm sorry to hear that. 😔💔 How can I help?"
    else:
        return "Interesting... 🤔 Tell me more! 🧠"

