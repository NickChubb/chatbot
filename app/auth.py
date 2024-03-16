from hashlib import sha256
import os
from werkzeug.wrappers import Request, Response

class auth_middleware():
    def __init__(self, app):
        self.app = app
        # Get api secret from os or from docker secrets dir
        API_SECRET = os.environ.get("API_SECRET")
        if API_SECRET is None:
            secret_file_path = '/run/secrets/API_SECRET'
            if os.path.isfile(secret_file_path):
                with open(secret_file_path, 'r') as secret_file:
                    API_SECRET = secret_file.read().strip()
        # hash secret
        self.secret = sha256(API_SECRET.encode('utf-8')).hexdigest()

    def __call__(self, environ, start_response):
        request = Request(environ)
        secret = request.args.get('secret')
        
        # verify the secrets match
        if secret == self.secret:
            return self.app(environ, start_response)

        res = Response(u'Authorization failed.', mimetype= 'text/plain', status=401)
        return res(environ, start_response)