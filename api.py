import requests
import urllib
import random
import json
import re
import schedule
import time
from rcon.source import Client
steps=28
cfg=11
f = open("config.py","r")
f = eval(f.read())
Map_Pool = tuple(f["maps"])
Humans_QQ = int(f["admins"])
server_IP = f["IP"]
server_port = int(f["port"])
rcon_password = f["password"]

def css_rcon(cmmd,gid,msgid):
    global response
    try:
        with Client(server_IP,server_port,passwd=rcon_password) as client:
            response = client.run("%s" % cmmd)
    except UnicodeDecodeError as response:
        response=str(response)
        response=response.decode(encoding, errors='replace').replace("?","NaN")
    except ConnectionRefusedError as response:
        requests.get(url:='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=[CQ:reply,id=%s]>>>请求控制台失败\n「服务器状态：关闭」' % (gid,msgid))
        return
def keyword(msgid,message,uid,gid,times):
    if message=="/menu":
        cai="꧁时崎狂三ᵇᵒᵗ || 功能列表꧂\n\n==========\n注意：命令中的空格不能省略！！！！！！！！！！！！！\n==========\n①/css_ping：\n查看服务器的运行状态\n==========\n②/css_players：\n查看服务器内在线玩家的信息\n==========\n③/css_maps：\n查看服务器的地图池\n==========\n④/css.cmd 命令：\n直接对控制台发出一条命令，可用于临时换图等操作，若是回显文字过多可能会回复空消息（此项仅主人可用）"
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=[CQ:reply,id=%s]%s' % (gid,msgid,cai))
    if "/css_" in message:
        css_rcon("status",gid,msgid)
        ress=response.split("\n")
        global hostname
        hostname=ress[0]
        hostname=hostname.replace("hostname: ",">>>")
        if message=="/css_ping":
            hostname=ress[0]
            maps=ress[3]
            players=ress[5]
            hostname=hostname.replace("hostname: ",">>>")
            maps=maps.replace("map     ","|地图").replace(" at: 0 x, 0 y, 0 z","")
            players=players.replace("players ","|在线人数").replace("humans","玩家").replace("bots","人机").replace(" (16 max)","").replace(","," ||")
            status="%s\n『服务器状态：在线』\n==========\n%s\n%s" % (hostname,maps,players)
            print(status)
            res=urllib.parse.quote(str(ress))
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=[CQ:reply,id=%s]%s' % (gid,msgid,status))
        if message=="/css_players":
            print(ress)
            print("")
            print("")
            pbn=ress[7:]
            print(pbn)
            print("")
            print("")
            global human
            human="%s\n『服务器状态：在线』\n==========\n注：空格隔开的每一个信息与开头的内容都是相对应的，请按从左到右的顺序自行对照！\n==========\n" % hostname
            for human_2 in pbn:
                human=human+human_2+"\n\n"
            human=human.replace("userid","玩家ID").replace("name","昵称").replace("                uniqueid            "," ").replace("STEAM_ID_LAN","").replace("          ","").replace("connected","在线时长").replace("ping","延迟").replace("loss","丢包率").replace("state","状态").replace("adr","玩家IP")
            human=urllib.parse.quote(human)
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=[CQ:reply,id=%s]%s' % (gid,msgid,human))
        if message=="/css_maps":
            shjiop="%s\n『服务器状态：在线』\n==========\nRose服务器地图池：\n" % hostname
            shuzu=1
            shuers=Map_Pool
            for shjs in shuers:
                smpaop="%s.<%s>\n" % (str(shuzu),shjs)
                shjiop=shjiop+smpaop
                shuzu+=1
            print(shjiop)
            smaps=urllib.parse.quote(shjiop)
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=[CQ:reply,id=%s]%s' % (gid,msgid,shjiop))
    if "/css.cmd " in message and uid==Humans_QQ:
        zheng=re.match("^/css.cmd ",message)
        if zheng!=None:
            mess=message.replace("/css.cmd ","")
            css_rcon(mess,gid,msgid)
            print(response)
            ress=urllib.parse.quote(str(response))
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id=%s&message=[CQ:reply,id=%s]%s' % (gid,msgid,ress))
        else:
            print("")