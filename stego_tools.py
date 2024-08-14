from math import cos, pi
def execute(image, data, code, args):
    context = { 'image' : image, 'data' : data, 'args' : args, 'output' : None }
    exec(code, context)
    return context['output']
