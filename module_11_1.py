import requests



Streaming Uploads
Requests supports streaming uploads, which allow you to send large streams or files without reading them into memory.
To stream and upload, simply provide a file-like object for your body:

with open('massive-body', 'rb') as f:
    requests.post('http://some.url/streamed', data=f)


Session Objects
The Session object allows you to persist certain parameters across requests. It also persists cookies across all
requests made from the Session instance, and will use urllib3’s connection pooling. So if you’re making several requests
to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase
(see HTTP persistent connection).

A Session object has all the methods of the main Requests API.

Let’s persist some cookies across requests:

s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

Prepared Requests
Whenever you receive a Response object from an API call or a Session call, the request attribute is actually the PreparedRequest that was used. In some cases you may wish to do some extra work to the body or headers (or anything else really) before sending a request. The simple recipe for this is the following:

from requests import Request, Session

s = Session()

req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)