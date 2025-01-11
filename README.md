# Career Guidance Chatbot
# 📝 Description
This project is a Career Guidance Chatbot that assists users in making informed decisions about their career choices after completing FSc (Faculty of Science) in Pakistan. The chatbot uses natural language processing and machine learning techniques to provide personalized advice based on a PDF document containing information about various career fields in Pakistan.
# ✨ Features
- 💬 Web-based chat interface   
- 🎙️ Voice input support  
- 🔊 Text-to-speech functionality for bot responses
- 🗄️ MongoDB integration for chat history storage
- 📄 PDF-based knowledge extraction  
- 📱 Responsive design for various devices  

# 🔧 Technology Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **AI/ML**: Langchain, OpenAI GPT
- **PDF Processing**: PyPDF2
- **Speech Recognition**: Web Speech API
- **Text-to-Speech**: Web Speech API

# 🛠️ Prerequisites
Python 3.7+  
MongoDB  
OpenAI API key  

# 🚀 Setup Instructions
1.Clone the repository:

git clone https://github.com/your-username/career-guidance-chatbot.git
cd career-guidance-chatbot

2.Install required packages:

pip install -r requirements.txt

3.Set up environment variable: Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

4.Ensure MongoDB is running on your local machine (default port: 27017).

5.Place your PDF file (Fields to Choose in Pakistan After FSc.pdf) in the project root directory. 

# 🖥️ Usage
1.Run the Flask application:
  
- python app.py

2.Open a web browser and navigate to  http://localhost:5000.

3.Start chatting with the Career Guidance Chatbot by typing your questions or using voice input.

# 📁 File Structure
- app.py: Main Flask application  

- chatbot.py: Core chatbot logic using Langchain 

- index.html: Web interface for the chatbot 
Fields to Choose in Pakistan After FSc.pdf : Knowledge base for career guidance


# ℹ️ Additional Information
- The chatbot uses the GPT-4o-mini model from OpenAI. Ensure you have access to this model in your OpenAI account.

- The web interface supports both text and voice input, as well as text-to-speech for bot responses.

- Chat history is stored in MongoDB for future reference and analysis.

# 🙏 Acknowledgments
- This Career Guidance Chatbot was developed as part of our 7th-semester project in Computational Intelligence.
- We extend our heartfelt gratitude to Sir Hamas Ur Rehman for his invaluable guidance and teaching throughout the course.
- Special thanks to my project member, Osama Ahmad, for his unwavering support and contributions to this project.

# 📄 License
This project is licensed under the MIT License

# Author:
1. Azaan Latif  
2. Osama Ahmad