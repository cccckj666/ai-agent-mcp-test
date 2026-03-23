import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(project_root)
from langchain_core.tools import Tool
from app.bailian.common import chat_prompt_template,llm

def add(a,b):
    return a + b

add_tool=Tool.from_function(
    func=add,
    name="add",
    description="add two numbers",
)

tool_dict={
    "add":add
}

llm_with_tools=llm.bind_tools([add_tool])  # 将工具绑定到模型上
chain=chat_prompt_template | llm_with_tools
resp=chain.invoke(input={"role":"计算","domain":"数学计算","question":"100+100=？"})
print(resp)

for tool_calls in resp.tool_calls:
    print(tool_calls)
    args=tool_calls["args"]
    print(args)
    func_name=tool_calls["name"]
    print(func_name)

    tool_func=tool_dict[func_name]
    tool_content=tool_func(int(args["__arg1"]),int(args["__arg2"]))
    print(tool_content)