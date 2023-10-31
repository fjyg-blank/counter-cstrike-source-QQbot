中文
一、准备工作
    1.python版本3及以上
    2.go-cqhttp最新版本
    
二、注意事项
    1.rcon密码设置方法
    在服务端主目录/cstrike/cfg/server.cfg中新增一行：
    rcon_password "密码"
    
    2.go-cqhttp框架配置请看各大社区的教程，B站，csdn一堆教程一找就有，请选择HTTP通信并把HTTP监听端口设置为5701，反向HTTP端口设置为5700。
    
    3.代码中需要的python运行库，命令如下：
    cd ~/QQBOT
    pip install -r package.txt
    
    4.以上全部做完后打开config.py进行相关配置。
    
    5.启动项目命令如下：
    python3 main.py或者python main.py因为安装方式不同命令可能有所出入都试一下就行，如果需要放在后台运行请自行寻找screen工具的使用方法。
    
    6.QQ群发送/menu查看功能菜单，一定是群消息，私聊暂未开发。

English
Preparation work
    1.Python version 3 and above
    2.go-cqhttp latest version

Precautions
    1.rcon password setting method
    Add a new line in the server home directory/cstrike/cfg/server.cfg:
    rcon_password "password"
    
    2. For go-cqhttp framework configuration, please refer to the tutorials of major communities. There are a lot of tutorials on Bilibili and csdn. Please select HTTP communication and set the HTTP listening port to 5701 and the reverse HTTP port to 5700.
    
    3. The python runtime library required in the code, the command is as follows:
    cd ~/QQBOT
    pip install -r package.txt
    
    4. After completing all the above, open config.py to perform relevant configurations.
    
    5. The command to start the project is as follows:
    python3 main.py or python main.py may have different commands due to different installation methods. Just give it a try. If you need to run it in the background, please find out how to use the screen tool by yourself.
    
    6. QQ group sending/menu viewing function menu must be group messages, private chat has not been developed yet.