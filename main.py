import os
import sys
import logging
import json
import random
from linebot.models import (TextSendMessage, TemplateSendMessage)
from linebot import (
    LineBotApi, WebhookHandler
)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


def callback(request):
    try:
        # 取得事件JSON
        body = request.get_data(as_text=True)
        events = json.loads(body)['events']
        for event in events:
            try:
                # 在Line上面Debug
                line_bot_api.reply_message(
                    event["replyToken"], TextSendMessage(text=event["message"]["text"]))
            except Exception as e:
                line_bot_api.reply_message(
                    event["replyToken"], TextSendMessage(text="main.py:{0}".format(e)))
    # 在主控台Debug
    except:
        logging.error(sys.exc_info())
        return 'ERROR'
    return 'OK'
