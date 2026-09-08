---
title: Ollama本地部署模型
---



## 大致流程

1. 安装ollama
2. 根据配置和用户需求，挑选模型
3. 让豆包编写上下文长度为64k，128k，256k的Ollama Modelfile文件
4. 执行`ollama create 模型 -f Modelfile`
5. 根据`http://127.0.0.1:11434/v1`, 接入hermes



## 速度优化

p2p + MTP3