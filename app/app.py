from flask import Flask, request
import chatbot
import generator
from auth import auth_middleware

app = Flask(__name__)

app.wsgi_app = auth_middleware(app.wsgi_app)

@app.route("/chatbot")
def chatbot_api():
    # Call Chatbot to query OpenAI
    query = request.args.get("query")
    if not query:
        return "Query must not be null."
    return chatbot.query(query)

@app.route("/generator")
def generator_api():
    query = request.args.get("query")
    if not query:
        return "Query must not be empty."
    return chatbot.generate(query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
