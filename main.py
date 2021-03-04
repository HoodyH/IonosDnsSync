import json
from urllib import request

ENDPOINT = 'https://api.hosting.ionos.com/dns/v1/zones'
MY_IP_API_ENDPOINT = 'https://api.my-ip.io/ip.json'


def get_my_ip() -> str:
    url = request.urlopen(MY_IP_API_ENDPOINT)
    json_data = json.loads(url.read().decode())

    if json_data.get('success'):
        return json_data.get('ip')

    raise Exception('Failed to get IP')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_my_ip()
