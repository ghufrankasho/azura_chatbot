from flask import Flask, render_template, request, jsonify
import openai
import os
from langchain.chat_models import AzureChatOpenAI
app = Flask(__name__)

# Set your OpenAI API key here


os.environ['OPENAI_API_KEY'] = os.getenv("AZURE_OPENAI_API_KEY")
os.environ['OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2023-07-01-preview'
os.environ['OPENAI_API_BASE'] = 'https://ubio-ai-aiservices-157053665.openai.azure.com/'


llm = AzureChatOpenAI(
    deployment_name="gpt-35-turbo",
    model_name="gpt-35-turbo"
)
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to understand string theory.")
]
@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']



    # now create a new user prompt
    prompt = HumanMessage(
        content=user_input
    )
    # add to messages
    messages.append(prompt)

    # send to chat-gpt
    res = llm(messages)


    bot_response = res.content

    return jsonify({'bot_response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
