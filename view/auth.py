from linebot.models import TextSendMessage

def refuseToServe():
    return TextSendMessage(text="抱歉，您不是本公司的服務對象。若有疑問，請洽公司窗口，謝謝。")