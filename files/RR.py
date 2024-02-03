# coding=utf-8
#Link Start!
#使用前请先阅读官方文档！https://shequ.codemao.cn/wiki/novel/cover/78176

import traceback
import requests as r
import time
import json
import re
import threading as th
import tkinter as tk
from tkinter import messagebox
import random
#from robotreply.py import go
import os
from urllib.request import quote

#real_url = "https://api.codemao.cn/web/message-record?query_type=COMMENT_REPLY&limit=30&offset=0"


def find_txt(path):
	"""初始化配置与指令，找到本地存的指令……"""
	txts = os.listdir(path + r'/data/information/')
	untxts = []
	for i in txts:
		try:
			if i[-4:] != ".txt":
				untxts.append(i)
		except:
			untxts.append(i)

	for i in untxts:
		txts.remove(i)

	#if ('in.txt' not in txts)or('else.txt' not in txts)or('maybe.txt' not in txts)or('name.txt' not in txts)or('common.txt' not in txts):
		#print("数据缺失")

	#in_txt = open(path + r'/data/information/in.txt').read()
	#else_txt = open(path + r'/data/information/else.txt').read()
	#maybe_txt = open(path + r'/data/information/maybe.txt').read()
	#name_txt = open(path + r'/data/information/name.txt').read()

	#print(else_txt)

	other_txt = {}
	for i in txts:
		#print(i[:-4])
		try:
			other_txt[i[:-4]] = open(path + r'/data/information/' + i, encoding='utf-8-sig').readlines()
		except UnicodeDecodeError:
			try:
				other_txt[i[:-4]] = open(path + r'/data/information/' + i, encoding='gbk').readlines()
			except UnicodeDecodeError:
				other_txt[i[:-4]] = open(path + r'/data/information/' + i, encoding='gb18030').readlines()

		if len(other_txt[i[:-4]]) == 1:
			if i[:-4] == 'name':
				other_txt[i[:-4]] = "【" + str(other_txt[i[:-4]][0]) + "】"
			else:
				other_txt[i[:-4]] = str(other_txt[i[:-4]][0])

	#the_return = {'in_txt':in_txt,'else_txt':else_txt,'maybe_txt':maybe_txt,'name_txt':name_txt,'other_txt':other_txt}
	return(other_txt)


