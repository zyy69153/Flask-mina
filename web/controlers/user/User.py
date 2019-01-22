#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 19:56

from flask import Blueprint,render_template

route_user = Blueprint( 'user_page',__name__ )

@route_user.route( "/login/" )
def login():
    return render_template( "user/login.html" )

@route_user.route( "/edit/" )
def edit():
    return render_template( "user/edit.html" )

@route_user.route( "/reset-pwd/" )
def resetPwd():
    return render_template( "user/reset_pwd.html" )