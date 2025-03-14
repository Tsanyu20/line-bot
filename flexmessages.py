def soup():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "湯類及蒸蛋",
        "weight": "bold",
        "color": "#76b33d",
        "size": "xl"
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
                "text": "人蔘雞心湯、豬腦湯",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$50",
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
                "text": "排骨湯、雞肉湯、當歸鴨湯",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$40",
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
                "text": "肉羹湯、豬肝湯、排骨酥湯",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$40",
                "size": "sm",
                "align": "end",
                "color": "#111111"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "香菇蒸蛋",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$30",
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
            "layout": "vertical",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "排骨湯：",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "菜頭、苦瓜、金針、酸菜、香菇",
                "size": "XS",
                "offsetStart": "lg"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "雞肉湯",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "香菇雞、瓜仔雞",
                "size": "XS",
                "offsetStart": "lg"
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "我要點餐",
          "text": "我要點餐"
        },
        "color": "#76b33d",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "看其他菜單",
          "text": "菜單"
        },
        "style": "primary",
        "margin": "sm",
        "color": "#ddd605"
      }
    ]
  }
}

def main_food():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "飯食及麵食（分大、小份）",
        "weight": "bold",
        "color": "#0aa1cb",
        "size": "xl"
      },
      {
        "type": "text",
        "text": "飯食",
        "offsetTop": "lg",
        "size": "md",
        "weight": "bold"
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
                "text": "雞肉飯、肉臊飯",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$40(大)/$30(小)",
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
                "text": "肉羹飯",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$60(大)/$50(小)",
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
                "text": "便當",
                "size": "sm",
                "color": "#111111"
              },
              {
                "type": "text",
                "text": "$70(加飯)/$60",
                "size": "sm",
                "align": "end",
                "color": "#111111"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "麵食",
            "size": "md",
            "weight": "bold",
            "flex": 0
          },
          {
            "type": "text",
            "size": "xxs",
            "text": "*可選油麵、米粉、蒸煮麵、雞絲麵、意麵",
            "align": "end",
            "offsetTop": "XS"
          }
        ],
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "鍋燒麵*",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$75(大)/$65(小)",
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
                "text": "鴨肉冬粉湯",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$70(大)/$50(小)",
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
                "text": "鴨肉湯麵*",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$65(大)/$50(小)",
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
                "text": "肉羹麵*",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$65(大)/$50(小)",
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
                "text": "肉臊麵*、湯麵*",
                "size": "sm",
                "color": "#111111",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$50(大)/$40(小)",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ],
        "margin": "md",
        "spacing": "sm"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "我要點餐",
          "text": "我要點餐"
        },
        "color": "#0aa1cb",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "看其他菜單",
          "text": "菜單"
        },
        "style": "primary",
        "color": "#76b33d",
        "margin": "sm"
      }
    ]
  }
}

def sides():
  pass

def veggie():
  pass

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
                                    "text": "勝美切仔担",
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

def test():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "In Progress",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "70%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "70%",
                "backgroundColor": "#0D8186",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Buy milk and lettuce before class",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Pending",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "30%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "30%",
                "backgroundColor": "#DE5658",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF6B6E",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Wash my car",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "In Progress",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "100%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "100%",
                "backgroundColor": "#7D51E4",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#A17DF5",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Buy milk and lettuce before class",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    }
  ]
}