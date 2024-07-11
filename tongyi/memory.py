from dotenv import load_dotenv
from langchain import ConversationChain
from langchain_community.llms import Tongyi

load_dotenv()
llm = Tongyi(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)
output = conversation.predict(input="Hi there! My name is ZhangSan")
print(output)
output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(output)
output = conversation.predict(input="who am i?")
print(output)