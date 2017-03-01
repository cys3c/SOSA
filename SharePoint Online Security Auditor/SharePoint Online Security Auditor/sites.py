import json

from client.office365.runtime.auth.authentication_context import AuthenticationContext
from client.office365.runtime.client_request import ClientRequest
from client.office365.runtime.utilities.request_options import RequestOptions

def list_sites(username, password):
    ctx_auth = AuthenticationContext(url)
    if ctx_auth.acquire_token_for_user(username, password):
      request = ClientRequest(ctx_auth)
      options = RequestOptions("{0}/_api/web/".format(url))
      options.set_header('Accept', 'application/json')
      options.set_header('Content-Type', 'application/json')
      data = request.execute_query_direct(options)
      s = json.loads(data.content)
      web_title = s['Title']
      return "Web title: " + web_title
    else:
      return ctx_auth.get_last_error()