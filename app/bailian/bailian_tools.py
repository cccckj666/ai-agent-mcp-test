from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv() # 加载 .env
llm=ChatOpenAI(
    model="qwen-max-latest",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=SecretStr(os.getenv("DASHSCOPE_API_KEY")),
    streaming=True,
)
# 创建提示词模版
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一位{role}专家，擅长回答{domain}领域的问题"),
    ("user", "用户问题：{question}"),
])
# 模版+变量=>提示词
prompt=chat_prompt_template.format_messages(
    role="编程",
    domain="Web开发",
    question="如何构建一个基于Vue的前端应用？"
    )
resp=llm.stream(prompt)
for chunk in resp:
    print(chunk.content,end="",flush=True)