# Diny: Shiny for Python using Dash

Use the ease and convenience of R Shiny in Python to get the best of both worlds. I have tried to get a syntax that looks and feels more like Shiny because I've found it's much more concise than traditional Dash syntax. 

    dashApp(ui = ui, server = server)

To get started, install all the dependencies:

    pip install dash dash_core_components dash_html_components plotly

Open example.py to see a running example of a simple reactive application using Diny. It makes use of some convenient Shiny components like Tabset Panel, Sidebar Layout, etc. Add any static files to the static folder, and then add it to your app using add_css or add_js.

To see different input and output controls, see [Dash Core Components](https://dash.plot.ly/dash-core-components). Add these components directly like:
    
    Graph(id='myChart')
    
Wrap the built-in inputs in a Control component to add a nicely spaced label like so:

    Control(Input(id='myTextInput', type='text'), label='Enter some text:)

You can also include HTML components easily like:

    html.Br() #Notice that first letter for HTML tags is capital

Any useful contributions are welcome!
