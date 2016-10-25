from urllib.request import Request, urlopen

try:
    import urllib.request as requests
except EnvironmentError:
    import urllib2 as requests

class RequestData:
    statusCode = 0
    response = ""

class NetworkManager:
    def get(url, params = None, headers = None):
        response = requests.urlopen(url).read()
        return response

    def post(url, params = None, headers = None):
        pass

    res = get("http://www.google.co.il", None)
    print(res)