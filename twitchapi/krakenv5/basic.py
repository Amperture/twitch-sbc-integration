import requests
import pprint

requests.packages.urllib3.disable_warnings()


def endpoint_get(endpoint, client_id, **kwargs):
    url = "https://api.twitch.tv/kraken/" + endpoint
    headers = {
            'Client-ID' : client_id 
            }

    if 'endpoint_args' in kwargs:
        for arg in kwargs['endpoint_args']:
            url += '/' + arg

    if 'header' in kwargs:
        headers = kwargs['header']

    r = requests.get(url, headers=headers)

    return r.json()

def endpoint_put(endpoint, client_id, **kwargs):
    url = "https://api.twitch.tv/kraken/" + endpoint
    # Not sure if empty dicts vs. Null objects will create problems in future
    # TODO keep the above in mind
    headers = {}
    data = {}
    
    if 'endpoint_args' in kwargs:
        for arg in kwargs['endpoint_args']:
            url += '/' + arg

    if 'data' in kwargs:
        data = kwargs['data']

    if 'header' in kwargs:
        headers = kwargs['header']

    headers['Client-ID'] = client_id
    r = requests.put(url, headers=headers, data=data)
    print r.reason

    return r.json()



if __name__ == "__main__":
    with open('LaunchpadBot_ClientID', 'r') as f:
        client_id = f.read().strip()

    args = ['amperture']

    pprint.pprint(endpoint_get('channels', client_id, endpoint_args = args))
