#%%

# import pandas as pd
# from PIL import Image
# import json

import streamlit as st
import os

# from lasso_predictor import executor_lasso
from joblib import load
print('importa')
from finca_raiz_get_house_info_from_link import get_processed_info
print('importado')
#%%

# image_r = Image.open('Iceberg-Data-Final-Logo.png')
# st.image(image_r, width=300)



#%%
class PredictionModel:
    

    def __init__(self):
        # address = os.getcwd()+
        self.model = load(os.getcwd()+"/lasso_v1.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
    
def executor_lasso (link):
    predicion_model = PredictionModel()
    df_to_predict = get_processed_info(link)
    results = predicion_model.make_predictions(df_to_predict)
    return results[0]# + ' ' + df_to_predict.price.values[0]


#%%

st.header("Herramienta para identificar oportunidades de negocio en Bogotá")
st.markdown(''' Data Finca Raíz''')
# tab1, tab2, tab3 = st.tabs(["Lasso","Model 2","Model 3"])
tab1, tab2, tab3 = st.tabs(["Herramienta",".","."])


with tab1:
    # image2 = Image.open('image.png')
    # st.image(image2, width=75)
    st.header("¿Cuánto debería costar una propiedad, dadas sus características?")
    # col1, col2 = st.columns(2)

    st.write('')
    st.write('')
    st.write('')
    search_r = st.text_input('Link propiedad', '').strip()
    st.write('')
    st.write('')
    st.write('')
    # df_to_predict = get_processed_info(link)


    if st.button('Recolectar datos'):
        with st.spinner('Recolectando datos...'):
            data_r = executor_lasso(search_r)
            df_to_predict = executor_lasso(search_r)
#            st.dataframe(df_to_predict.drop(['price'],axis=1)) 
            st.write('El precio de la propiedad debería ser', df_to_predict) 
