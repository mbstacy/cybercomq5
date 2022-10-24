from celery import Celery
import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)

#Example task
@app.task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result
    
@app.task()
def subtract(x, y):
    """ Example task that subtract two numbers
        args: x and y
        return subtraction
    """
    result = x - y
    return result


@app.task()
def hello(name):
    """ Example say Hello
 
    """
    result = "Hello {0}".format(name)
    return result