import openai
import gradio as gr

# OpenAI API Key
OPENAI_API_KEY=""

# Set OpenAI API Key
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chatbot_response(user_input):
    """Send user input to OpenAI API and return the response"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Launch web-based chatbot
iface = gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="AI Chatbot")
iface.launch()
