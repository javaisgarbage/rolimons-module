import requests
import os

class Rolimons:
  def get_inverse_index(response, i1, i2):
    end = response.index(i1)
    x = end
    while response[x] != i2: x -= 1
    return response[x+1:end]

  def get_index(response, i1, i2):
    start = response.index(i1)+len(i1)
    x = start
    while response[x] != i2: x += 1
    return response[start:x]
    
  class User:
    def __init__(self, username=None, id=None):
      if username is None:
        self.id = id
        self.username = requests.get(f'https://users.roblox.com/v1/users/{id}').json()['name']
      else:
        self.username = username
        self.id = self.query_user(username)
      self.value, self.rap, self.inventory, self.trade_ads = self.get_metadata()

    def query_user(self, username):
      request = requests.get(f'https://users.roblox.com/v1/users/search?keyword={username}&limit=10').json()
      return request['data'][0]['id']

    def get_metadata(self):
      request = requests.get(f'https://www.rolimons.com/player/{self.id}')
      with open('raw.txt','w') as file: file.write(request.text)
      value = Rolimons.get_inverse_index(request.text, '],"rap":', ',')
      trade_ad_count = Rolimons.get_index(request.text, '"trade_ad_count":', ',')
      inventory = []
      rap = 0
      request = requests.get(f'https://inventory.roblox.com/v1/users/{self.id}/assets/collectibles?limit=100').json()
      for item in request['data']:
        rap += item['recentAveragePrice']
        inventory.append(item['assetId'])
        
      return value, rap, inventory, trade_ad_count
  
  class Item:
    def __init__(self, id):
      self.id = id
      self.raw = requests.get('https://www.rolimons.com/itemapi/itemdetails').json()['items']
      self.name = self.raw[str(self.id)][0]

      if self.raw[str(self.id)][3] == -1:
        self.value = self.raw[str(self.id)][2]
      else:
        self.value = self.raw[str(self.id)][3]
      self.rap = self.raw[str(self.id)][2]
