echo "Stopping Docker container: "; docker stop chatbot
echo "Removing Docker container: "; docker rm chatbot
echo "Building Docker image: "; docker build --tag=nickchubb/chatbot .
echo "Starting Docker container Chatbot..."; docker run -p 8080:8080 -e OPENAI_API_KEY=$OPENAI_API_KEY -e API_SECRET=$API_SECRET --name=chatbot nickchubb/chatbot