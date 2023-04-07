from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

# @app.route('/hello')
# @app.route('/hello/')
# @app.route('/hello/<string:name>')
# def hello(name='World'):
#   return render_template('header.html.j2', name=name)

# @app.route('/sitemap')
# def sitemap():
#     urls={
#         'index' : url_for('index'),
#         'hello' : url_for('hello'),
#         'hello(Pierre)' : url_for('hello', name='Pierre')
#     }
#     return render_template('sitemap.html.j2', urls=urls)

# @app.route('/index')
# def index():
#   return render_template('index.html.j2')

# @app.errorhandler(404)
# def not_found(error):
#    return render_template('error.html.j2', code=404), 404