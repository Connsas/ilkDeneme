#!/usr/bin/python

from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import requests
import json as js
import random as rn

app = Flask(__name__)

api = Api(app)

def editTitle(poemTitle:str):
   poemTitle.encode('ascii')
   for item in poemTitle:
      if item == 92 or item == 32:
         item = 0
   return poemTitle

class Titles(Resource):

   def get(self):
      urlTitle = "https://poetrydb.org/title"
      responseTitle = requests.get(urlTitle)
      jsonData = responseTitle.json()
      return jsonData, 200

class Poems(Resource):

   def get(self,poemTitle):
      editedPoemTitle = editTitle(poemTitle)
      urlPoems = "https://poetrydb.org/title/"+ editedPoemTitle + "/lines.json"
      responsePoems = requests.get(urlPoems)
      jsonData = responsePoems.json()
      return jsonData, 200

api.add_resource(Titles, '/title')

api.add_resource(Poems, '/poem/<string:poemTitle>')


if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()

