# -*- coding: utf-8 -*-

from flask import render_template

from core import app



@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404
