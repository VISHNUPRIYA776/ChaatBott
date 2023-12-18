import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import defaultdict

# Sample data for IIT Mandi's School of Management
data = {
    "admission": "The admission process involves...",
    "programs": "We offer various programs such as...",
    # Add more queries and responses here
}

# Tokenization, Lemmatization, and Stopwords removal
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

# Build word index for faster lookup
word_index = defaultdict(list)
for key, value in data.items():
    for word in preprocess_text(key):
        word_index[word].append(key)

# Function to retrieve response based on user query
def get_response(query):
    tokens = preprocess_text(query)
    matches = []
    for token in tokens:
        matches.extend(word_index[token])

    if matches:
        return data[matches[0]]  # Return the first matched response
    else:
        return "Sorry, I don't have information about that."

# Streamlit App
import streamlit as st

st.title("IIT Mandi School of Management Chatbot")

# Streamlit UI
user_input = st.text_input("You: ", "")

if st.button("Ask"):
    response = get_response(user_input)
    st.text_area("Bot: ", value=response, height=200)

