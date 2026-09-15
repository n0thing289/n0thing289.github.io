---
title: Hermes陪跑和全模态
---

## 大纲

- 视觉分析模型
- 生图
- 生视频
- tavily（实现全网抓取）
- 接入hindsight（搭建记忆系统）
- 安装kimi webbridge
- 安装Obsidian cli

## 写在前面

我比较喜欢在终端中配置好所有的api key，最后的调整用桌面版告诉hermes执行

## 构建全模态

### 配置视觉分析辅助模型

>截止2026年9月15日，deepseek-flash已经变为多模态模型了，无其他特殊需求，默认用它就可以完成视觉分析

主模型：Deepseek

视觉辅助模型：

- Kimi K3 更适配的领域（识图强项：UI 原型、草图转代码、复杂文档、空间透视、图表深度推理）**如果你是人使用（网页端，少量图，追求质量），做原型、科研、深度分析 → Kimi K3**。

- **如果你要做 API 接入，做产品、服务，要处理大量图片 / 视频，对延迟、成本敏感 → MiniMax M3**。

  



### 配置全网搜索工具（tavily）

1. 使用`hermes setup tools`
2. 进入到==web extraction==界面
3. 选择tavily，打开给的网址，让客户注册
4. 复制key
5. 在桌面版对话中喂给她tavily官网的提示词模板，最后验证一下

### 配置生图生视频能力

