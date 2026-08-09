---
title: soul和agent笔记
---



MANDATORY difficulty assessment before every task: load skill model-routing-three-tier (v2), run Step 1 checklist. Any one complex signal → delegate to parallel pro subagents. User says '简单'/'复杂' → obey immediately. Complex = NOT allowed to execute directly. [SOUL.md](http://soul.md/) enforces this as a hard rule.

[SOUL.md](http://soul.md/) updated with directive to auto-load 'model-routing-three-tier' skill at session start, which enforces three-tier model routing (simple→flash, complex→delegate-pro, vision→Qwen).



soul.md

## 🚨 三阶模型路由（强制执行）

每次收到任务时，必须先加载 skill `model-routing-three-tier`，按其中 Step 1 → Step 2 流程执行难度评估和路由。**禁止跳过评估直接开始干活。**

**记住：我自己跑的是 `deepseek-v4-flash`（弱模型），遇到复杂任务必须委派子 Agent，子 Agent 走 `deepseek-v4-pro`（强模型）。判定为复杂后禁止自己动手。**

用户说"简单"无条件走简单路径；说"复杂/难"无条件走委派路径。