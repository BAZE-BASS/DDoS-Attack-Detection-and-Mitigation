import pandas as pd
import numpy as np

num_rows = 1000

data = {
    "Duration": np.random.uniform(0.1, 10.0, num_rows), 
    "Bytes": np.random.randint(100, 1000, num_rows),  
    "Packets": np.random.randint(1, 50, num_rows),  
    "SrcPort": np.random.randint(1024, 65535, num_rows),  
    "DstPort": np.random.choice([80, 443, 22, 3389], num_rows),  
    "SrcBytes": np.random.randint(50, 500, num_rows),  
    "DstBytes": np.random.randint(50, 500, num_rows),  
    "Label": np.random.choice([0, 1], num_rows)  # 0 = normal, 1 = suspicious
}

df = pd.DataFrame(data)
df.to_csv("FlowStatsfile.csv", index=False)
print("FlowStatsfile.csv created with simulated data.")
