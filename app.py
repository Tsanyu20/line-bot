import os
#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

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
    if mtext == '＠傳送文字':
        try:
            message = TextSendMessage(
                text='我是LineBot機器人！\n您好')
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '＠傳送圖片':
        try:
            message = ImageSendMessage(
                original_content_url='https://i.imgur.com/fwWC9HM.png',
                preview_image_url='https://i.imgur.com/fwWC9HM.png'
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '＠傳送貼圖':
        try:
            message = StickerSendMessage(
                package_id='1',
                sticker_id='2'
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '＠多項傳送':
        message = [
            TextSendMessage(
                text='我就爛！'),
            ImageSendMessage(
                original_content_url='https://i.imgur.com/fwWC9HM.png',
                preview_image_url='https://i.imgur.com/fwWC9HM.png'),
            StickerSendMessage(
                package_id='11539',
                sticker_id='52114111')
        ]
        line_bot_api.reply_message(event.reply_token, message)
    elif mtext == '＠傳送位置':
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
    elif mtext == '＠快速選單':
        try:
            message = TextSendMessage(
                text='請選擇品項',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label='雞肉飯', text='雞肉飯')),
                        QuickReplyButton(
                            action=MessageAction(label='蒸煮麵', text='蒸煮麵')),
                        QuickReplyButton(
                            action=MessageAction(label='肉羹湯', text='肉羹湯')),
                        QuickReplyButton(
                            action=MessageAction(label='燙青菜', text='燙青菜'))
                    ])
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    else:
         line_bot_api.reply_message(event.reply_token, TextSendMessage(text='蛤'))

if __name__ == '__main__':
    app.run()
