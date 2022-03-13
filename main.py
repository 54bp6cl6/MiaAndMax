import sys
import logging
from botApp import LineBotApp

lineBotApp = LineBotApp()

def callback(request):
    try:
        lineBotApp.serve(request)
    # 在主控台Debug
    except Exception as ex:
        print(ex)
        return 'ERROR'
    return 'OK'