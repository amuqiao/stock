# qwen3.5-plus 模型配置指南

根据分析的文档和配置文件，以下是配置 qwen3.5-plus 模型的详细步骤和示例：

## 1. 配置方式选择

系统支持两种配置模式：
- **渠道模式**：推荐，支持多模型共存
- **Legacy 模式**：单模型简单配置

## 2. 渠道模式配置（推荐）

### 步骤：
1. 登录 [通义千问控制台](https://dashscope.aliyun.com) 获取 API Key
2. 在 `.env` 文件中添加以下配置：

```env
# 多渠道配置
LLM_CHANNELS=dashscope

# 通义千问配置
LLM_DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_DASHSCOPE_API_KEY=your_dashscope_api_key_here
LLM_DASHSCOPE_MODELS=qwen3.5-plus,qwen-plus,qwen-turbo

# 主模型设置（可选，若不设置则使用默认模型）
LITELLM_MODEL=dashscope/qwen3.5-plus
```

### 说明：
- `LLM_CHANNELS`：指定使用 dashscope 渠道
- `LLM_DASHSCOPE_BASE_URL`：通义千问的 API 地址（固定）
- `LLM_DASHSCOPE_API_KEY`：替换为你的实际 API Key
- `LLM_DASHSCOPE_MODELS`：配置可用的模型列表，包含 qwen3.5-plus
- `LITELLM_MODEL`：设置默认使用的模型，格式为 `provider/model`

## 3. Legacy 模式配置（备选）

### 步骤：
1. 登录 [通义千问控制台](https://dashscope.aliyun.com) 获取 API Key
2. 在 `.env` 文件中添加以下配置：

```env
# 通义千问 API Key
DASHSCOPE_API_KEY=your_dashscope_api_key_here

# 主模型设置（可选）
LITELLM_MODEL=dashscope/qwen3.5-plus
```

### 说明：
- `DASHSCOPE_API_KEY`：替换为你的实际 API Key
- `LITELLM_MODEL`：设置默认使用的模型，格式为 `provider/model`

## 4. 配置验证和测试

### 验证配置结构：
```bash
python test_env.py --config
```

### 测试 LLM 连接：
```bash
python test_env.py --llm
```

## 5. 注意事项

1. **API Key 安全**：不要将 API Key 提交到版本控制系统
2. **模型名称**：使用 `qwen3.5-plus`（渠道模式）或 `dashscope/qwen3.5-plus`（指定主模型时）
3. **多 Key 负载均衡**：支持 `LLM_DASHSCOPE_API_KEYS=key1,key2` 格式
4. **优先级**：渠道模式优先级高于 Legacy 模式，配置渠道后 Legacy 配置会被忽略
5. **图片识别**：若需要使用图片识别功能，建议同时配置 Vision 模型，如 `VISION_MODEL=gemini/gemini-2.0-flash`

## 6. 完整配置示例

### 渠道模式完整示例：
```env
# 多渠道配置
LLM_CHANNELS=dashscope

# 通义千问配置
LLM_DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
LLM_DASHSCOPE_MODELS=qwen3.5-plus,qwen-plus,qwen-turbo

# 主模型设置
LITELLM_MODEL=dashscope/qwen3.5-plus

# 备选模型（可选）
LITELLM_FALLBACK_MODELS=anthropic/claude-3-5-sonnet-20241022,openai/gpt-4o-mini
```

### Legacy 模式完整示例：
```env
# 通义千问 API Key
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

# 主模型设置
LITELLM_MODEL=dashscope/qwen3.5-plus
```

配置完成后，系统会自动使用 qwen3.5-plus 模型进行股票分析和对话。