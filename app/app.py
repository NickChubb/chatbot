from flask import Flask, request
import chatbot
app = Flask(__name__)

@app.route('/')
def chatbot_api():
	message = request.args.get('message')
	if not message:
		return 'Message query string must not be empty.'
	return chatbot.query(message)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)