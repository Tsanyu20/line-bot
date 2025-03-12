import os
#linebotTest1
from flask import Flask
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

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
    # if mtext == '功能關鍵字清單':
    #     try:
    #         message = TextSendMessage(
    #             text='請選擇要執行的動作：',
    #             quick_reply=QuickReply(
    #                 items=[
    #                     QuickReplyButton(
    #                         action=MessageAction(label='預約自取', text='線上訂餐稍後取')),
    #                     QuickReplyButton(
    #                         action=MessageAction(label='預約外送', text='外送到我家')),
    #                     QuickReplyButton(
    #                         action=MessageAction(label='我要看菜單', text='菜單')),
    #                     QuickReplyButton(
    #                         action=MessageAction(label='我需要推薦', text='推薦')),
    #                     QuickReplyButton(
    #                         action=MessageAction(label='查詢店家地址', text='店家地址')),
    #                     QuickReplyButton(
    #                         action=MessageAction(label='我要結帳', text='結帳'))
    #                 ]
    #             )
    #         )
    #         line_bot_api.reply_message(event.reply_token, message)
    #     except:
    #         line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    if mtext == '線上訂餐稍後取' or mtext == '外送到我家':
        try:
            message = StickerSendMessage(
                package_id='1',
                sticker_id='2'
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '菜單':
        try:
            message = TextSendMessage(text='菜單OK')
            # message = FlexSendMessage(
            #     alt_text='看菜單',
            #     contents=menu()
            # )
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
    elif  mtext == '結帳':
        try:
            message = FlexSendMessage(
                alt_text='收據',
                contents=total()
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='如果不知如何使用，可以點擊以下按鈕，選擇功能唷！',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            actoin=MessageAction(label="點我查看！", text='功能關鍵字清單'))
                    ]
                )
            )
        )
# def menu():
#     contents= {
#         "type" : "carousel",
#         "contents" : [
#             {
#                 "type" : "bubble",
#                 "body" : {
#                     "type" : "box",
#                     "layout" : "vertical",
#                     "spacing" : "md",
#                     "action" : {
#                         "type" : "uri",
#                         "uri" : "https://line.me/"
#                     },
#                     "contents" : [
#                         {
#                             "type": "text",
#                             "text": "湯類",
#                             "size": "xl",
#                             "weight": "bold"
#                         },
#                         {
#                             "type" : "box",
#                             "layout" : "vertical",
#                             "spacing" : "sm",
#                             "contents" : [
#                                 {
#                                     "type": "box",
#                                     "layout" : "baseline",
#                                     "contents" : [
#                                         {
#                                             "type": "text",
#                                             "text": "排骨湯",
#                                             "weight" : "bold",
#                                             "margin" : "sm",
#                                             "flex" : 0
#                                         },
#                                         {
#                                             "type": "text",
#                                             "text": "40元",
#                                             "size": "sm",
#                                             "align": "end",
#                                             "color": "#aaaaa"
#                                         }
#                                     ]
#                                 }
#                             ]
#                         },
#                         {
#                             "type": "text",
#                             "text": "菜頭、金針、酸菜、香菇、苦瓜",
#                             "wrap": True,
#                             "color": "#fff",
#                             "size": "xs"
#                         }
#                     ]
#                 },
#                 "footer" : {
#                     "type" : "box",
#                     "layout" : "vertical",
#                     "contents" : [
#                         {
#                             "type": "button",
#                             "style": "primary",
#                             "color": "#905c44",
#                             "margin": "xxl",
#                             "action": {
#                                 "type": "uri",
#                                 "label": "Add to Cart",
#                                 "uri": "https://line.me/"
#                             }
#                         }
#                     ]
#                 }
#             },
#             {
#                 "type" : "bubble",
#                 "body" : {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [
#                         {
#                             "type": "text",
#                             "text": "RECEIPT",
#                             "weight": "bold",
#                             "color": "#1DB446",
#                             "size": "sm"
#                         }
#                     ]
#                 }
#             }
#         ]
#     }
#     return contents

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