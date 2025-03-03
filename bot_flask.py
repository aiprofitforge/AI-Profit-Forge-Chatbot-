from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

OPENAI_API_KEY = ""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}],
        api_key=OPENAI_API_KEY
    )
    
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(port=5000)