def nlp(main):
	"""NLP：自然语言处理，对回复的内容进行解析，并返回自动回复的内容"""

	sender_name = main["sender"]["nickname"]
	sender_title = main["message"]["business_name"]
	try:
		msg = str(main["message"]["reply"])
		reply_id = main["message"]['reply_id']
		sender_content = main["message"]["reply"]
	except KeyError:
		msg = str(main["message"]["comment"])
		reply_id = main["message"]['comment_id']
		sender_content = "<帖子下直接回复>"

	reply_msg = str(datas['common'])

	msg = msg.split("#")[0].strip()
	if msg == "":
		msg=" "

	
	if msg[0] == "/":
		#指令
		zl = True
		#print(msg[:7])
		#print(msg[:7] == "/自定义回复=")
		#print(msg[:4] == "/召唤=")
		real_msg = msg[1:]
		if "=" in real_msg:
			real_msg = real_msg.split("=")[0]
		if real_msg in datas:
			if msg == "/最新活动":
				reply_msg=datas['name'] + datas['最新活动']
			elif msg == "/不再回复":
				zl = False
				reply_msg=datas['name'] + datas['不再回复'][0]
				file_name = os.path.abspath('.') + r'/data/unreply.txt'
				with open(file_name,"a+") as f:
					f.seek(0)
					every_each = f.read().split(",")
					if every_each == ['']:
						f.write(str(main["sender"]["id"]))
					else:
						#print(every_each)
						if not str(main["sender"]["id"]) in every_each:
							f.write("," + str(main["sender"]["id"]))
			elif msg == "/恢复回复":
				reply_msg=datas['name'] + datas['恢复回复'][0]
				file_name = os.path.abspath('.') + r'/data/unreply.txt'
				with open(file_name, "r+") as f:
					f_content = f.read()
					new_f = f_content
					if str(main["sender"]["id"]) not in f_content:
						reply_msg=datas['name'] + datas['恢复回复'][1]
					else:
						while str(main["sender"]["id"]) in new_f:
							new_f = f_content.replace(str(main["sender"]["id"]) + ",",'')
							#print(new_f)
						f.seek(0)
						f.truncate()
						f.write(new_f)
			elif msg == "/讲笑话":
				file_name = os.path.abspath('.') + r'/data/jokes.txt'
				with open(file_name) as f:
					every = f.read().split("\n")
					#print(every)
					reply_msg=datas['name'] + str(random.choice(every))
			elif msg == "/毒鸡汤":
				file_name = os.path.abspath('.') + r'/data/sentence.txt'
				with open(file_name) as f:
					every = f.read().split("\n")
					#print(every)
					reply_msg=datas['name'] + str(random.choice(every))
			elif msg == "/名言警句":
				file_name = os.path.abspath('.') + r'/data/myjj.txt'
				with open(file_name) as f:
					every = f.read().split("\n")
					#print(every)
					reply_msg=datas['name'] + str(random.choice(every))
			elif msg == "/自定义回复":
				reply_msg = datas['name'] + datas['自定义回复'][0]
			
			
			elif msg[:7] == "/自定义回复=":
				zdy_msg = datas['name'][:-1] + "の自定义回复】" + msg[7:]
				if len(zdy_msg) > 90:
					reply_msg=datas['name'] + datas['自定义回复'][1]
				else:
					ok = True

					file_name = os.path.abspath('.') + r'/data/stopword.txt'
					try:
						with open(file_name,"a+") as f:
							f.seek(0)
							stop_words = f.read().split(",")
							#print(stopwords)
							for letter in stop_words:
								if letter in zdy_msg.lower():
									reply_msg = datas['name'] + datas['自定义回复'][2] + letter
									ok = False
							
					except FileNotFoundError:
						with open(file_name, "w"):
							pass

					
					if ok:
						file_name = os.path.abspath('.') + r'/data/replies.txt'
						with open(file_name, "r+", encoding="utf-8-sig") as f:
							f_content = json.load(f)
							#new_f = f_content
							if str(main["sender"]["id"]) in f_content:
								reply_msg=datas['name'] + datas['自定义回复'][3]
							else:
								reply_msg=datas['name'] + datas['自定义回复'][4]
							f_content[str(main["sender"]["id"])] = zdy_msg
							f.seek(0)
							f.truncate()
							json.dump(f_content, f)


			elif msg == "/召唤":
				reply_msg = datas['name'] + datas['召唤'][0]
			
			
			elif msg[:4] == "/召唤=":
				id_msg = msg[4:]
				try:
					id_msg = int(id_msg)
					id_msg = str(id_msg)
				except:
					reply_msg = datas['name'] + datas['召唤'][1]
				print(id_msg)
				if len(id_msg) > 6:
					reply_msg=datas['name'] + datas['召唤'][2]
				else:
					ok = True

					file_name = os.path.abspath('.') + r'/data/hasgone.txt'
					try:
						with open(file_name,"a+") as f:
							f.seek(0)
							every_hasgone_id = f.read().split(",")
							#print(stopwords)
							if id_msg in every_hasgone_id:
								reply_msg =datas['name'] + datas['召唤'][3]
								ok = False
							else:
								f.seek(2)
								f.write("," + id_msg)
							
					except FileNotFoundError:
						with open(file_name, "w"):
							f.seek(2)
							f.write(id_msg)

					
					if ok:
						threading_go_to = go_to(uid=id_msg,reply_name=str(main["sender"]["nickname"]))
						#threading_search.setDaemon(True)
						threading_go_to.start()
						reply_msg = datas['name'] + datas['召唤'][4]



			elif msg == "/切换点赞模式":
				file_name = os.path.abspath('.') + r'/data/unlike.txt'
				with open(file_name, "a+") as f:
					f.seek(0)
					f_content = list(set(f.read().split(",")))
					new_f = f_content
					if str(main["sender"]["id"]) not in f_content:
						reply_msg=datas['name'] + datas['切换点赞模式'][0]
						f.seek(2)
						if f_content != ['']:	
							f.write("," + str(main["sender"]["id"]))
						else:
							f.write(str(main["sender"]["id"]))
					else:
						reply_msg=datas['name'] + datas['切换点赞模式'][1]
						f_content = f_content.remove(str(main["sender"]["id"]))
						f.seek(0)
						f.truncate()
						if f_content != None:
							f.write(f_content)
			
			elif msg == "/特别鸣谢":
				reply_msg=datas['name'] + datas['特别鸣谢']

			elif msg == "/作品点赞":
				reply_msg=datas['name'] + datas['作品点赞']
				threaidng_like_work = like_works(reply_id=main["sender"]["id"])
				threaidng_like_work.start()
			
			else:
				reply_msg=datas['name'] + "该机器人制作者添加了回复内容配置，却没有改动对应的代码"

		else:
			reply_msg = datas['else']

		
	else:
		#平常说的话
		zl = False

		if_else = False
		for j in datas:
			if j in msg:
				reply_msg = datas['maybe']
				if_else = True

		if not if_else:
			if str(datas['name']) in msg:
				reply_msg = str(datas['in'])
			else:
				file_name = os.path.abspath('.') + r'/data/replies.txt'
				with open(file_name, encoding="utf-8-sig") as f:
					every = json.load(f)
					if str(main["sender"]["id"]).strip() in every:
						reply_msg = every[str(main["sender"]["id"]).strip()]
						#print("特殊回复：" + reply_msg)

	all_data = {"zl":zl ,"reply_msg": reply_msg, "reply_id":reply_id,"sender_name":sender_name,"sender_title":sender_title,"sender_content":sender_content}
	#print("return")
	return(all_data)

