from diny import *

tab_x = tabPanel([
    Control(Input(id='x1', type='number', value=1), label='X1'),
    Control(Dropdown(id='x2', options=[
        {'label':2, 'value':2},
        {'label':3, 'value':3},
        {'label':4, 'value':4},
    ], value=2), label='X2'),
    Control(Slider(id='x3', min=0, max=5, value=3, step=1), label='X3')
], title='X values')

tab_y = tabPanel([
    Control(Input(id='y1', type='number', value=1), label='Y1'),
    Control(Input(id='y2', type='number', value=2), label='Y2'),
    Control(Input(id='y3', type='number', value=3), label='Y3')
], title='Y values')

ui = fluidPage([
    sidebarLayout(
        sidebarPanel(tabsetPanel([tab_x, tab_y])),
        mainPanel([Graph(id='myChart')])
    )
])

def server():
    @reactive('myChart.figure', ['x1.value', 'y1.value', 'x2.value', 'y2.value', 'x3.value', 'y3.value'])
    def handle_change(x1, y1, x2, y2, x3, y3):
        print(x1, type(x1))
        return {'data':
            [{
                'x':[x1, x2, x3],
                'y':[y1, y2, y3]
            }]
        }

dashApp(ui = ui, server = server, debug = True)