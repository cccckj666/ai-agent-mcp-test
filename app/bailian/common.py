import os
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from langchain_core.prompts import ChatPromptTemplate,ChatMessagePromptTemplate

from dotenv import load_dotenv
load_dotenv() # 加载 .env
llm=ChatOpenAI(
    model="qwen-max-latest",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=SecretStr(os.getenv("DASHSCOPE_API_KEY")),
    streaming=True,
)

system_message_template=ChatMessagePromptTemplate.from_template(
    template="你是一位{role}专家，擅长回答{domain}领域的问题",
    role="system",
)
human_message_template=ChatMessagePromptTemplate.from_template(
    template="用户问题：{question}",
    role="user",
)
# 创建提示词模版
chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template
])