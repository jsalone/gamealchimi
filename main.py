# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import json, os, psycopg2, urlparse
from db import Db # voyez db.py

app = Flask(__name__)
app.debug = True

##################################################################

@app.route('/debug/db/reset')
def route_dbinit():
  """Cette route sert à initialiser (ou nettoyer) la base de données."""
  db = Db()
  db.executeFile("database_reset.sql")
  db.close()
  return "Done."

#-----------------------------------------------------------------

@app.route('/', methods=['GET'])
def home():
  return "Voir le sujet sur e-learning pour plus d'informations."
  
#-----------------------------------------------------------------

@app.route('/prets', methods=['GET'])
def prets_fetchall():
  db = Db()
  result = db.select("SELECT * FROM prets")
  db.close()
  
  resp = make_response(json.dumps(result))
  resp.mimetype = 'application/json'
  return resp

#-----------------------------------------------------------------

if __name__ == "__main__":
  app.run()