# -*- coding: utf-8 -*-

from core import app
from core import db
from flask import g
from flask.ext.login import current_user

from fapp.views.errorhandler import *



@app.before_request
def before_request():
    # Do something before request.
    t = db.session.registry().transaction
    if t and t._rollback_exception is not None:
        db.session.rollback()
    g.user = current_user


@app.teardown_request
def teardown_request(exception):
    t = db.session.registry().transaction
    if t and t._rollback_exception is not None:
        db.session.rollback()



