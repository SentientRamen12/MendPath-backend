import os
from flask import Flask, request, jsonify
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
CORS(app)

client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)
@app.route("/")
def hello_word():
    return "Hello"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": open('prompt.txt', 'r').read().strip()
            },   
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3.1-70b",
        stream=True,
    )

    response_text = ''
    for chunk in stream:
        response_text += chunk.choices[0].delta.content or ""
        
    print(response_text)

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)