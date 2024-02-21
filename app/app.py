import os
from flask import Flask, request
import chatbot
from hashlib import sha256

app = Flask(__name__)

@app.route("/")
def chatbot_api():
    # API Authentication by hashed shared secret
    secret = request.args.get("secret")
    if not secret:
        return "No secret supplied."

    CHATBOT_API_SECRET = os.environ.get("CHATBOT_API_SECRET")
    if CHATBOT_API_SECRET is None:
        secret_file_path = '/run/secrets/CHATBOT_API_SECRET'
        if os.path.isfile(secret_file_path):
            with open(secret_file_path, 'r') as secret_file:
                CHATBOT_API_SECRET = secret_file.read().strip()
                os.environ['CHATBOT_API_SECRET'] = CHATBOT_API_SECRET
    
    if CHATBOT_API_SECRET is None:
        return "No secret set."

    hashedSecret = sha256(CHATBOT_API_SECRET.encode('utf-8')).hexdigest()
    if secret != hashedSecret:
        return "Incorrect secret supplied."

    # Call Chatbot to query OpenAI
    message = request.args.get("message")
    if not message:
        return "Message query string must not be empty."
    return chatbot.query(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
