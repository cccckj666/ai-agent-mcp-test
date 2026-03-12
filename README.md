# AI Agent 编程智能体实战项目

##  项目简介
本项目基于 MCP 协议打造商业级 AI Agent，实现本地大模型驱动的自动化编程助手。

## 开发日志 (Dev Log)
- [2026-03-05] 完成环境初始化（使用`uv`进行环境管理）与Ollama 本地部署。
- [2026-03-05] 集成 LangChain 框架，成功实现 Python 脚本调用本地 DeepSeek 模型。
- [2026-03-07] **项目架构重构与云端集成**：
  - 将原 `main.py` 重命名为`ollama.py`，专职负责本地模型驱动。
  - 新增 `bailian.py`，接入阿里云百炼平台实现云端 Qwen3 模型调用。
  - 引入 `.env` 环境隔离机制，规范化管理 API Key 等敏感信息。
  - 新增 `bailian_qwq.py`，对接阿里云**QWQ-plus**推理模型。
- [2026-03-08] **目录优化与工具集成**：
  - 重构目录结构，将核心逻辑迁移至`app/`目录。
  - 新增`bailian_tools.py`，集成LangChain OpenAI接口调用Qwen-Max旗舰模型。
  - 实现`SecretStr`安全调用。
  - 引入LangChain`PromptTemplate`，学习提示词模版知识。
  - 成功实现动态参数注入提示词。
- [2026-03-11] **对话升级**：
  - 引入`ChatPromptTemplate`，实现 System/User 角色的结构化解耦。
  - 支持多变量（Role/Domain/Question）动态注入，提升模型在专业领域的表现。
  - 引入 `ChatMessagePromptTemplate`，实现消息体的原子化封装。
- [2026-03-12] **少样本学习实践**：
  - 引入 `FewShotPromptTemplate`，实现基于少样本学习（Few-Shot Learning）的提示词引导。
  - 通过 `examples` 数组动态构建上下文示例。
---

## 快速开始 (Getting Started)
### 1. 环境依赖
- **Python**: 3.9.13(uv管理)
- **Ollama**: 0.17.6

### 2. 模型部署
- 模型：`deepseek-r1:7b`
- 关键命令：`ollama run deepseek-r1:7b`
- **避坑点**：
  - 遇到端口 `11434` 占用报错，是因为 Ollama 后台服务已启动，无需重复执行 `serve`。
  - 如果 C 盘空间不足，建议配置 `OLLAMA_MODELS` 环境变量迁移模型路径。
  - 务必确保.env已加入.gitignore，严禁将API Key提交至公开仓库。

---

## 🛠 功能模块 (Features)
-  **基础环境搭建**: 使用 `uv` 实现高效的 Python 依赖管理。
-  **本地大模型部署**: 成功运行 `deepseek-r1:7b` 推理模型。
-  **模型交互层**: 封装 LangChain 调用接口。
-  **交互体验优化**: 实现 **Streaming (流式输出)**，消除模型生成的等待焦虑。
-  **工程化配置**：实现敏感信息与代码逻辑的完全解耦。
-  **流式交互优化**：针对推理模型实现Reasoning Content的独立渲染。
-  **安全类型增强**：采用Pydantic SecretStr。
-  **提示词工程**：集成LangChain PromptTemplate，支持结构化、动态化的提示词管理。
-  **结构化对话工程**：采用ChatPromptTemplate控制上下文。
-  **动态参数注入**：支持多维变量实时填充模版。
-  **提示词原子化**：采用ChatMessagePromptTemplate将消息体作为独立组件进行管理。
-  **少样本学习**：使用FewShotPromptTemplate，支持通过少量示例对模型进行即时微调。