def before_find(k):
	"""对帖子进行定位，以及对回复的消息进行预处理"""
	#print(j["type"])
	#print((j["type"] != "WORK_COMMENT") & (j["type"] != "WORK_REPLY_REPLY"))
	if ((k["type"] == "POST_REPLY_REPLY") or (k["type"] == "POST_REPLY") or (k["type"] == "POST_REPLY_AUTHOR")or (k["type"] == "POST_REPLY_REPLY_FEEDBACK")):
		#print("帖子下的回复")
		if k['type'] == "POST_REPLY_REPLY":
			reply_reply = True
		else:
			reply_reply = False
		#BOSSBUG此处一切正常
		main = eval(k["content"])
		choose_unreply=False
		file_name = os.path.abspath('.') + r'/data/unreply.txt'
		new_url = "https://api.codemao.cn/web/forums/posts/" + str(main["message"]["business_id"]) + "/replies?page=1&limit=30&sort=-created_at"
		
		
		all_data = nlp(main)
		#BOSSBUG此处一切正常

		#return(0)

		with open(file_name, encoding="utf-8-sig") as f:
			f.seek(0)
			every_each = f.read().split(",")
			for each in every_each:
				#print(str(each).strip())
				#print(str(main["sender"]["id"]).strip())
				#print(str(each).strip() == str(main["sender"]["id"]).strip())
				if str(each).strip() == str(main["sender"]["id"]).strip():
					#如果回复的人在取消回复的名单之内
					choose_unreply = True
					if all_data['zl'] : 
						all_data['reply_msg'] = datas['不再回复'][1]

		#print(all_data)


		if choose_unreply:
			if not all_data['zl']:
				new_text_content = "————————————————————\n回帖API状态码：<目标已取消自动回复>\n回帖API返回值：<目标已取消自动回复>\n原贴名称：" + all_data["sender_title"] + "\n回复人：" + all_data["sender_name"] + "\n回复内容："+ all_data["sender_content"] + "\n" + "————————————————————"
				write_right = new_text(new_text_content)
				if write_right == "err":
					new_text_content = "————————————————————\n回帖API状态码：<目标已取消自动回复>\n回帖API返回值：<目标已取消自动回复>\n原贴名称：" + all_data["sender_title"] + "\n回复人：" + all_data["sender_name"] + "\n回复内容：<因编码问题无法写入>\n" + "————————————————————"
					new_text(new_text_content,again=True)
				return(0)

		#此处BOSSBUG一切正常

		new_url = "https://api.codemao.cn/web/forums/posts/" + str(main["message"]["business_id"]) + "/replies"
		new = to(new_url,0)
		new_content = re_sub(new.text)
		the_list = list(reversed(new_content['items']))
		for j in the_list:
			result = to_find(j=j,k=k,all_data=all_data,reply_reply=reply_reply,choose_unreply=choose_unreply,main=main)
			#print("result:" + str(result))
			try:
				if result['statu'] == "not404":
					#print("result['statu'] == 404")
					return(0)
			except :
				if result != "not me":
					return(0)

		#print("<对方已撤回消息>")
		print(result)
		try:
			new_text_content = "\n————————————————————\n回帖API状态码：404\n回帖API返回值：<对方已撤回消息>\n原贴名称：" +result['sender_title'] + "\n回复人：" + result['sender_name'] + "\n回复内容："+ result['sender_content'] + "\n————————————————————"
		except:
			new_text_content = "\n————————————————————\n回帖API状态码：404\n回帖API返回值：<对方已撤回消息>\n原贴名称：<无法查看>\n回复人：<无法查看>\n回复内容：<无法查看>\n————————————————————"
		write_right = new_text(new_text_content)
		if write_right == "err":
			new_text_content = "————————————————————\n回帖API状态码：404\n回帖API返回值：<对方已撤回消息>\n原贴名称：" + result['sender_title'] + "\n回复人：" + result['sender_name'] + "\n回复内容：<因编码问题无法写入>\n————————————————————"
			new_text(new_text_content,again= True)
	else:
		#print("作品回复或帖子下直接回复")
		new_text_content = "————————————————————\n回帖API状态码：<目标在帖子下直接回复，或在作品下回复>\n回帖API返回值：<目标在帖子下直接回复，或在作品下回复>\n————————————————————"
		new_text(new_text_content)
		return(0)

def to_find(j,k,all_data,reply_reply,choose_unreply,main):
	"""用于处理请求完成后的善后工作"""
	#print(j)
	if j['user']["id"] == str(datas['id']):
		#如果是晓寒的回帖（但不包括一个帖子下好几条回复的情况，这种情况需要在find里进行处理（404递归，直到找到正确的回帖为止，否则就是对方已撤回
		#print("第一次调用，reply_id：" + str(reply_id))
		statu = find(page=1, j=j,k=k, reply_id=all_data["reply_id"], reply_msg=all_data["reply_msg"], sender_content=all_data["sender_content"],sender_name=all_data["sender_name"], sender_title=all_data["sender_title"], reply_reply=reply_reply,choose_unreply=choose_unreply,main=main)
		#print("调用find()完成：" + str(statu))
		if statu['statu'] == '404':
			new_text_content = "\n————————————————————\n当前回帖下找不到回复\n————————————————————"
			new_text(new_text_content)
			time.sleep(5)
			#print("404")
			return(statu)
		elif statu['statu'] == '429':
			#print("429")
			time.sleep(10)
			to_find(j=j,k=k,all_data=all_data,reply_reply=reply_reply,choose_unreply=choose_unreply,main=main)
		else:
			time.sleep(5)
			#print("200")
			return(statu)
	return("not me")

