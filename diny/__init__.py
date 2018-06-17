import dash

from .layouts import *
from .inputs import *
from .reactivity import set_env

app = dash.Dash(static_folder='static')
reactive = set_env(app)

def add_css(filename):
    app.css.append_css({"external_url":"/static/" + filename})

def add_js(filename):
    app.scripts.append_script({"external_url":"/static/" + filename})

def dashApp(ui, server, **kwargs):
    """
    Supply the UI and Server components of the Diny app to this function as you would
    for a Shiny app. Set debug=True for enabling debug mode in Dash.
    """
    # Intialize app
    app.layout = ui
    server()
    # Add bootstrap
    app.css.append_css({"external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"})
    app.css.append_css({"external_url": "/static/diny.css"})
    app.scripts.append_script({"external_url": "https://code.jquery.com/jquery-3.3.1.slim.min.js"})
    app.scripts.append_script({"external_url": "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"})
    app.scripts.append_script({"external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"})
    # Run app
    app.run_server(**kwargs)