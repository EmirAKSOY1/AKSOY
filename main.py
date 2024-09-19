import requests

def konum_getir(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    if response.status_code == 200:
        return response.json()
    else:
        return None
