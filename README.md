# AI Agent 编程智能体实战项目

##  项目简介
本项目基于 MCP 协议打造商业级 AI Agent，实现本地大模型驱动的自动化编程助手。

## 开发日志 (Dev Log)
- [2026-03-05] 完成环境初始化（使用`uv`进行环境管理）与Ollama 本地部署。
- [2026-03-05] 集成 LangChain 框架，成功实现 Python 脚本调用本地 DeepSeek 模型。

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

---

## 🛠 功能模块 (Features)
-  **基础环境搭建**: 使用 `uv` 实现高效的 Python 依赖管理。
-  **本地大模型部署**: 成功运行 `deepseek-r1:7b` 推理模型。
-  **模型交互层**: 封装 LangChain 调用接口。
-  **交互体验优化**: 实现 **Streaming (流式输出)**，消除模型生成的等待焦虑。