def find(page, j, k, reply_id, reply_msg, sender_content, sender_name, sender_title, reply_reply,choose_unreply,main):
	"""处理已经定位了具体的帖子，寻找帖子下回帖的部分"""
	#print("被调用：" + str(reply_id))
	#more_information_url = "https://api.codemao.cn/web/forums/replies/" + j["id"] + "/comments?limit=30&page=" + str(page)
	#more_information_web = r.get(more_information_url, headers=headers, timeout=2)
	#m_i_content = re_sub(more_information_web.text)

	#right = False
	try:
		#for k in m_i_content['items']:
		#    if k['id'] == str(reply_id):

				#reply_msg = "但不管怎么说，观澜已经是公认的大佬了啊"

		if reply_reply:
			finily_url = "https://api.codemao.cn/web/forums/replies/" + str(j['id']) +"/comments"
			#print("用作API地址的str(j)：" + str(j))
		else:
		#print(str(eval(k['content'])['message']['replied_id']))
			finily_url = "https://api.codemao.cn/web/forums/replies/" + str(eval(k['content'])['message']['replied_id']) + "/comments"
			#print("用作API地址的str(k['content']['message']['replied_id'])：" + str(eval(k['content'])['message']['replied_id']))
			#finily_url = "https://api.codemao.cn/web/forums/replies/" + \
			#    str(j['content']['message']['reply_id']) + "/comments"
		finily_content = {"parent_id": reply_id, "content": reply_msg}
		#print(finily_content)
		#print("用作parent_id的'reply_id':" + str(reply_id))
		#print("用作API地址的str(k['content']['message']['replied_id'])：" + str(eval(k['content'])['message']['replied_id']))
		finily_web = to(finily_url,1,finily_content)
		if finily_web.status_code == 404:
			statu = {'statu':"404", 'sender_title':sender_title, 'sender_name':sender_name,'sender_content': sender_content}
			#print("404的statu:" + str(statu))
			return(statu)
			#new_text_content = "\n————————————————————\n回帖API状态码：" + str(finily_web.status_code) + "\n回帖API返回值：<对方已撤回消息>\n原贴名称：" + sender_title + "\n回复人：" + sender_name + "\n回复内容："+ sender_content + "\n" + "————————————————————"
		#    new_text(new_text_content)
		elif finily_web.status_code == 429:
			statu = {'statu':"429","headers":finily_web.headers, 'sender_title':sender_title, 'sender_name':sender_name,'sender_content': sender_content}
			print("429！！！")
			return(statu)
		else:
			if choose_unreply:
				new_text_content = "————————————————————\n回帖API状态码：" + str(finily_web.status_code) + "\n回帖API返回值：" + str(finily_web.text)+ "\n回帖API地址：" + str(finily_url) + "\n原贴名称：" + sender_title + "\n回复人(已取消自动回复)：" + sender_name + "\n回复内容："+ sender_content + "\n晓寒的回复：" + reply_msg + "\n————————————————————"
			else:
				new_text_content = "————————————————————\n回帖API状态码：" + str(finily_web.status_code) + "\n回帖API返回值：" + str(finily_web.text)+ "\n回帖API地址：" + str(finily_url) + "\n原贴名称：" + sender_title + "\n回复人：" + sender_name + "\n回复内容："+ sender_content + "\n晓寒的回复：" + reply_msg + "\n————————————————————"
			write_right = new_text(new_text_content)
			if write_right == "err":
				if choose_unreply:
					new_text_content = "————————————————————\n回帖API状态码：" + str(finily_web.status_code) + "\n回帖API返回值：" + str(finily_web.text)+ "\n回帖API地址：" + str(finily_url) + "\n原贴名称：" + sender_title + "\n回复人(已取消自动回复)：" + sender_name + "\n回复内容："+ sender_content + "\n晓寒的回复：<因编码问题无法写入>\n————————————————————"
				else:
					new_text_content = "————————————————————\n回帖API状态码：" + str(finily_web.status_code) + "\n回帖API返回值：" + str(finily_web.text)+ "\n回帖API地址：" + str(finily_url) + "\n原贴名称：" + sender_title + "\n回复人：" + sender_name + "\n回复内容："+ sender_content + "\n晓寒的回复：<因编码问题无法写入>\n————————————————————"
				new_text(new_text_content, again=True)
										#msg.set(str(msg.get()) + "\n" + "————————————————————")
										#msg.set(str(msg.get()) + "\n" + "回帖API状态码：" + str(finily_web.status_code))
										#msg.set(str(msg.get()) + "\n" + "回帖API返回值：" + str(finily_web.text))
										#msg.set(str(msg.get()) + "\n" + "————————————————————")

										#print("回帖API状态码：" + str(finily_web.status_code))
										#print("回帖API返回值：" + str(finily_web.text))
			#right = True
			#print(reply_msg)
			#time.sleep(5)
			threading_like = like(reply_id, the_id=str(main["sender"]["id"]))
			threading_like.start()

			statu = {'statu':"not404", 'sender_title':sender_title, 'sender_name':sender_name,'sender_content': sender_content}
			#print("202的statu:" + str(statu))
			return(statu)

									
	except KeyError:
		pass

	#if not right:
		#print(m_i_content['items'])
		#if m_i_content['items'] == []:
			#new_text_content = "————————————————————\n回帖未找到（此页为空）！\n————————————————————"
			#new_text(new_text_content)
			#print("\n空：" +str(more_information_url)+"\n")
			#right = False
			#return(0)
		#else:
			#new_text_content = "————————————————————\n在当前页回帖未找到！正在准备查找下一页内容"
			#new_text(new_text_content)
			#msg.set(str(msg.get()) + "\n回帖未找到！")
			#find(page=page + 1,j=j , reply_id=reply_id, reply_msg=reply_msg,sender_content=sender_content,sender_name=sender_name,sender_title=sender_title)
	#exit()

