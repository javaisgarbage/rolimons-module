import requests

def loadResponse(response, i1, i2):
  #open('Response.txt','w').write(response) #easier indexing
  start = response.index(i1)+len(i1)
  x = start
  while response[x] != i2: x += 1
  return response[start:x]

def getIDfromI(name):
  response = str(requests.get('https://www.rolimons.com/itemtable').text)
  #open('itemtable.txt','w').write(response) #easier indexing
  end = response.index(name)-5
  x = end
  while response[x] != '"': x -= 1
  return response[x+1:end+1]

def getIDfromP(name):
  response = str(requests.get('https://rblx.trade/u/'+name).text)
  #open('playerIndex.txt','w').write(response) #easier indexing
  start = response.index('https://www.roblox.com/users/')+29
  x = start
  while response[x] != '/': x += 1
  return response[start:x]

def loadResponseInverse(response, i1, i2):
  end = response.index(i1)
  x = end
  while response[x] != i2: x -= 1
  return response[x+1:end]

class rolimons():
  class item:
    def __init__(self, name):
      self.id = getIDfromI(name)
      self.url = 'https://rolimons.com/item/'+self.id
    def value(self):
      try: return loadResponse(str(requests.get(self.url).text),'Value=',' ')
      except: return 'None'
    def rap(self):
      return loadResponse(str(requests.get(self.url).text),'RAP=',' ')
    def avaliable_copies(self):
      return loadResponse(str(requests.get(self.url).text),'Available Copies=', ' ')
    def premium_copies(self):
      return loadResponse(str(requests.get(self.url).text),'Premium Copies=', '.')
    def demand(self):
      try: return loadResponse(str(requests.get(self.url).text),'Demand=', ' ')
      except: return 'None'
    def trend(self):
      try: return loadResponse(str(requests.get(self.url).text),'Trend=', ' ')
      except: 'None'

  class player:
    def __init__(self, name):
      self.id = getIDfromP(name)
      self.url = 'https://www.rolimons.com/player/'+self.id
    def value(self):
      return loadResponseInverse(str(requests.get(self.url).text),'],"rap":',',')
    def rap(self):
      return loadResponseInverse(str(requests.get(self.url).text),'],"num_limiteds":',',')
    def items(self):
      return loadResponseInverse(str(requests.get(self.url).text),'],"terminated":',',')