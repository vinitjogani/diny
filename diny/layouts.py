import dash_html_components as html

"""
These are composite HTML elements to make use of Bootstrap components and 
give the look and feel of a Shiny app.
"""

def fluidPage(children=[]):
    return html.Div(children, className='container-fluid')

def sidebarLayout(sidebar, main):
    return html.Div([
        sidebar, main
    ], className='row')

def sidebarPanel(children=[]):
    return html.Div([
        html.Form(children, className='well')
    ], className='col-sm-4')

def mainPanel(children=[]):
    return html.Div(children, className='col-sm-8')

def tabsetPanel(children=[]):
    tabs = []
    pages = []
    i = 0
    for child in children:
        active = '' if i != 0 else ' show active'
        selected = 'true' if i == 0 else 'false'

        tabs.append(
            html.Li([
                html.A(
                    child['title'], 
                    className='nav-link' + active, 
                    id='link-tab' + str(i), 
                    href='#tab' + str(i), 
                    role='tab', 
                    **{
                        'data-toggle':'tab',
                        'aria-controls':child['title'], 
                        'aria-selected':selected
                    }
                )
            ])
        )

        pages.append(
            html.Div(
                child['children'], 
                id='tab' + str(i),
                className='tab-pane fade ' + active, 
                role='tabpanel', 
                **{
                    'aria-labelledby':'link-tab' + str(i)
                }
            )
        )

        i += 1

    return html.Div([
        html.Ul(tabs, className='nav nav-tabs', role='tablist'),
        html.Div(pages, className='tab-content')
    ])

def tabPanel(children, title=''):
    return {
        'title': title,
        'children': children
    }

def inputWidget(widget, label=''):
    return html.Div([
        html.B(label),
        html.Br(),
        widget
    ], className='form-group')