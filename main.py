import sys
import logging
from service import Service

def callback(request):
    try:
        params = { "request" : request }
        servise = Service()
        servise.nextMiddleware(params)

    # 在主控台Debug
    except:
        logging.error(sys.exc_info())
        return 'ERROR'
    return 'OK'