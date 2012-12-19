#Goes to the documentation for BennuBot
import urllib2
plugName = 'Documents'

def docs_locate():
    req = urllib2.Request('https://github.com/titegtnodI/BennuBot/wiki')
    res = urllib2.urlopen(req)
    data = res.read()
    data = data[data.index('<title>')+7:data.index('</title>')]
    return data.decode('utf-8'), res.geturl()

def docs_get(inMSG):
    splitMSG = inMSG[0].split()
    if len(splitMSG) == 1:
        name, url = docs_locate()
        return name + ' - ' + url
    else:
        sendMSG("Usage: "+funcPrefix+"docs", inMSG[1], inMSG[2], inMSG[3])

def load():
    return {'docs':docs_get}
