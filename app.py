import os
#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, FlexSendMessage

line_bot_api = LineBotApi(os.getenv("LINE_BOT_API"))
handler = WebhookHandler(os.getenv("WEBHOOK"))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    # Get the message sent by the user
    body = request.get_data(as_text=True)

    try:
        # Send message
        handler.handle(body, signature)
    except InvalidSignatureError:
        # Send bad request (400)
        abort(400)
    # return OK
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text(event):
    mtext = event.message.text
    if mtext == '結帳':
        try:
            message = FlexSendMessage(
                alt_text='total',
                contents={
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Hello,"
                      },
                      {
                        "type": "text",
                        "text": "World!"
                      }
                    ]
                  }
                }
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '線上訂餐稍後取':
        try:
            message = StickerSendMessage(
                package_id='1',
                sticker_id='2'
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '功能關鍵字清單':
        message = [
            TextSendMessage(

                ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    elif '店家地址' in mtext:
        try:
            message = LocationSendMessage(
                title='勝美美食',
                address='屏東縣東港鎮朝陽街44號',
                latitude=22.466120,
                longitude=120.449240
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '推薦':
        try:
            message = [
                TextSendMessage(
                    text='以下是老闆女兒的不負責推薦！'
                ),
                TextSendMessage(
                    text='最愛吃這些',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label='雞肉飯', text='雞肉飯')),
                            QuickReplyButton(
                                action=MessageAction(label='蒸煮麵', text='蒸煮麵')),
                            QuickReplyButton(
                                action=MessageAction(label='肉羹湯', text='肉羹湯')),
                            QuickReplyButton(
                                action=MessageAction(label='燙空心菜', text='燙空心菜'))
                    ])
                )
            ]
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    else:
         line_bot_api.reply_message(event.reply_token, TextSendMessage(text='蛤'))

def total():
    contents= {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                              {
                                    "type": "text",
                                    "text": "收據",
                                    "weight": "bold",
                                    "color": "#1DB446",
                                    "size": "sm"
                              },
                              {
                                    "type": "text",
                                    "text": "勝美切子担",
                                    "weight": "bold",
                                    "size": "xxl",
                                    "margin": "md"
                              },
                              {
                                    "type": "text",
                                    "text": "屏東縣東港鎮朝陽街44號",
                                    "size": "xs",
                                    "color": "#aaaaaa",
                                    "wrap": True
                              }
                    ]
                  },
                  "styles": {
                        "footer": {
                            "separator": True
                        }
                  }
    }
    return contents

if __name__ == '__main__':
    app.run()