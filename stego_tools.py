from math import cos, pi
def execute(image, data, code, args):
    context = { 'img' : image, 'data' : data, 'args' : args}
    exec(code, {}, context)
    return context['output']
