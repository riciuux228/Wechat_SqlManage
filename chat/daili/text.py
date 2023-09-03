from urllib import request
from urllib.parse import urlparse
from urllib.request import Request

from flask import Response



async def fetch(request, env):
    return await handle_request(request)

async def handle_request(request):
    # Define the target server's address
    url = urlparse(request.url)
    target_url = 'https://api.openai.com'

    # Construct a new request object
    proxy_request = Request(target_url + url.path + url.query, method=request.method, headers=request.headers, body=request.body)

    # Send the request to the target server
    response = await fetch(proxy_request)

    # Construct a new response object
    proxy_response = Response(response.body, status=response.status, status_text=response.status_text, headers=response.headers)

    # Return the response to the client
    return proxy_response




