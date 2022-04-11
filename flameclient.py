import os
import requests
import json
from datetime import datetime
from dacite import Config, from_dict
from dotenv import load_dotenv
from typing import List
import utilz

from models.requestresult import Result_Categories, Result_Bookmarks
from models.bookmark import Bookmark
from models.categories import Category

class FlameClient():
  
  def __init__(self, endpoint: str, password: str):
    """
    endpoint: needs to be the full url of the flame server include the "/api" at the end
    """
    self.endpoint: str = endpoint
    self._password: str = password
    self._duration: str = "1y"

    # ensure the endpoint has a slash at the end of the url
    if not self.endpoint.endswith("/"):
      self.endpoint = self.endpoint + "/"
      
  def authenticate(self) -> None:
    url = "{endpoint}auth".format(endpoint=self.endpoint)
    data = { "password": self._password, "duration": self._duration}
    hed = { "Accept": "*/*" }
    response = requests.post(url, json=data, headers=hed)
    
    result = response.json()

    if result["success"]:
      self.auth_token: str = result['data']['token']
    else:
      self.auth_token: str = ''

  def get_auth_header(self) -> object:
    return {'Content-Type':'application/json',
               'Authorization': 'Bearer {}'.format(self.auth_token)}
    
    #return {'Authorization': 'Bearer ' + self.auth_token}

  def get_categories(self) -> List[Category]:
    url = "{endpoint}categories".format(endpoint=self.endpoint)
    hed = self.get_auth_header()
    data = {}
    response = requests.get(url, json=data, headers=hed)
    json_val = response.json()
    result = from_dict(Result_Categories, json_val, Config({datetime: datetime.fromisoformat}))

    return result.data

  def create_bookmark(self, bookmark: Bookmark):
    url = "{endpoint}bookmarks".format(endpoint=self.endpoint)
    authenticator = self.get_auth_header()
    data = json.loads(json.dumps(bookmark, default=utilz.serialize))
    response = requests.post(url, json=data, headers=authenticator)
    json_val = response.json()


if __name__ == "__main__":
  load_dotenv()

  ENDPOINT = os.environ.get("ENDPOINT")
  PASSWORD = os.environ.get("PASSWORD")

  client = FlameClient(ENDPOINT, PASSWORD)

  client.authenticate()

  categories = client.get_categories()
  
  for x in categories:
    print("{id} - {name} - {numbookmarks}".format(id=x.id, name=x.name, numbookmarks=len(x.bookmarks)))


  bm = Bookmark(id=None, name="testing", url="https://google.ca/", category_id=2, icon="book", is_public=0, order_id=None, created_at=datetime.now(), updated_at=datetime.now())

  client.create_bookmark(bm)