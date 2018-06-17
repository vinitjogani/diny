from typing import List
from dash.dependencies import Input, Output

def set_env(app):

    def reactive(output: str, inputs: List[str]):
        """
        Decorator function for assigning callbacks for user input, which can be
        used to update the outputs.
        
        Outputs are of the form "<output id>.<parameter name>". Therefore, to update
        the figure of an output graph with the id "myChart", the proper format to 
        provide is "myChart.figure".

        Likewise, inputs are of the form "<input id>.<parameter name>". Therefore, to
        listen for changes in the value of a slider input with id "mySlider", the proper
        format to provide is "mySlider.value".
        """
        def wrapper(func):
            i = []
            if not "." in output:
                raise ImproperFormatException()
            parts = output.split(".")
            o = Output(parts[0], parts[1])
            for inp in inputs:
                if not "." in inp:
                    raise ImproperFormatException()
                parts = inp.split(".")
                i.append(Input(parts[0], parts[1]))
            return app.callback(o, i)(func)

        return wrapper
    
    return reactive

class ImproperFormatException(Exception):
    """
    This exception is thrown when the provided string for an input or output
    for the reactive decorator is in an improper format. Read documentation above
    for proper format.
    """
    def __init__(self):
        super("The format for the string is not proper.")