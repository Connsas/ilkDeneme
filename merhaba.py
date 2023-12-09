from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import requests
import json as js
import random as rn

app = Flask(__name__)

api = Api(app)

class Titles(Resource):

   def get(self):
      urlTitle = "https://poetrydb.org/title"
      responseTitle = requests.get(urlTitle)
      jsonData = responseTitle.json()
      jsonData = "merhaba"
      return jsonData, 200

class Poems(Resource):

   def get(self,poemTitle):
      urlPoems = "https://poetrydb.org/title/"+ poemTitle + "/lines.json"
      responsePoems = requests.get(urlPoems)
      jsonData = responsePoems.json()
      return jsonData, 200
      

api.add_resource(Titles, '/title')

api.add_resource(Poems, '/poem/<string:poemTitle>')


if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()

