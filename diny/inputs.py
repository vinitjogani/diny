import dash_html_components as html
from dash_core_components import *

"""
More widgets will be added here in the future to give more functionality
of Shiny inputs.
"""

def Control(widget, label=''):
    return html.Div([
        html.B(label),
        html.Br(),
        widget
    ], className='form-group')