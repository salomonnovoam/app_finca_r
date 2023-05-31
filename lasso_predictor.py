
#%%

from joblib import load
from finca_raiz_get_house_info_from_link import get_processed_info

#%%
class PredictionModel:

    def __init__(self):
        self.model = load("lasso_v1.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result

def executor_lasso (link):
    predicion_model = PredictionModel()
    df_to_predict = get_processed_info(link)
    results = predicion_model.make_predictions(df_to_predict)
    return results[0]    


# %%
