#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

# ===================================================
## this is the main part of "GSB" python bot which is
## made for VK with vk_api py @python273
## vk_api: https://github.com/python273/vk_api
## gsb: https://github.com/mdpanf/gsb-python
## MIT License (c) 2020 Vokdon & MDPanf
# ===================================================

# <!-------- IMPORT --------!>
import random
import requests
import datetime
import json
import urllib.request
## vk_api
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
import vk_api.keyboard
## my modules
from config import * # importing configurations

# <!-------- AUTH --------!>
## all data for authorization
## are indicated in configuration
## file: config/configuration.py

# <!-------- CONNECTION --------!>
vk_session = vk_api.VkApi(token=group_token)
upload = VkUpload(vk_session)  # Для загрузки изображений
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()
print('~ bot_longpoll connected with token: ' + group_token[:-80])

# <!-------- BE ONLINE --------!>
def enableOnline():
	onlineStatus = vk.groups.getOnlineStatus(group_id=group_id)['status']
	print(f'~ onlineStatus: {onlineStatus}')
	if onlineStatus != 'online':
		vk.groups.enableOnline(group_id=group_id)
		print('~ Your group online status is activated')
enableOnline()
# <!-------- LONGPOLL --------!>
def main():
	for event in longpoll.listen(): # listen longpoll
		if event.type == VkBotEventType.MESSAGE_NEW: # if a new message arrives
			# <-- variables for messages -->
			peer_id = event.object.peer_id
			from_id = event.object.from_id
			msg_text = event.object.text.lower()
			if peer_id != from_id: #сообщения в чат с ботом
				if event.object.text.startswith("!"):
					if msg_text == '!some':
						vk.messages.send(peer_id = peer_id, message = ('text'), random_id = 0)
			if peer_id == from_id: # сообщения в личку бота
				if event.object.text.startswith("!"):
					if msg_text == '!some':
						vk.messages.send(peer_id = peer_id, message = ('text'), random_id = 0)

main()
# <!-------- SOMESHIT --------!>
