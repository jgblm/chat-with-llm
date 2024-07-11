from dotenv import load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
)
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
chat_prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")
llm=ChatTongyi()
output_parser = StrOutputParser()
chain =chat_prompt|llm|output_parser
result = chain.invoke({"topic": "咖啡"})
print(result)