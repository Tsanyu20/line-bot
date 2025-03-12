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
                contents=total()
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

def total():
    contents= {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "RECEIPT",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "text",
        "text": "Brown Store",
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "text",
        "text": "Flex Tower, 7-7-4 Midori-ku, Tokyo",
        "size": "xs",
        "color": "#aaaaaa",
        "wrap": True
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Energy Drink",
                "size": "sm",
                "color": "#555555",
                "flex": 0,
                "contents": [
                  {
                    "type": "span",
                    "text": "hello, world"
                  }
                ]
              },
              {
                "type": "text",
                "text": "$2.99",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Chewing Gum",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$0.99",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Bottled Water",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$3.33",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "ITEMS",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "3",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "TOTAL",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$7.31",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "CASH",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "CHANGE",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$0.69",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "PAYMENT ID",
            "size": "xs",
            "color": "#aaaaaa",
            "flex": 0
          },
          {
            "type": "text",
            "text": "#743289384279",
            "color": "#aaaaaa",
            "size": "xs",
            "align": "end"
          }
        ]
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
if __name__ == '__main__':
    app.run()