def go(times, reply_times):
	"""监听有无新消息，以及将每一个待处理消息遍历调用before_find()"""
	global cmd_content

	try:

		count_url = "https://api.codemao.cn/web/message-record/count"
		web = to(count_url,0)
		#real_web = r.get(real_url, headers=headers, timeout=2)
		content = re_sub(web.text)
		#print(content)
		#real = re_sub(real_web.text)
		#print(real["items"])
		new_text_content = str(content[0]["count"]) + "回复"
		new_text(new_text_content)
		#cmd.focus_force()
		#msg.set(str(msg.get()) + "\n" + str(times) + "、当前：" + str(content[0]["count"]) + "回复")
		#print(str(times) + "、当前：" + str(content[0]["count"]) + "回复")

		if reply_times == -1:
			#正常模式
			if content[0]["count"] != 0:
				#pass
			#else:
				#content[0]["count"] = 1

				msgs_url = "https://api.codemao.cn/web/message-record?query_type=COMMENT_REPLY&limit=30&offset=0"
				msgs_web = to(msgs_url,0)
			#print(re_sub(msgs_web.text))
				msgs_content = re_sub(msgs_web.text)
				need_reply = []
				for reply_number in range(0, int(content[0]["count"])):
					need_reply.append(msgs_content['items'][reply_number])

				#print(need_reply)

				for k in need_reply:
					#print("k:" + str(k))
					#BOSSBUG此处正常
					before_find(k=k)
		else:
			#调试模式
			content[0]["count"] = reply_times

			msgs_url = "https://api.codemao.cn/web/message-record?query_type=COMMENT_REPLY&limit=30&offset=0"
			msgs_web = to(msgs_url,0)
			#print(re_sub(msgs_web.text))
			msgs_content = re_sub(msgs_web.text)
			need_reply = []
			for reply_number in range(0, int(content[0]["count"])):
				need_reply.append(msgs_content['items'][reply_number])

			for k in need_reply:
				#print("k:" + str(k))
				before_find(k=k)

			exit()
	except r.exceptions.RequestException as e:
		new_text_content = "请求超时 ： " + str(e)
		new_text(new_text_content)
		#msg.set(str(msg.get()) + "\n" + str(times) + "、请求超时 ： " + str(e))
		#print(str(times) + "、请求超时 ： " + str(e))
		time.sleep(3)
		return(0)
	#except Exception as e:
		#print(cmd_content)
		#new_text_content = str(times) + "、抛出异常：\n"
		#new_text(new_text_content)
		#new_text_content = str(e)
		#new_text(new_text_content)
		#print(e)
		#msg.set(str(msg.get()) + "\n" + str(times) + "、抛出异常")
		#print(str(times) + "、抛出异常")
		#time.sleep(3)
		#return(0)


def new_text(new_text_content,again=False):
	"""用于更新日志的内容"""
	global cmd
	global cmd_content

	while put_right :
		pass    

	#txt = cmd.get("0.0", "end")

	#print("txt: " + txt,end="\n\n")
	#print("cmd_cotent: " + cmd_content,end="\n\n")
	#print(str(txt) == str(cmd_content.strip()))

	#if txt.rstrip("\n") == cmd_content:
		#all_new_content = cmd_content + new_text_content

		#print("正常")
	#else:
		#cmd_content = cmd_content + "\n" + str(time.strftime("%H:%M:%S",time.localtime())) +"：" +new_text_content
		#cmd['state'] = tk.NORMAL
		#cmd.delete(1.0,tk.END)
		#cmd.insert('end',cmd_content)
		#cmd['state'] = tk.DISABLED

	file_name = os.path.abspath(
		'.') + r'/logs/'+str(time.strftime("%Y-%m-%d", time.localtime())) + ".txt"

	the_return = 0

	try:
		with open(file_name,"a+", encoding="gbk") as f:
			f_content = "\n" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————"+ new_text_content
			f.write(f_content)
		#return(0)
	except FileNotFoundError:
		with open(file_name, "w", encoding="gbk"):
			pass
		#return(0)
	except UnicodeEncodeError:
		if again:
			with open(file_name,"a+", encoding="gbk") as f:
				f.write("\n<编码错误导致无法正常写入>")
		the_return = "err"

	

	if not again:
		for i in range(0,len(cmd_content)):
			cmd_content=cmd_content.replace("\n\n","\n")
		cmd['state'] = tk.NORMAL
		cmd.insert('end',str(time.strftime("%H:%M:%S",time.localtime())) +"：" +new_text_content+"\n")
		cmd['state'] = tk.DISABLED
		cmd_content = cmd_content + new_text_content
		
	return(the_return)

def re_sub(b):
	a = re.sub('true','True',b)
	a = eval(re.sub('false','False',a))
	return(a)

def on_closing():
	global die

	if messagebox.askokcancel("警告", "您确定要关闭吗"):
		window.destroy()
		#th.Thread._Thread__stop(threading_ask)
		die = True

		exit()


