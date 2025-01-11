import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
import PyPDF2
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Load environment variables (for OpenAI API key)
load_dotenv()

app = Flask(__name__)

# MongoDB setup
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['Chatbot']
    history_collection = db['History']
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Initialize LLM (ChatOpenAI)
LLM = ChatOpenAI(model="gpt-4o-mini")  # Ensure this model is accessible from your OpenAI account

# Initialize memory
memory = ConversationBufferMemory()

# Define the prompt template to restrict responses to the content of the first aid PDF
prompt = ChatPromptTemplate.from_template(
    """You are a Career Guidance assistant that answers questions based on the content of the provided Best Fields to Choose in Pakistan After FSc . However if you dont find any relative answer from pdf you can answer from your own dataset
    The content from the PDF is: {pdf_content}
    
    Previous conversation:
    {history}
    
    Question: {question}
    Please answer the question using only the information from the Best Fields to Choose in Pakistan After FSc PDF document."""
)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    """Extract text from the given PDF file."""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text()
        return text
    except Exception as e:
        return f"An error occurred while reading the PDF: {e}"

# Function to generate a response based on the PDF content
def generate_response(question, pdf_content):
    """Generate a response using the OpenAI model based on the extracted Best Fields to Choose in Pakistan After FSc PDF content."""
    # Format the prompt with the PDF content, the user's question, and the conversation history
    formatted_prompt = prompt.format(question=question, pdf_content=pdf_content, history=memory.buffer)
    response = LLM.predict(formatted_prompt)
    
    # Convert response to a list with bullet points
    response = response.replace("\n", "<br>")  # Replace newlines with <br> for HTML line breaks
    response = "<ul>" + "".join([f"<li>{item.strip()}</li>" for item in response.split("\n") if item.strip()]) + "</ul>"
    
    # Save the interaction to memory
    memory.chat_memory.add_user_message(question)
    memory.chat_memory.add_ai_message(response)

    # Save the interaction to MongoDB
    try:
        history_collection.insert_one({
            "timestamp": datetime.now(),
            "user_message": question,
            "bot_response": response
        })
        print("Chat history saved to MongoDB successfully!")
    except Exception as e:
        print(f"Error saving chat history to MongoDB: {e}")

    return response

# Specify the path to your PDF file
pdf_path = "./Fields to Choose in Pakistan After FSc.pdf"  # Change this to your actual PDF file path

# Extract text from the PDF
pdf_content = extract_text_from_pdf(pdf_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    if "An error occurred" in pdf_content:
        bot_response = "I'm sorry, but there was an error reading the career guidance information. Please try again later."
    else:
        bot_response = generate_response(user_message, pdf_content)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    if "An error occurred" in pdf_content:
        print(pdf_content)  # Error in reading the PDF
        exit(1)
    app.run(debug=True)