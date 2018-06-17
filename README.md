# Diny: Shiny for Python using Dash

Use the ease and convenience of R Shiny in Python to get the best of both worlds. I have tried to get a syntax that looks and feels more like Shiny because I've found it's much more concise than traditional Dash syntax. 

    dashApp(ui = ui, server = server)

To get started, install all the dependencies:

    pip install dash dash_core_components dash_html_components plotly

Open example.py to see a running example of a simple reactive application using Diny. It makes use of some convenient Shiny components like Tabset Panel, Sidebar Layout, etc. Add any static files to the static folder, and then add it to your app using add_css or add_js.

Any useful contributions are welcome!
