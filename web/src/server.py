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
    # # Connect to the database and retrieve the users
    # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    # cursor = db.cursor()
    # cursor.execute("select first_name, last_name, email from Users;")
    # records = cursor.fetchall()
    # db.close()

    return render_to_response('templates/coming_soon.html', {}, request=req)


def welcome(req):
    return render_to_response('templates/welcome.html', {}, request=req)


def cv(req):
    return render_to_response('templates/coming_soon.html', {}, request=req)


def avatar(req):
    avatar_response = {"image_src": "images/chiken.jpg"}
    response = Response(body=json.dumps(avatar_response))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response


def personal(req):
    # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    # cursor = db.cursor()
    # cursor.execute("select first_name, last_name, email from Users where id=0")
    # records = cursor.fetchall()
    # db.commit()
    # db.close()
    records = {
        "first_name": "Stephen",
        "last_name": "Kim",
        "email": "sskim@ucsd.edu"
    }

    response = Response(body=json.dumps(records))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response



def education(req):
    # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    # cursor = db.cursor()
    # cursor.execute("select school, degree, major, date from Educations where id=0")
    # records = cursor.fetchall()
    # db.commit()
    # db.close()

    records = {
      "school": "University of California, San Diego",
      "degree": "Bachelor",
      "major": "Electrical Engineering",
      "date": "March 2022"
    }
    response = Response(body=json.dumps(records))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response


def project(req):
    # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    # cursor = db.cursor()
    # cursor.execute("select title, description, link, Image_src, teamID from Users where id=0")
    # records = cursor.fetchall()
    # db.commit()
    # cursor.execute("select url from Teammates where url={}".format(records["teamID"]))
    # teammates = cursor.fetchall()
    # db.commit()
    # db.close()
    #
    # print(teammates)

    records = {
      "title": "ServiceUp",
      "description": "Community Posting Board for services",
      "link": "tbd",
      "Image_src": "tbd/static/images/ServiceUp.png",
      "teamID": 0
    }
    teammates = ["link1", "link2", "link3"]
    records.pop("teamID")
    records["team"] = teammates
    response = Response(body=json.dumps(records))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response


# *****************************Data Routes************************************

def add_user(req):
    req_fields = ["first_name", "last_name", "email", "comment"]
    new_user = req.POST.mixed()

    if (sorted(req_fields) == sorted(list(new_user.keys()))):
        # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
        values = ", ".join(new_user.values())
        # cursor = db.cursor()
        # cursor.execute("insert into Users (first_name, last_name, email, comment) values (" + values + ")")
        # db.close()
        print()

        print("insert into Users (first_name, last_name, email, comment) values (" + values + ")")

        return exc.HTTPCreated()
    else:
        return exc.HTTPBadRequest()


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
