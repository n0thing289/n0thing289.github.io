---
Hermes陪跑和全模态
---

## 构建全模态

### 配置视觉分析辅助模型

主模型：Deepseek

视觉辅助模型：

- Kimi K3 更适配的领域（识图强项：UI 原型、草图转代码、复杂文档、空间透视、图表深度推理）**如果你是人使用（网页端，少量图，追求质量），做原型、科研、深度分析 → Kimi K3**。
- **如果你要做 API 接入，做产品、服务，要处理大量图片 / 视频，对延迟、成本敏感 → MiniMax M3**。



### 配置全网搜索工具

配置tavily

配置firecrawl

### 配置生图生视频能力

生图模型：gpt image 2、nano banana

生视频模型：seeddance



一种方式使用官方api

一种方式使用中转：

1. 配置api key
2. 把模型平台关于生图模型的文档，喂给hermes，让他根据这些文档，创建一个生图的skill，后续调用这个skill去生图
3. 另外我又给你配置了一个superaiapi-vedio的供应商，api key也有，使用这个供应商中的doubao seedance 2.0，完成视频生成任务。superaiapi.apifox.cn/api-479274320，这个是其中一个视频生成的文档，你用kimi webbridge去里面获取这个doubao seedance 2.0 模型的相关文档，并写成一个视频生成的skill



一种方式使用hermes官方推荐的fal.ai平台（统一管理生图生视频的模型）

### 搭建记忆系统

>尤其是多profile的情况需要额外配置

#### 主流记忆架构设计

有四层

Hermes记忆系统的设计

- 记忆分层
  - 工作记忆（此时此刻）
  - 情景记忆（按时间索引）
    - 当天事件摘要，心得，决策
    - compact时触发写入。按需grep检索
  - 核心记忆
    - （MEMORY.md：核心目标、当前任务、关键事实）
    - USER.md：稳定的用户习惯与偏好

#### 接入hindsight的提示词



1. 接下来你将查询（Holographic | Hindsight）（hermes官网文档）官方文档及主流记忆方案，我将向你提问，你也可以向我提问直到问题补充完整。接下来我想让你接入外部记忆，并且优化当前的记忆架构和方案，让你拥有长期记忆
2. 检查当前的记忆文件，是否符合官方文档中的记忆系统的架构和记忆分层，都存了什么东西
3. 接入hindsight后，需要处理什么吗，需不需要根据官方文档优化当前的记忆系统，以及接入前和接入后的变化是什么
4. hindsight都存哪些东西呢，什么时候触发存和读取呢
5. hindsight本地嵌入，安装在了哪里，有一天不需要怎么删除卸载呢
6. hindsight本地嵌入的，如何做备份数据迁移呢，有没有面板可以看到



#### 整理迁移Hindsight的提示词：

1. 接下来你将查询（Holographic | Hindsight）（hermes官网文档）官方文档及主流记忆方案
2. 对照官方文档核查记忆系统是否符合三层架构（内置 MEMORY.md/USER.md + session_search + 外部 provider）与分层设计，以及官方接入外部provider后的记忆架构设计推荐方案是怎么样的


多档案 hindsight 全家桶 → 方案2半隔离（每档案独立 bank，共享约定播种全部 bank）
精简 MEMORY.md/USER.md 分层，细节下沉 hindsight
沉淀为 skill



审视 MEMORY.md / USER.md 分层是否符合官方设计, 将其中多余的移入hindsight，需要时调用即可 MEMORY.md = Agent 笔记：环境事实、项目约定、经验教训（"core goals, environment facts, conventions, lessons learned"）
USER.md = 用户画像：身份、稳定的偏好、沟通风格（"identity, preferences, communication style"）





## 创建生图skill：

要创建skill，你可以不断向我提问知道完整直接让hermes 拷问我

### 生图skill的提示词：

1. 在default这个profile中，
2. 我给你配置了一个Provider叫superaiapi，这是superaiapi的api文档（你需要在这里找到关于GPT Image 2的接口调用说明并写入skill中）superaiapi.apifox.cn，密钥在default的profile的config中。
3. 另外，相等地，我也给你配置了一个Provider叫tokenflux，这是tokenflux的api文档（你需要在这里找到关于Nano Banana的接口调用说明并写入skill中，如果没有就参考Nano Banana官方模型调用生图接口的文档和接口端点），docs.tokenflux.dev/docs/quickstart.html，密钥在default的profile的config中。
4. 其次，每次生图前需要告诉我，本次生图用的模型是什么。
5. 最后写完skill后去验证一下生图一下是否可以生图，并且后续每次用本skill生图产生的错误和经验，并再次总结写入到本skill中，最后剔除无效多余的错误和经验
6. 生图分辨率设置成2k
7. 如果我指定你默认生图模型，那就用默认模型
8. 生图前未指定模型就默认用GPT Image 2
9. 生完图后自检

如法炮制这个提供商还可以生视频，帮我接入grok的生视频模型，并写成skill

### 创建反推图片提示词的  skill提示词：

1. 现在我需要你创建skill，我将会不断的给你我们公司的图片，你需要根据这些图片反推提示词给我，然后现在需要你反推的图片风格样式你可以向我提问那些需要反推哪些不需要直到需要反推的提示词补充完整；

   1. 从图片中提取可观察的构图、色彩、光线、材质、字体与视觉风格

      区分事实、推断和不确定信息

      只针对无法从图片确认的关键内容向你提问

      持续补齐提示词变量，直到关键条件完整

      输出视觉指纹、风格规则、主提示词、反向提示词和可替换变量

2. 每次给你图片的时候，你都可以分析把需要新增的方面记录回本skill，剔除冗余的方面

   1. 新增一个可维护的视觉知识库，记录从实际图片中反复验证出的公司风格规则。每次分析后先去重、合并、标注证据与置信度，再决定是否写入，避免技能越用越臃肿。

   2. 每次分析图片前读取公司视觉风格记忆

      每次分析完成后，自动判断是否需要新增风格维度

      新规则必须满足：有图片证据、影响后续提示词、具备长期参考价值

      自动合并重复规则

      弱化或移除只出现一次的偶然特征

      对冲突风格保留为“适用范围/变体”

      输出中新增 `Memory update`，说明本轮记忆发生了什么变化

3. 风格需要分类好

4. 当用户需要生图提示词的时候，有两种情况

   1. 用户把图片给你，你会根据视觉知识库+对当前图片的分析，给用户分析检索生成出来类似的提示词
   2. 只有提示词，询问用户是否走视觉知识库，生成一张近似的

5. 当用户发给你图片让你分析时，就触发本skill

6. 来图反推提示词 + 来图分析反推入库



按照主播的风格，来出图（霸道总裁就出霸道总裁类似的图）



场景环节：我是美工，运营找我，“给新主播做壁纸”，

“什么样的人设”

“霸道总裁，刷一点，拽一点，性张力强一点，不要ai一点，色调贴合”

“那主播叫什么名字，标签怎么写：比如叔音/疗愈/在这里陪你聊天”



那美工第一步是什么：人物主体先做出来符合人设贴合的。美工一般会去搜立绘图找素材

第二步：搞背景排版



## Skill推荐

>[Hermes Skill 卡片浏览](https://codesstar.github.io/hermes-skill-atlas/article/hermes-skill-cards.html)
>
>

ppt master：



### 审美skill

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

### AI团队

```
```

