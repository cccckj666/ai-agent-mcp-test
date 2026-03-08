from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
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
prompt_template = PromptTemplate.from_template("今天{something}真不错")
prompt=prompt_template.format(something="天气")
resp=llm.stream(prompt)
for chunk in resp:
    print(chunk.content,end="",flush=True)