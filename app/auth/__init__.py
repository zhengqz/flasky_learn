# coding:utf-8 
"""
Created on 2016/04/26
Author: shylock
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views