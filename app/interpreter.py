# command line interpreter for the chatbot
import chatbot

if __name__ == '__main__':
  while True:
    message = input('Ask a question: ')
    response = chatbot.query(message)
    print(response)