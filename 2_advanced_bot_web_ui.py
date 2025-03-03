import openai
import gradio as gr
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Predefined FAQ Knowledge Base
FAQ_DATABASE = {
    "What are your business hours?": "Our business hours are Monday to Friday, 9 AM to 5 PM.",
    "How do I reset my password?": "To reset your password, go to the login page and click on 'Forgot Password'.",
    "Where is my order?": "You can track your order in the 'My Orders' section on our website."
}

def chatbot_response(user_input):
    """ AI Customer Support Chatbot with FAQ Handling """
    # Check if the user's question is in the FAQ database
    for question, answer in FAQ_DATABASE.items():
        if question.lower() in user_input.lower():
            return answer

    # If not in FAQ, send to OpenAI for a general response
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
iface = gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="AI Customer Support Bot")

# Run the chatbot
iface.launch()
