import pandas as pd

def load_data(path="../datasets/rent_apartments.csv") -> pd.DataFrame:    
    # Load data from a CSV file into a DataFrame
    df = pd.read_csv(path)
    return df

#df = load_data()
#print(df.sample(20))