class look(th.Thread):
	"""伪主进程"""
	def __init__(self, reply_times=-1):
		th.Thread.__init__(self)

		self.reply_times = reply_times
	
	def run(self):
		global die

		while put_right :
			pass

		times = 1
		while True:
			if die:
				exit()
			
			try_to_do('go', times, self.reply_times)
			time.sleep(10)
			times += 1
			

class put(th.Thread):
	"""用于tkinter的GUI"""
	def __init__(self):
		th.Thread.__init__(self)

	def run(self):
		global cmd_content #交互全局化终端内容
		global cmd#交互全局化终端
		global window#全局化根窗口
		#global to_time_content#交互全局化时间戳
		global to_time#更新时间戳第二种办法


		window = tk.Tk()
		window.title("RobotRepeat")
		window.geometry("800x500") 
		window.resizable(width=False, height=False)
		try:
			window.iconbitmap(os.path.abspath('.') + r'/data/information/ico.ico')
		except:
			pass

		#window.protocol("WM_DELETE_WINDOW", on_closing)#监听程序关闭


		#msg=tk.StringVar()
		cmd_content = "RobotRepeat系统开始工作~\n————————————————————"

		cmd = tk.Text(window, width=47,height=29,font=(10), bg="white",state = tk.DISABLED)
		cmd.place(x=400, y=20)

		scroll = tk.Scrollbar(window)
		#scroll.place(x=780, y=20)
		scroll.pack(side=tk.RIGHT,fill=tk.Y)
		scroll.config(command=cmd.yview)
		cmd.config(yscrollcommand=scroll.set)

		#to_time_content = tk.StringVar()
		#print(to_time_content)

		to_time = tk.Label(window,text="程序正常启动！",font=(15))
		to_time.place(x=5,y=470)
		#print(to_time_content.get())

		put_right = True
		window.mainloop()

class put_time(th.Thread):
	"""用于GUI的实时更新时间"""
	def __init__(self):
		th.Thread.__init__(self)

	def run(self):
		global to_time

		start_time = int(time.time())

		while put_right :
			pass

		time.sleep(3)

		while True:
			if die:
				exit()
			the_real_time = int(time.time()) - start_time
			m,s = int(the_real_time/60),the_real_time % 60
			h,m = int(m/60),m % 60
			#to_time_content.set("开始使用工具"+str(h)+"小时"+str(m)+"分钟"+str(s)+"秒后")
			to_time['text'] = "开始使用工具"+str(h)+"小时"+str(m)+"分钟"+str(s)+"秒后"
			time.sleep(1)

class like(th.Thread):
	"""用于回复完后的点赞"""
	def __init__(self,reply_id,the_id):
		th.Thread.__init__(self)
		self.reply_id = reply_id
		self.the_id=the_id

	def run(self):
		if_like = True

		file_name = os.path.abspath('.') + r'/data/unlike.txt'
		with open(file_name, encoding="utf-8-sig") as f:
			f.seek(0)
			every_each = f.read().split(",")
			if every_each != ['']:
				for each in every_each:
					if str(each).strip() == str(self.the_id).strip():
						#如果回复的人在取消点赞的名单之内
						if_like = False

		if if_like:
			like_url = "https://api.codemao.cn/web/forums/comments/" + str(self.reply_id) + "/liked?source=COMMENT"
			to(like_url,2)

class robot_reply(th.Thread):
	"""用于自动回帖"""
	def __init__(self):
		th.Thread.__init__(self)

	def run(self):
		for uid in range(313830,313840):
			try_to_do('go_reply', uid)
			if die:
				exit()
			time.sleep(5)

def go_reply(uid):
	url = "https://api.codemao.cn/web/forums/posts/" + str(uid) + "/replies"
	
	contents = {"content": "<p>Hi~ o(*￣▽￣*)ブ我就是由主人自主研发的全编程猫第一个社区自动回复机器人——晓寒啦（晓寒的主人当然就是我的制作者——渠源哒！）。欢迎通过回复的方式与晓寒进行互动哦，晓寒会第一时间回复你哒！╰(*°▽°*)╯（主人说晓寒的功能还没完全开发完毕，因此不要对晓寒失望哦）。另外要是不愿意自己的帖子变成99+，也可以选择删除我的回复<img src=\"http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/b6/doge_thumb.gif\" alt=\"emotion_doge\"></p><p>以下，就是我目前的功能(虽然目前有点少，但是请静候主人将我升级哦)：</p><p>“/不再回复”、“/恢复回复”、“/讲笑话”、“/最新活动”、“/自定义回复”、“/切换点赞模式”……</p><p></p><p>PS：部分回复可能因为一些奇奇怪怪のBUG而无法进行及时回复，主人已经在加紧修复咯，还请见谅~</p>"}
	web = to(url,1, contents)
	print(str(uid) + " ：" + str(web.status_code))
	if web.status_code != 200:
		print(web.text)


class go_search(th.Thread):
	"""用于自动寻找帖子"""
	def __init__(self):
		th.Thread.__init__(self)

	def run(self):
		while True:
			try_to_do('search')
			if die:
				exit()
			time.sleep(20)

