import vk_requests
from time import gmtime, strftime

token = ""
api = vk_requests.create_api(service_token=token, scope=['friends', 'messages', 'wall', 'offline'])
chatid = 1 #place here your conversation id

def sendMessage(par):
    print('# sendMessage called')
    if par[0] == 1: #date
        letsSendIt = api.messages.send(user_id=chatid, random_id=random.getrandbits(128), message=par[1])
        print ('# sent!')
        
def searchMessage():
    print('# searchMessage called')
    getMessage = api.messages.search(q='!бот',peer_id='124057393',count=1)
    getMessageBody = getMessage['items'][0]['body']
    return getMessageBody

def initalizeRequest():
    print('# initalizeRequest called')
    callMessage = searchMessage()
    print('# continue')
    if callMessage == '!бот время':
        print('# date callMessage found')
        sendMessage(_retTime())
    elif callMessage == '!бот погода':
        print('# weather callMessage found')
        return 0 # функция времени
    else:
        print('# no messages found')
        return 0

def _retTime():
    print('# _reqTime called')
    return (1, strftime("%Y-%m-%d %H:%M:%S", gmtime()))

while True:
    print('# iteration')
    initalizeRequest()
    time.sleep(1)

    
