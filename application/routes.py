"""Core Flask app routes."""
from flask import render_template
from flask import current_app as app


@app.route('/')
def home():
    """Landing page."""
    return render_template('index.jinja2',
                           title='Python for data Analisys Proyect',
                           template='home-template',
                           body="Dash and plotly with Flask")