def search():
	search_url = r"https://api.codemao.cn/web/forums/posts/search?title=@" + str(quote(datas['name'][1:3], safe=";/?:@&=+$,", encoding="utf-8"))
	#print(search_url)
	search_web = to(search_url,0)
	search_content = re_sub(search_web.text)
	#print(search_content)
	for l in search_content['items']:
		try:
			file_name = os.path.abspath('.') + '\\data\\searched.txt'
			with open(file_name,"a+") as f:
				f.seek(0)
				all_searched = f.read().split(",")
				#print(all_searched)
				if all_searched == ['']:
					all_searched = ['257435']
		except FileNotFoundError:
			with open(file_name, "w") as f:
				f.write("257435")
			all_searched = ['257435']
				

		#print("初始化完后的all_saerched:" + str(all_searched))

		if str(l['id']) not in all_searched:
			#all_searched.append(str(l['id']))
			#print("添加完后的all_searched:" + str(all_searched))

			be_searched_contents = {"content": str(datas['be_searched'])}
			#be_searched_contents = {"content": "<p>抱歉，由于一些特殊原因，晓寒暂时不能回复了，请静候明天4点解封Σ( ° △ °|||)︴</p><p>详细内容请见：https://shequ.codemao.cn/community/313219</p>"}
			be_searched_url = "https://api.codemao.cn/web/forums/posts/" + str(l['id']) + "/replies"
			be_searched_web = to(be_searched_url,1,be_searched_contents)

			new_text_content = "————————————————————\n回应@的API状态码：" + str(be_searched_web.status_code) + "\n回应@的API返回值：" + str(be_searched_web.text)+ "\n回应@的API地址：" + str(be_searched_url) + "\n原贴名称：" + str(l['title']) + "\n发帖人：" + str(l['user']['nickname']) + "\n————————————————————"
			write_right = new_text(new_text_content)
			if write_right == "err":
				new_text_content = "————————————————————\n回应@的API状态码：" + str(be_searched_web.status_code) + "\n回应@的API返回值：" + str(be_searched_web.text)+ "\n回应@的API地址：" + str(be_searched_url) + "\n原贴名称：<因编码问题无法写入>\n发帖人：" + str(l['user']['nickname']) + "\n————————————————————"
				new_text(new_text_content, again=True)

			file_name = os.path.abspath('.') + '\\data\\searched.txt'
			with open(file_name,"a+") as f:
				#print("写入前的的all_searched:" + str(all_searched))
				#for every_id in all_searched:
					#try:
						#all_id = all_id + "," + every_id
					#except NameError:
						#all_id = every_id

					#print("all_id:" + all_id)
					
				#f.seek(0)
				#f.truncate()
				f.write("," + str(l['id']))

		time.sleep(10)


	return(0)


class go_to(th.Thread):
	"""用于传送召唤"""
	def __init__(self,uid,reply_name):
		th.Thread.__init__(self)
		self.uid = uid
		self.reply_name = reply_name

	def run(self):
		the_return = to_go_to(self.uid,self.reply_name)
		get_web_content = the_return['get_web_content']
		try:
			new_text_content = "————————————————————\n被传送帖子的API状态码(POST与GET)：" + str(the_return['status_code']) + ";" + str(the_return['get_statu']) + "\n传送人名称：" + str(the_return['reply_name']) + "\n目标贴名称：" + str(get_web_content['title']) + "\n目标贴发帖人：" + str(get_web_content['user']['nickname']) + "\n————————————————————"
			#reply_msg = "【晓寒】晓寒已成功被召唤到目标帖子："+ str(get_web_content['title'])
		except KeyError:
			new_text_content = "————————————————————\n被传送帖子的API状态码(POST与GET)：" + str(the_return['status_code']) + ";" + str(the_return['get_statu'])+ "\n传送人名称：" + str(the_return['reply_name']) + "\n目标贴名称：<404>\n目标贴发帖人：<404>\n————————————————————"
			#reply_msg = "【晓寒】目标帖子找不到啦！"
		write_right = new_text(new_text_content)
		if write_right == "err":
			try:
				new_text_content = "————————————————————\n被传送帖子的API状态码(POST与GET)：" + str(the_return['status_code']) + ";" + str(the_return['get_statu']) +"\n传送人名称：<因编码问题无法写入>\n目标贴名称：<因编码问题无法写入>\n目标贴发帖人：<因编码问题无法写入>\n————————————————————"
				#reply_msg = "【晓寒】晓寒已成功被召唤到目标帖子："+ str(get_web_content['title'])
			except KeyError:
				new_text_content = "————————————————————\n被传送帖子的API状态码(POST与GET)：" + str(the_return['status_code']) + ";" + str(the_return['get_statu']) + "\n传送人名称：<因编码问题无法写入>\n目标贴名称：<404>\n目标贴发帖人：<404>\n————————————————————"
				#reply_msg = "【晓寒】目标帖子找不到啦！"
			new_text(new_text_content, again=True)


def to_go_to(uid,reply_name):
	try:
		community_url = "https://api.codemao.cn/web/forums/posts/" + str(uid) + "/replies"	
		contents = {"content": datas['go'].replace('`reply_name`',reply_name)}
		web = to(community_url,1, json=contents)
		community_url = "https://api.codemao.cn/web/forums/posts/" + str(uid) + "/details"
		get_web = to(community_url,0)
		get_web_content = re_sub(get_web.text)
	except:
		time.sleep(5)
		to_go_to(uid,reply_name)

	the_return = {'status_code':str(web.status_code),'get_statu':str(get_web.status_code),'reply_name':str(reply_name),'get_web_content':get_web_content}
	return(the_return)
	