>我个人安装使用的中转站：
>
>superaiapi：[平价稳定的 AI 模型聚合平台 | SuperAI API](https://superaiapi.com/zh-cn)
>
>tokenflux：[仪表盘 - tokenflux](https://tokenflux.dev/dashboard)
>
>如何使用？
>
>superaiapi 用来接入他的gpt-image-2
>
>tokenflux 用来接入他的gpt-5.6-sol
>

#### 模型选择

生图模型：gpt image 2、nano banana

生视频模型：seedance、minimax h3

#### 推荐操作顺序

1. 需要提前配置好提供商 ==hermes setup model== 建议提供商name写全小写
2. 在桌面版开单独会话去喂提示词

#### 提示词模板

接入gpt-image-2为例

```
这是superaiapi的api官方文档地址https://superaiapi.apifox.cn/llms.txt，请你在里面学习关于gpt image 2的接口说明，然后试着调用一下验证一下，最后总结学习成一个叫自定义生图（custom-gen-image）的skill
```

接入minimax h3为例：

```
这是minimax的api官方文档地址https://superaiapi.apifox.cn/llms.txt，请你在里面学习关于gpt image 2的接口说明，然后试着调用一下验证一下，最后总结学习成一个叫自定义生图（custom-gen-image）的skill
```



一种方式使用hermes官方推荐的fal.ai平台（统一管理生图生视频的模型）

### 搭建记忆系统

>尤其是多profile的情况需要额外配置

#### Hermes记忆系统的设计

- 记忆分层
  - 工作记忆（此时此刻）
  - 情景记忆（按时间索引）
    - 当天事件摘要，心得，决策
    - compact时触发写入。按需grep检索
  - 核心记忆
    - （MEMORY.md：核心目标、当前任务、关键事实）
    - USER.md：稳定的用户习惯与偏好

#### 学习Hindsight的提问提示词

1. 接下来你将查询（Holographic | Hindsight）（hermes官网文档）官方文档及主流记忆方案，我将向你提问，你也可以向我提问直到问题补充完整。接下来我想让你接入外部记忆，并且优化当前的记忆架构和方案，让你拥有长期记忆
2. 检查当前的记忆文件，是否符合官方文档中的记忆系统的架构和记忆分层，都存了什么东西
3. 接入hindsight后，需要处理什么吗，需不需要根据官方文档优化当前的记忆系统，以及接入前和接入后的变化是什么
4. hindsight都存哪些东西呢，什么时候触发存和读取呢
5. hindsight本地嵌入，安装在了哪里，有一天不需要怎么删除卸载呢
6. hindsight本地嵌入的，如何做备份数据迁移呢，有没有面板可以看到



#### 从旧记忆迁移到Hindsight的提示词

1. 接下来你将查询（Holographic | Hindsight）（hermes官网文档）官方文档及主流记忆方案
2. 对照官方文档核查记忆系统是否符合三层架构（内置 MEMORY.md/USER.md + session_search + 外部 provider）与分层设计，以及官方接入外部provider后的记忆架构设计推荐方案是怎么样的



#### 提示词模板

```
审视 MEMORY.md / USER.md 分层是否符合官方设计, 将其中多余的移入hindsight，需要时调用即可.
MEMORY.md = Agent 笔记：环境事实、项目约定、经验教训（"core goals, environment facts, conventions, lessons learned"）
USER.md = 用户画像：身份、稳定的偏好、沟通风格（"identity, preferences, communication style"）
对照官方文档核查记忆系统是否符合三层架构（内置 MEMORY.md/USER.md + session_search + 外部 provider）与分层设计，以及官方接入外部provider后的记忆架构设计
```







## Skill推荐

>[Hermes Skill 卡片浏览](https://codesstar.github.io/hermes-skill-atlas/article/hermes-skill-cards.html)
>
>这里的skill，安装前可以问客户的工作内容大致都是什么，需要ppt，就装ppt相关的
>
>默认满血版安装这两个：
>
>- [mattpocock/skills: Skills for Real Engineers. Straight from my .agents directory.](https://github.com/mattpocock/skills)
>- [jnMetaCode/agency-agents-zh: 🎭 277 个即插即用的 AI 专家角色 — 支持 Claude Code/Cursor/Copilot 等 20 种工具，覆盖工程/设计/营销/金融等 20 个部门。含 64 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉/Qt 上位机/机械设计）。搭配编排器 agency-orchestrator，一句话即可让多位专家按 DAG 自动协作。](https://github.com/jnMetaCode/agency-agents-zh)
>- 安装上面两个的时候，也可以问客户的工作内容，进行选装



### PPT

```
安装这个skill：https://github.com/hugohe3/ppt-master
```



### 审美相关skill

- taste skill：

- impeccable

https://mp.weixin.qq.com/s/a232jGEfi7VwEeOZYvPF9A

| Skill                            | 风格              | 打分   | 关键特点                                                     |
| -------------------------------- | ----------------- | ------ | ------------------------------------------------------------ |
| **gc-minimal-zine-poster-v0-3**  | 纸刊海报 / 做旧风 | ⭐⭐⭐⭐⭐  | 最出名。自带 prompt-compiler + quality-gate 质检流程；大面积留白 + 单一视觉焦点，仿旧纸张竖版画布，默认 3:5；可传图或只发一句话（翻译成视觉隐喻）；情绪依赖最强，提示词越具体效果越好 |
| **pixel-style-poster-skill**     | 像素 / 点阵印刷风 | ⭐⭐⭐⭐   | 细密小点表现明暗，像老式激光打印机印在米白纤维纸上；适合花卉、动物、近景人脸；默认 3:4 竖版；很挑原图质量，看多易视觉疲劳 |
| **muted-zine-poster-v01**        | 极简低饱和        | ⭐⭐⭐    | gc-minimal 的「安静版」二创；颜色近单色，70%+ 留白；适合雨天、旧书、海边、回忆；缺点是元素少、情感单一 |
| **deconstructed-duotone-poster** | 解构 / 平面印刷   | ⭐⭐⭐⭐⭐⭐ | 核心是「解构」：拆原图为语义锚点，用六 / 九宫格重新演绎，分析细节而非套滤镜；对比例敏感，最好先裁 3:4 或 4:3 |
| **photo-revival**                | 手绘重绘          | ⭐⭐⭐    | 保留主体 / 空间 / 情绪再手绘重绘，「把照片画成一页诗」；专治手机相册里舍不得删的废片；建议 3:4/3:5 竖图，像儿童读物配图 |
| **photo-relic-editorial**        | 纸上留影          | ⭐⭐⭐⭐   | 上半保留照片、下半生成版画并提取照片色彩结构、淡墨勾勒；适合建筑 / 天际线 / 水面 / 道路；图下有配文 |
| **photo-abstract-editorial**     | 克制极简抽象      | ⭐⭐⭐⭐⭐  | 8 月初开源几天冲榜 GitHub 第一；下半部分是象牙白抽象面板，只抽离大空间关系成极简几何标记 + 英文标题；简约高级，可直接当商标 |
| **travel-photo-abstraction**     | 旅行抽象          | ⭐⭐⭐⭐   | 把照片的数量 / 位置 / 节奏 / 间隙映射成抽象符号；适合元素丰富、层次清楚的城市 / 街道 / 风景照，可做旅拍作品集 / 手账配图 |
| **scenes-gathered-zine-v1-3**    | 撕纸纸刊风        | ⭐⭐⭐⭐⭐⭐ | 作者最爱。保留照片真实质感，用手撕纸纤维边连接照片与纸刊插画，下方加从照片提取的高饱和抽象色块；把复杂细节压成几块大形状，最值得精挑原图 |

### 公文skill：

```
请帮我安装这个 Agent Skill。

Skill 页面：https://skillsmp.com/zh/creators/leoyeai/openclaw-master-skills/skills-official-doc-writer
源地址：https://github.com/LeoYeAI/openclaw-master-skills/tree/main/skills/official-doc-writer
Skill 名称：official-doc-writer
作者：LeoYeAI
推荐安装命令：npx skills add https://github.com/LeoYeAI/openclaw-master-skills --skill official-doc-writer

请打开 Skill 页面和源地址，先阅读 SKILL.md 以及所有配套文件，并在安装前说明任何风险。

如果当前环境可以执行 shell 命令，优先使用上面的安装命令。如果需要手动安装，请复制包含 SKILL.md 的完整 skill 目录，包括 scripts、references、assets、agents 以及 Skill 页面展示的其他文件，并保留相对目录结构。不要只安装 SKILL.md。安装完成后，请确认目标 skills 目录里包含 SKILL.md 和这个 skill 需要的全部配套文件。
```

### 生产力skill

这里的skill，安装前可以问客户的工作内容大致都是什么

```
请你结合我的工作需求，如果你不知道我的工作需求，你可以让我补充，然后安装这个skill：https://github.com/mattpocock/skills
```

```
请你结合我的工作需求，如果你不知道我的工作需求，你可以让我补充，然后安装这个skill：https://github.com/jnMetaCode/agency-agents-zh
```

