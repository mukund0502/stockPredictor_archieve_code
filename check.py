import pickle
from darts import TimeSeries
from darts.utils.timeseries_generation import gaussian_timeseries, linear_timeseries, sine_timeseries
from darts.models import RNNModel, TCNModel, TransformerModel, NBEATSModel, BlockRNNModel
from darts.metrics import mape, smape
import matplotlib.pyplot as plt 
from darts.datasets import AirPassengersDataset, MonthlyMilkDataset

series_air = AirPassengersDataset().load()
series_milk = MonthlyMilkDataset().load()


from darts.dataprocessing.transformers import Scaler
scaler_air, scaler_milk = Scaler(), Scaler()
series_air_scaled = scaler_air.fit_transform(series_air)
series_milk_scaled = scaler_milk.fit_transform(series_milk)



print(2)
print(pickle.load(open('krish_model.pkl', 'rb')))
print(1)
print(type(modelbykrish))


pred = modelbykrish.predict(n=36, series=series_air_scaled)

series_air_scaled.plot(label='actual')
pred.plot(label='forecast')
plt.legend()