# coding:utf-8 
"""
Created on 2016/04/25
Author: shylock
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('index.html',
                           form=form, name=session.get("name"),
                           current_time=datetime.utcnow())
