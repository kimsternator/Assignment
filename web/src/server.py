from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response
import pyramid.httpexceptions as exc

import mysql.connector as mysql
import os

import json

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/coming_soon.html', {'users': records}, request=req)

def welcome(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/welcome.html', {'users': records}, request=req)

def cv(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/coming_soon.html', {'users': records[0]}, request=req)

def avatar(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/coming_soon.html', {'users': records[0]}, request=req)

def personal(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/coming_soon.html', {'users': records[0]}, request=req)

def education(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/coming_soon.html', {'users': records[0]}, request=req)

def project(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/coming_soon.html', {'users': records[0]}, request=req)

#*****************************************************************

def add_user(req):
  req_fields = ["first_name", "last_name", "email", "comment"]
  new_user = req.POST.mixed()

  # if (sorted(req_fields) == sorted(list(new_user.keys()))):
  #   db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  #   cursor = db.cursor()
  #   cursor.execute("insert into Users (first_name, last_name, email, comment) values ("")
  #
  # else:
  #   return exc.HTTPBadRequest()
  print(new_user)
  print(type(new_user))

  return exc.HTTPCreated()

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route("welcome", "/welcome")
  config.add_view(welcome, route_name="welcome")

  config.add_route('add_user', '/add_user')
  config.add_view(add_user, route_name='add_user', renderer='json', request_method='POST')

  config.add_route("cv", "/cv")
  config.add_view(cv, route_name="cv")

  config.add_route("avatar", "/avatar")
  config.add_view(avatar, route_name="avatar")

  config.add_route('personal', '/personal')
  config.add_view(personal, route_name='personal', renderer='json')

  config.add_route('education', '/education')
  config.add_view(education, route_name='education', renderer='json')

  config.add_route('project', '/project')
  config.add_view(project, route_name='project', renderer='json')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()