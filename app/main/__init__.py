# coding:utf-8 
"""
Created on 2016/04/25
Author: shylock
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
