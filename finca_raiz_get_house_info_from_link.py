#%%

import requests, json, pandas as pd, random
from bs4 import BeautifulSoup

#%%

def get_proxy_dc()-> dict:
    """
    It returns a dictionary with the keys 'http' and 'https' and the values are the proxy address to use the datacenter proxy
    :return: A dictionary with the keys 'http' and 'https' and the values are the entry variable.
    """


    username = 'brd-customer-hl_435d7aea-zone-data_center-country-in'
    password = '8dletu9t4a7u'

    username =  'brd-customer-hl_435d7aea-zone-residential-country-in'
    password = 'evb8oehm4sza'



    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, session_id, password, port))
    proxy_handler = {
        'http': super_proxy_url,
        'https': super_proxy_url,
    } 
    return proxy_handler

#%%
def get_json_from_url(link):

    try:
        headers = {

            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        response = requests.get( link,
            headers=headers,
            proxies = get_proxy_dc()
        )

        return response.status_code#response.status_code#json.loads(discovery)['props']['pageProps']
    except Exception as e:
        print(e)
        print('-----error----')
        print(link)
# %%
