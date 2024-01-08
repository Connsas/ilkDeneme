from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import pandas as pd
import requests
import json as js

app = Flask(__name__)
CORS(app)

api = Api(app)

class Titles(Resource):

   def get(self):
      urlTitle = "https://poetrydb.org/title"
      responseTitle = requests.get(urlTitle)
      jsonData = responseTitle.json()
      return jsonData, 200

class Poems(Resource):

   def get(self,poemTitle):
      urlPoems = "https://poetrydb.org/title/"+ poemTitle
      responsePoems = requests.get(urlPoems)
      jsonData = responsePoems.json()
      return jsonData, 200

class Authors(Resource):

   def get(self):
      urlAuthor = "https://poetrydb.org/author"
      responseAuthor = requests.get(urlAuthor)
      jsonData = responseAuthor.json()
      return jsonData, 200   


api.add_resource(Titles, '/title')

api.add_resource(Authors, '/author')

api.add_resource(Poems, '/title/poem/<string:poemTitle>')


if __name__ == '__main__':

   app.run(host="0.0.0.0")

   app.run()
