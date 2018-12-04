import vk_requests
from time import gmtime, strftime

token = ""
api = vk_requests.create_api(service_token=token, scope=['friends', 'messages', 'wall', 'offline'])

def searchMessage():
    getMessage = api.messages.search(q='!bot',count=1)
    getMessageBody = getMessage['items'][0]['body']
    return getMessageBody

def initalizeRequest():
    callMessage = searchMessage()
    if callMessage == '!bot time':
        _retTime()
    elif callMessage == '!bot weather':
        _retWearher()
    else:
        return 0

def _retTime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def _retWearher():
    return 0 #todo
    
