# test1
------------------------------------------------------------
客户端程序

register.py: 用户注册。读配置，将用户信息发送至服务器，添加新用户。

re-register.py: 用户重注册。修改已有的用户信息。

client.py: 处理csv文件，将生成的json数据发至服务器。

------------------------------------------------------------
服务器API

client: 新增client。

client/{curl}: 修改client信息。

poster: 将信息正确的client发送的json数据进行格式验证，为正确数据生成uuid并保存。

---------------------------------------------------------------
使用

1、安装python3.7或以上版本。

2、安装环境。运行pip install -r requirements.txt

3、启动服务端。进入t1目录后，运行python3 manage.py runserver

4、应用客户端程序。进入client目录后，运行相应py脚本。如python3 client.py