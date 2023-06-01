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


    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, session_id, password, port))
    proxy_handler = {
        'http': super_proxy_url,
        'https': super_proxy_url,
    } 
    return proxy_handler

def get_json_from_url(link):

    try:
        headers = {

            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        response = requests.get( link,
            headers=headers, proxies = get_proxy_dc()
                             
        )

        soup = BeautifulSoup(response.text, 'lxml')
        soup

        discovery = soup.find('script', {'id':'__NEXT_DATA__'}).text
        print(link)
        return json.loads(discovery)['props']['pageProps']
    except Exception as e:
        print(e)
        print('-----error----')
        print(link)
# %%


def prepare (i):
    try:
        cat_sec = i['categories']['sector']
        # print(cat_sec)
        for j in cat_sec:
            value = j['slug']
            print(value)
            i[value]=1
    except:
        print('a')
        pass

    try:
        cat_int = i['categories']['interior']
        # print(cat_int)
        for j in cat_int:
            value = j['slug']
            print(value)
            i[value]=1
    except:
        print('b')
        pass
        
    try:
        cat_ext = i['categories']['exterior']
        # print(cat_ext)
        for j in cat_ext:
            value = j['slug']
            print(value)
            i[value]=1
    except:
        print('c')
        pass

    return i


def get_processed_info(link):
    print(link)

    a = get_json_from_url(link)
    print(a)
    a_ = prepare (a)



    #df = pd.json_normalize(a_)[[ 'price',
    #'administration.price',
    #'age.id',
    #'age.name',
    #'area',
    #'baths.id',
    #'baths.name',
    #'client.type',
    #'condition.id',
    #'floor.id',
    #'garages.id',
    #'locations.lat',
    #'locations.lng',
    #'rooms.name',
    #'segmentation.baños',
    #'segmentation.habitaciones',
    #'segmentation.tipo_cliente',
    #'stratum.id']]
#
    #test = df
    #test['stratum.id'] = test['stratum.id'].replace(100,1)
    #test['client.type'] = test['client.type'].replace('BUILDER','BROKER')
    #test = test[test['segmentation.habitaciones'] != 'Sin especificar']
    #test = test[test['age.name'] != 'Sin especificar']
    #test = test[test['baths.name'] != 'Sin especificar']
    #test = test[test['rooms.name'] != 'Sin especificar']
    #test = test[test['segmentation.baños'] != 'Sin especificar']
    #test = test[test['segmentation.habitaciones'] != 'UNDEFINED']

    return str(a)

# %%
