#%%

import requests, json, pandas as pd
from bs4 import BeautifulSoup

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

    a = get_json_from_url(link)
    print(a)
    a_ = prepare (a)



    df = pd.json_normalize(a_)[[ 'price',
    'administration.price',
    'age.id',
    'age.name',
    'area',
    'baths.id',
    'baths.name',
    'client.type',
    'condition.id',
    'floor.id',
    'garages.id',
    'locations.lat',
    'locations.lng',
    'rooms.name',
    'segmentation.baños',
    'segmentation.habitaciones',
    'segmentation.tipo_cliente',
    'stratum.id']]

    test = df
    test['stratum.id'] = test['stratum.id'].replace(100,1)
    test['client.type'] = test['client.type'].replace('BUILDER','BROKER')
    test = test[test['segmentation.habitaciones'] != 'Sin especificar']
    test = test[test['age.name'] != 'Sin especificar']
    test = test[test['baths.name'] != 'Sin especificar']
    test = test[test['rooms.name'] != 'Sin especificar']
    test = test[test['segmentation.baños'] != 'Sin especificar']
    test = test[test['segmentation.habitaciones'] != 'UNDEFINED']

    return test

# %%
