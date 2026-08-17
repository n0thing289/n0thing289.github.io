---
name: model-routing-three-tier
description: "Route: simple→flash, complex→pro-delegate, vision→Qwen."
version: 2.2.0
author: Hermes Agent
---

# Three-Tier Model Routing

## ⚠️ 强制执行规则

**每次用户发出任务时，你在回复之前必须先执行下面的难度评估流程。不允许跳过此步骤直接开始执行任务。**

---

## Step 1 — 难度评估（强制）

在开始任何实质性工作前，先停下来自问以下问题。**至少中 1 条即判定为复杂任务：**

### 🟢 标记为「简单」的条件（全都满足才算简单）

- [ ] 单步操作（问一个问题、查一个信息、一个简单命令）
- [ ] 不需要创建/修改多个文件
- [ ] 不需要深度推理、调试排错、多轮探索
- [ ] 执行时间预估 < 30 秒
- [ ] 用户明确说了"简单"/"简单任务"

### 🔴 标记为「复杂」的条件（任意一条即复杂）

- [ ] 涉及多个步骤或有依赖关系的子任务
- [ ] 需要修改多个文件
- [ ] 需要调试/排错/分析日志
- [ ] 涉及深度研究、调研、方案设计
- [ ] 执行时间预估 > 1 分钟
- [ ] 用户明确说了"复杂"/"难"/"麻烦"/"耗时"
- [ ] 你自己心里觉得这个不简单

**评估结论必须是三选一：简单 / 复杂 / 视觉。写进你的思考过程。**

---

## Step 2 — 按评估结论路由

### 🟢 简单 → 我自己直接处理

模型：`deepseek-v4-flash`
方式：直接执行，不需要委派

---

### 🔴 复杂 → 必须委派子 Agent（禁止自己干）

**核心逻辑（死记）：**

```
判定  复杂  →
   ├── ❌ 我自己干 → deepseek-v4-flash（弱模型）→ 不准！
   └── ✅ delegate_task 委派 → deepseek-v4-pro（强模型）→ 必须！
```

- **我当前跑的是 `deepseek-v4-flash` — 快速/轻量模型，不适合处理复杂任务。**
- **子 Agent 通过 `delegation.provider=deepseek` + `delegation.model=deepseek-v4-pro` 配置，自动使用 pro 强模型。**
- **判定为复杂后，我绝对不自己上手。必须委派给子 Agent。**

**流程：分析 → 委派 → 聚合**

#### 2a. 分析

理解任务整体，判断能否拆分子任务以及它们之间的依赖关系。

- 子任务**相互独立** → 可以用 `delegate_task(tasks=[...])` 批量并发
- 子任务**有依赖关系**（如 B 依赖 A 的输出） → 串行委派，先 A 再 B
- 不能有效拆分 → 单个 `delegate_task(goal=..., context=...)`

**关键原则：委派强模型是必须的，并行是可选的。** 不要为了并行而强行拆分。

**并行成功的关键：在 context 中明确 API 接口契约。** 每个子 Agent 独立工作，必须靠你定义的接口约定来保证集成时能对上。

#### 2b. 委派

```python
# 可并行时 — batch 并发
delegate_task(tasks=[
    {"goal": "...", "context": "接口约定 + 文件路径 + 约束"},
    {"goal": "...", "context": "..."},
])

# 有依赖时或无法拆分时 — 单个委派
delegate_task(goal="...", context="...")
```

**约束：**
- 最多 3 并发
- 每个子 Agent 的 context 要自包含（没有历史会话）

#### 2c. 聚合（关键！）

收到所有子 Agent 结果后，必须做以下检查并修复：

**聚合检查清单：**

- [ ] **接口一致性** — 各子 Agent 对同一接口的命名和签名是否一致？
- [ ] **导入路径** — 模块间的 import 路径是否正确（如 src layout 需要 `where = ["src"]`）？
- [ ] **配置文件** — pyproject.toml / setup.cfg / package.json 等是否与目录结构匹配？
- [ ] **测试可运行** — 运行一次测试，确保全部通过
- [ ] **入口点** — CLI 入口、console_scripts 等是否已注册？
- [ ] **端到端验证** — 核心功能能否跑通？

如果发现集成问题，直接修复（我是主 Agent，有权修正子 Agent 产出的不一致）。

---

### 🟣 视觉任务 → vision_analyze

直接调 `vision_analyze`，自动走 Qwen/Qwen3-VL-8B-Instruct（auxiliary.vision 已配置好）。

---

## Config

```yaml
model:
  default: "deepseek-v4-flash"     # Tier 1 — 主 Agent（弱模型）
  provider: "deepseek"

delegation:
  provider: "deepseek"              # Tier 2 — 子 Agent（强模型）
  model: "deepseek-v4-pro"

auxiliary:
  vision:
    provider: "custom:api.siliconflow.cn"  # Tier 3 — 视觉
    model: "Qwen/Qwen3-VL-8B-Instruct"
```