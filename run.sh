echo "Stopping Docker container: "; docker stop chatbot
echo "Removing Docker container: "; docker rm chatbot
echo "Starting Docker container Chatbot..."; docker run -p 8080:8080 -e OPENAI_API_KEY=$OPENAI_API_KEY --name=chatbot nickchubb/chatbot