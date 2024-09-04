# Sentiment Analysis Chatbot Using Hugging Face Transformers

This project is a simple Sentiment Analysis Chatbot built using the Hugging Face Transformers library. It detects whether a user's input conveys a positive or negative sentiment and responds accordingly. The chatbot also recognizes basic greetings and farewells, providing intelligent and emoji-enhanced responses.


## Project Structure


├── chatbot.py            # Main chatbot logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation



## Features
- Sentiment Analysis: Classifies user input as positive, negative, or neutral using Hugging Face's `pipeline` for sentiment analysis.
- Basic Intent Recognition: Recognizes common greetings like "Hi" and farewells like "Goodbye" for a more natural conversation.
- Emoji Integration: Uses emojis to enhance chatbot responses, making the interactions more engaging.


## Technologies Used
- Python: Core programming language.
- Hugging Face Transformers: NLP library for using pre-trained models.
- Streamlit: Web app framework for deploying the chatbot (optional).



## Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/sentiment-analysis-chatbot.git
cd sentiment-analysis-chatbot


### 2. Create a virtual environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


### 3. Install the required dependencies

pip install -r requirements.txt


### 4. Run the Chatbot Locally

You can run the chatbot locally using Python. In the terminal, run the following command:
python chatbot.py

### 5. Deploy the Chatbot on Streamlit (Optional)

To showcase this project to recruiters, you can deploy it using Streamlit Cloud.
1. Install Streamlit if you haven’t already:

   pip install streamlit


2. Modify your chatbot script to work with Streamlit (if necessary).

3. Run the following command to launch it on Streamlit locally:
   streamlit run chatbot.py

4. If you want to deploy it, link your GitHub repository to Streamlit Cloud and deploy the app directly.




## Demo on Streamlit Cloud
