#def app(env, start_response):
  #status = '200 OK'
  #headers = [('Content-Type', 'text/plain')]
  #body = env['QUERY_STRING'].replace('&', '\n')
  #start_response(status, headers)
 # return [body]
def app(environ, start_response):
    """Simplest possible application object"""
    data = '\n'.join(environ['QUERY_STRING'].split('&'))
    #data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
