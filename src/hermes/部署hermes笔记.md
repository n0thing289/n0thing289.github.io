---
title: 部署hermes笔记
---

## 最基本的前置工作

1. 如果对方没有梯子，我们就要给他准备梯子的安装包下载连接`https://file.cat-cdn.com/v1/Clash.Verge_1.7.5_x64-setup.exe`

2. 开启梯子

## 安装方式选择

优先考虑windows mac原生安装，实在不行才是wsl2安装

## Hermes 安装流程

1. 前置工作做好

2. 根据平台，安装hermes

3. 安装hermes-web-ui，执行`npm i -g hermes-web-ui`

   可能会遇见两个错误：

   1. `缺失node环境`，如果使用的是国内镜像安装就会出现这个问题。手动去nodejs官网 [Node.js — 在任何地方运行 JavaScript ](https://nodejs.org/zh-cn) 下载安装即可
   2. `此系统上禁止运行脚本`，管理员身份在环境中，执行` Set-ExecutionPolicy RemoteSigned` 即可

4. 将网关自启动，执行`hermes gateway install`

5. (可选) 给用户安装命令版桌面版，执行`hermes desktop`

## WSL2 安装命令

>win10可以提前装一个`window terminal `

1. wsl --update
2. wsl --install --web-download --location D:\wsl



- wsl.exe --set-default-version <1|2>

- wsl --list --online



- 退出wsl：exit

- wsl --shutdown

## WSL2排查错误



### 1-虚拟化前提

必须确定开启了虚拟化

AMD ： 

SVM Mode
NX/DX mode



英特尔：待补充

### 2-window功能开启

hyper + 虚拟化平台 + WSL







## 装完后完善ui启动的教程

1. 编写一个cmd脚本

   ```cmd
   hermes-web-ui
   ```

2. 用edge的功能，设置=> 更多工具 => 应用 => 将此站点作为应用安装

