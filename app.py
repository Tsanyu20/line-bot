import os
#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, FlexSendMessage
from flexmessages import *

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
    reservation = ['外送', '自取', '點餐', '訂餐','訂飯']
    reserve = [True if x in mtext else False for x in reservation]
    if mtext == '功能關鍵字清單':
        try:
            message = TextSendMessage(
                text='請選擇要執行的動作：',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label='預約訂單', text='我要點餐')),
                        QuickReplyButton(
                            action=MessageAction(label='我要看菜單', text='菜單')),
                        # QuickReplyButton(
                        #     action=MessageAction(label='我需要推薦', text='推薦')),
                        QuickReplyButton(
                            action=MessageAction(label='查詢店家地址', text='店家地址'))#,
                        # QuickReplyButton(
                        #     action=MessageAction(label='我要結帳', text='結帳'))
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '我要點餐':
        try:
            message = [
                TextSendMessage(text='以下連結是我們的點餐表單！'),
                TextSendMessage(text='https://tycreate.aidaform.com/free-product-order-form'),
                TextSendMessage(
                    text='或是以文字訊息傳菜單給我們喔！',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label='我要外送', text='線上訂餐稍後取')),
                            QuickReplyButton(
                                action=MessageAction(label='我要自取', text='外送到我家')
                            )

                        ]
                    )
                )
            ]

            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '線上訂餐稍後取' or mtext == '外送到我家' or True in reserve:
        try:
            reserve = []
            message = [
                # TextSendMessage(text='告訴我們想吃的品項，也要記得留下稱呼及電話讓我們可以辨識哦！需外送的話也請附上住址～'),
                StickerSendMessage(
                    package_id='1',
                    sticker_id='2'),
                TextSendMessage(text='等待訊息被已讀，或收到回覆才代表我們有確認訂單哦！')
            ]
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif '菜單' in mtext:
        try:
            message = TextSendMessage(
                text='請選擇想看的菜單：',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label='看湯類', text='湯類')),
                        QuickReplyButton(
                            action=MessageAction(label='看主食', text='主食')),
                        QuickReplyButton(
                            action=MessageAction(label='看切料跟燙青菜', text='切料及燙青菜'))
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '湯類':
        try:
            message = FlexSendMessage(
                alt_text='湯類菜單',
                contents=soup()
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    elif mtext == '主食':
        try:
            message = FlexSendMessage(
                alt_text='主食菜單',
                contents=main_food()
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    elif '切料' in mtext or '青菜' in mtext:
        try:
            message = [
                FlexSendMessage(
                    alt_text='切料及燙青菜菜單',
                    contents=sides()
                ),
            ]
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

    elif '店家地址' in mtext:
        try:
            message = [
                LocationSendMessage(
                    title='勝美美食',
                    address='屏東縣東港鎮朝陽街44號',
                    latitude=22.466120,
                    longitude=120.449240
                ),
                TextSendMessage(text='也可以點開我們的帳號主頁面尋找哦！')
            ]
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    # elif mtext == '結帳':
    #     try:
    #         message = FlexSendMessage(
    #             alt_text='收據',
    #             contents=total()
    #         )
    #         line_bot_api.reply_message(event.reply_token, message)
    #     except:
    #         line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '怎麼使用':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='如果不知如何使用，可以點擊以下按鈕，選擇功能唷！',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label='點我查看！', text='功能關鍵字清單'))
                    ]
                )
            )
        )



if __name__ == '__main__':
    app.run()


