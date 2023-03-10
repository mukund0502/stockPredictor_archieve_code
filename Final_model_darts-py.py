import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from darts import TimeSeries
from darts.models import NBEATSModel
from darts import datasets


from darts.metrics import mape, smape, mae
from darts.dataprocessing.transformers import Scaler
import nsepy
from datetime import date

nifty100list = pd.read_csv('ind_nifty100list.csv')['Symbol']
nifty100list = np.array(nifty100list)

dictClose = {}
for i in nifty100list:
    df = pd.DataFrame(nsepy.get_history(symbol = nifty100list[0], start = date(2020, 10, 1), end = date.today() ))['Close']
    df = np.array(df)
    df = TimeSeries.from_values(df, columns=None, fillna_value=None, static_covariates=None, hierarchy=None)
    dictClose[i] = df

totallist = []
scalerdict = {}
for i in dictClose:
    datascaler = Scaler()
    dictClose[i] = datascaler.fit_transform(dictClose[i])
    scalerdict[i] = datascaler
    totallist.append(dictClose[i])

finalmodel = NBEATSModel(input_chunk_length = 150, output_chunk_length = 30, n_epochs = 200, random_state = 0)

finalmodel.fit(totallist, verbose=True)

# can we train model by different name and predict by different name ???
#"YES"
# from now save model by model.save in darts in pt format 
# and load model by 

finalmodel.save('final_model.pt')
