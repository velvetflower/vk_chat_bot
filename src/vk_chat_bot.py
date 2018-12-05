import vk_requests
from time import gmtime, strftime

token = ""
api = vk_requests.create_api(service_token=token, scope=['friends', 'messages', 'wall', 'offline'])
chatid = 1 #place here your conversation id
latestCommandID = 0

def sendMessage(par):
    print('# sendMessage called')
    if par[0] == 1: #date
        letsSendIt = api.messages.send(user_id=chatid, random_id=random.getrandbits(128), message=par[1])
        print ('# sent!')

def searchMessage():
    global latestCommandID
    print('# searchMessage called')
    getMessage = api.messages.search(q='!бот',peer_id='124057393',count=1)
    print (getMessage)
    getMessageBody = getMessage['items'][0]['body']
    getMessageID = getMessage['items'][0]['random_id']
    if getMessageID != latestCommandID:
        latestCommandID = getMessage['items'][0]['random_id']
        return getMessageBody
    else:
        print ('#no new messages found')

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
