from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]
while (True):
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print('AI: ', res.content)

print(chat_history)