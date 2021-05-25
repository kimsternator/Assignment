# from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.renderers import render_to_response
from pyramid.response import Response
import pyramid.httpexceptions as exc

import mysql.connector as mysql
import os
import bjoern
import json

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']


def get_home(req):
    return render_to_response('templates/coming_soon.html', {}, request=req)


def welcome(req):
    return render_to_response('templates/welcome.html', {}, request=req)


def about(req):
    return render_to_response('templates/coming_soon.html', {}, request=req)


def cv(req):
    subreq = Request.blank('/personal')
    personal = req.invoke_subrequest(subreq).json_body

    subreq = Request.blank('/education')
    education = req.invoke_subrequest(subreq).json_body

    subreq = Request.blank('/project')
    project = req.invoke_subrequest(subreq).json_body

    records = {**{**personal, **education}, **project}

    records['name'] = str(records['first_name']) + " " + str(records['last_name'])
    records.pop("first_name")
    records.pop("last_name")

    return render_to_response('templates/cv.html', records, request=req)


def avatar(req):
    avatar_response = {"image_src": "images/chiken.jpg"}
    response = Response(body=json.dumps(avatar_response))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response


def personal(req):
    keys = ("first_name", "last_name", "email")

    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    cursor.execute("select first_name, last_name, email from Users where id=1")
    records = cursor.fetchall()[0]
    db.commit()
    db.close()

    records = dict(zip(keys, records))
    response = Response(body=json.dumps(records))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response


def education(req):
    keys = ("school", "degree", "major", "date")

    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    cursor.execute("select school, degree, major, date from Educations where id=1")
    records = cursor.fetchall()[0]
    db.commit()
    db.close()

    records = dict(zip(keys, records))
    response = Response(body=json.dumps(records))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response


def project(req):
    keys = ["title", "description", "link", "Image_src", "teamID"]

    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    cursor.execute("select title, description, link, Image_src, teamID from Projects where id=1")
    records = cursor.fetchall()[0]
    db.commit()
    cursor.execute("select url from Teammates where teamID={0}".format(records[4]))
    teammates = cursor.fetchall()
    db.commit()
    db.close()

    records = dict(zip(keys, records))
    teammates = ["".join(tup) for tup in teammates]
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
        db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
        values = ", ".join([f'"{a}"' for a in new_user.values()])
        cursor = db.cursor()
        cursor.execute("insert into Users (first_name, last_name, email, comment) values (" + values + ")")
        db.commit()
        db.close()

        return exc.HTTPCreated()
    else:
        return exc.HTTPBadRequest()


def get_users(req):
    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    cursor.execute("select first_name, last_name, email, comment from Users where id!=1")
    records = cursor.fetchall()
    db.commit()
    db.close()

    response = Response(body=json.dumps(records))
    response.headers.update({'Access-Control-Allow-Origin': '*', })

    return response

''' Route Configurations '''
if __name__ == '__main__':
    config = Configurator()

    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('get_home', '/')
    config.add_view(get_home, route_name='get_home')

    config.add_route("welcome", "/welcome")
    config.add_view(welcome, route_name="welcome")

    config.add_route("about", "/about")
    config.add_view(about, route_name="about")

    config.add_route("cv", "/cv")
    config.add_view(cv, route_name="cv")

    config.add_route("avatar", "/avatar")
    config.add_view(avatar, route_name="avatar", renderer='json')

    config.add_route('personal', '/personal')
    config.add_view(personal, route_name='personal', renderer='json')

    config.add_route('education', '/education')
    config.add_view(education, route_name='education', renderer='json')

    config.add_route('project', '/project')
    config.add_view(project, route_name='project', renderer='json')

    config.add_route('add_user', '/add_user')
    config.add_view(add_user, route_name='add_user', renderer='json', request_method='POST')

    config.add_route('get_users', '/get_users')
    config.add_view(get_users, route_name='get_users', renderer='json', request_method='GET')

    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    app = config.make_wsgi_app()
    bjoern.run(app, "0.0.0.0", 6000)
