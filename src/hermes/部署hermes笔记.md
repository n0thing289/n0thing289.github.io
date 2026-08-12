## 最基本的前置工作

开启梯子，没有就用自己的梯子，把梯子安装包连接复制，在客户浏览器中下载安装



## Windows原生安装

>推荐windows原生安装，使用中文论坛镜像安装脚本

hermes desktop（执行之后也是桌面版，然后右键窗口找到这个窗口的文件起始位置就是桌面版图标了）



## WSL2安装

### 快速命令

wsl.exe --set-default-version <1|2>

wsl --list --online

wsl --update

wsl --install --web-download --location D:\wsl

https://github.com/microsoft/terminal/releases/download/v1.24.11321.0/Microsoft.WindowsTerminal_1.24.11321.0_8wekyb3d8bbwe.msixbundle



wsl --list -v

win10可以装一个window terminal preview

wsl -d ubuntu

exit

wsl --shutdown



### 1-虚拟化前提

必须确定开启了虚拟化

AMD ： 

SVM Mode
NX/DX mode



英特尔：





### 2-window功能开启

hyper + 虚拟化平台 + WSL



### 3-安装WSL2



### 4-安装hermes



### 5-安装hermes-web-ui





### 安装window桌面版（非最终）

```text
HERMES_DASHBOARD_BASIC_AUTH_USERNAME=<你的用户名， admin>
HERMES_DASHBOARD_BASIC_AUTH_PASSWORD=<你的密码，如 abc123>
hermes dashboard --no-open --host 0.0.0.0 --port 9119
```

#### hermes dashboard 命令配置持久运行服务

```text
mkdir -p ~/.config/systemd/user
```

```text
cat > ~/.config/systemd/user/hermes-dashboard.service << 'EOF'
[Unit]
Description=Hermes Dashboard (user service)

[Service]
#Hermes 主目录
Environment=HERMES_HOME=%h/.hermes
#如果你用 ~/.hermes/.env 存环境变量/认证信息，在这里一起加载
EnvironmentFile=%h/.hermes/.env
#启动 dashboard，监听 0.0.0.0:9119
ExecStart=/usr/bin/env hermes dashboard --no-open --host 0.0.0.0 --port 9119
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
```

```text
systemctl daemon-reload (--user)
systemctl enable hermes-dashboard (--user)
systemctl start hermes-dashboard (--user)
```

### 桌面版的代替方案

使用hermes-web-ui，然后用edge安装为一个桌面程序，桌面版不稳定



## MAC安装



## 接入飞书

目前的飞书配置很简化了，只需要`hermes gateway setup`配置前运行pip install(用户扫码), 或者自己点击连接帮助客户创建



 source venv/bin/activate
