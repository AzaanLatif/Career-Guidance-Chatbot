import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
import PyPDF2  # For PDF text extraction

# Load environment variables (for OpenAI API key)
load_dotenv()

# Initialize LLM (ChatOpenAI)
LLM = ChatOpenAI(model="gpt-4o-mini")  # Ensure this model is accessible from your OpenAI account

# Initialize memory
memory = ConversationBufferMemory()

# Define the prompt template to restrict responses to the content of the first aid PDF
prompt = ChatPromptTemplate.from_template(
    """You are a Career Guidance assistant that answers questions  based on the content of the provided Best Fields to Choose in Pakistan After FSc PDF.However if you dont find any relative answer from pdf you can answer from your own dataset
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
    
    # Save the interaction to memory
    memory.chat_memory.add_user_message(question)
    memory.chat_memory.add_ai_message(response)

    return response

# Main function to run the chatbot
if __name__ == "__main__":
    # Specify the path to your PDF file
    pdf_path = "./Fields to Choose in Pakistan After FSc.pdf"  # Change this to your actual first aid PDF file path
    
    # Extract text from the PDF
    pdf_content = extract_text_from_pdf(pdf_path)

    if "An error occurred" in pdf_content:
        print(pdf_content)  # Error in reading the PDF
    else:
        
        while True:
            # Ask the user for a question related to Career Guidance
            user_question = input("Enter a question about Career to choose after FSc in Pakistan: ")
            if user_question.lower() == 'exit':
                print("Good Bye ! Stay Safe. ")
                break
            
            # Generate and print the response
            print(generate_response(user_question, pdf_content))
