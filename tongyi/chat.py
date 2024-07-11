from dotenv import load_dotenv
from langchain.schema import (
    HumanMessage
)
from langchain_community.chat_models import ChatTongyi

load_dotenv()
chat = ChatTongyi(temperature=0)
result = chat([HumanMessage(content="Translate this sentence from English to Chinese. I love programming.")])
print(result)