class like_works(th.Thread):
	"""用于点赞作品"""
	def __init__(self,reply_id):
		th.Thread.__init__(self)
		self.reply_id = reply_id

	def run(self):
		the_return = try_to_do('like_all_works', self.reply_id)
		#get_web_content = the_return['get_web_content']
		new_text_content = "————————————————————\n目标要求点赞的作品总数：1\n目标要求点赞的作品成功数：" + str(the_return['like_ok_length']) + "\n目标要求点赞的作品id：" + str(the_return['like_ok']) + "\n目标要求人：" + str(the_return['like_worker']) + "\n————————————————————"
		write_right = new_text(new_text_content)
		if write_right == "err":
			new_text_content = "————————————————————\n目标要求点赞的作品总数：1\n目标要求点赞的作品成功数：" + str(the_return['like_ok_length']) + "\n目标要求点赞的作品id：" + str(the_return['like_ok']) + "\n目标要求人：<因编码问题无法写入>\n————————————————————"
			new_text(new_text_content, again=True)


def like_all_works(user_id):
	#print(user_id)
	#like_ok = []
	like_ok_length = 0
	#works_length = 0
	#all_works_url = "https://api.codemao.cn/api/user/works/published?user_id=" + str(user_id) + "&types=1"
	all_works_url = "https://api.codemao.cn/api/user/info/detail/" + str(user_id)
	print(to(all_works_url,0))
	all_works_web = re_sub(to(all_works_url,0).text)
	#print(all_works_web)
	try:
		work_id = all_works_web['data']['userInfo']['work']['id']
		like_worker = all_works_web['data']['userInfo']['user']['nickname']
		url = "https://api.codemao.cn/web/works/" + str(work_id) + "/like"
		web = to(url,3)
		if str(web.status_code) == "204":
			like_ok_length = 1
			
		#like_ok.append(str(work['work_id']))
		#like_worker = str(work['nickname'])
		#for work in all_works_web['data']['works']:
			#url = "https://api.codemao.cn/web/works/" + str(work['work_id']) + "/like"
			#web = r.patch(url=url,headers=headers,timeout=5)
			#if str(web.status_code) == "204":
				#like_ok_length += 1
				#print(str(url))

			#like_worker = str(work['nickname'])
			#like_ok.append(str(work['work_id']))
			#works_length += 1
			#time.sleep(10)
	except KeyError:
		the_return = {'like_ok':"none",'like_ok_length':"none",'like_worker':'none'}

	the_return = {'like_ok':work_id,'like_ok_length':like_ok_length,'like_worker':like_worker}
	return(the_return)

def to(url, requests_type, json={}):
	"0为get，1为post，2为put，3为patch"
	try:
		if requests_type == 0:
			web = r.get(url, headers=headers, timeout=5)
		elif requests_type == 1:
			web = r.post(url, headers=headers, timeout=5, json=json)
		elif requests_type == 2:
			web = r.put(url, headers=headers, timeout=5)
		elif requests_type == 3:
			web = r.patch(url, headers=headers, timeout=5)

		return(web)

	except r.exceptions.RequestException as e:
		web = to(url, requests_type, json={})
		return(web)


def try_to_do(func,*c):
	#print(c)
	if c != ():
		string = str(func) + "("
		for i in c:
			string += str(i) + ","

		string = string[:-1]
		string += ")" 
		#print(string)

	else:
		string = str(func) + "()"	
		#print(string)
	
	try:
		return(eval(string))
	except:
		print(traceback.format_exc())
		file_name = os.path.abspath('.') + '\\errs\\'+str(time.strftime("%Y-%m-%d", time.localtime())) + ".txt"
		try:
			with open(file_name,"a+") as f:
				f.write(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————\n"+ traceback.format_exc() + "\n")
				#print(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————\n"+ traceback.format_exc() + "\n")
		except FileNotFoundError:
			with open(file_name, "w") as f:
				f.write(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————\n"+ traceback.format_exc() + "\n")


try:
	now_to_time = ""
	cmd_content = "编程猫自动回复工具开始工作~"
	put_right = False
	die = False

	#threading_reply = robot_reply()
	#threading_gui.setDaemon(True)
	#threading_reply.start()

	datas = find_txt(os.path.abspath('.'))
	headers = {'cookie':datas['cookies'],'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

	#time.sleep(3600)

	threading_gui = put()
	threading_gui.setDaemon(True)
	threading_gui.start()

	threading_ask = look(-1)
	threading_ask.setDaemon(True)
	threading_ask.start()

	threading_time = put_time()
	threading_time.setDaemon(True)
	threading_time.start()

	threading_search = go_search()
	threading_search.setDaemon(True)
	threading_search.start()

	threading_gui.join()



except:
	print(traceback.format_exc())
	file_name = os.path.abspath('.') + '\\errs\\'+str(time.strftime("%Y-%m-%d", time.localtime())) + ".txt"
	#print(file_name)
	try:
		with open(file_name,"a+") as f:
			f.write(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————\n"+ traceback.format_exc() + "\n")
			#print(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————\n"+ traceback.format_exc() + "\n")
	except FileNotFoundError:
		with open(file_name, "w") as f:
			f.write(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) +"————\n"+ traceback.format_exc() + "\n")
