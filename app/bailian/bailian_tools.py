from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,ChatMessagePromptTemplate
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
# 模版+变量=>提示词
prompt=chat_prompt_template.format_messages(
    role="编程",
    domain="Web开发",
    question="你擅长什么？"
    )
print(prompt)
resp=llm.stream(prompt)
for chunk in resp:
    print(chunk.content,end="",flush=True)