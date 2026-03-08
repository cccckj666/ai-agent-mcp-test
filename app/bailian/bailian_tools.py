from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv() # 加载 .env
# safe_key=SecretStr(os.getenv("DASHSCOPE_API_KEY"))
llm=ChatOpenAI(
    model="qwen-max-latest",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    
    api_key=SecretStr(os.getenv("DASHSCOPE_API_KEY")),
    streaming=True,
)
print(llm)