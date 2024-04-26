import numpy as np
import ruptures as rp
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('resources/WTemp_C1_Avg.csv', header=0)
data = ds.WTemp_C1_Avg.values

# Algoritmo Pelt
pelt = rp.Pelt(model="l2").fit(data)
bkps_pelt = pelt.predict(pen=5)

# Algoritmo BinarySeg
algo = rp.Binseg(model="l2").fit(data)
bkps_binSeg = algo.predict(pen=3)

# Algoritmo Dynp
algo = rp.Dynp(model="l2").fit(data)
bkps_dynp = algo.predict(n_bkps=10)

# Visualizzazione dei risultati per Pelt
rp.display(data, bkps_pelt)
plt.title("WTemp Pelt")
plt.show()

# Visualizzazione dei risultati per BinarySeg
rp.display(data, bkps_binSeg)
plt.title("WTemp BinarySeg")
plt.show()

# Visualizzazione dei risultati per Dynp
rp.display(data, bkps_dynp)
plt.title("WTemp Dynp")
plt.show()