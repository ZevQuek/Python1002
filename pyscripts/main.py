import pandas as pd
import sys

def test():
    covid_df = pd.read_csv("covid19.csv") #reads the csv into python pandas
    cv_dataset2 = covid_df[["Date","Daily Confirmed", "Cumulative Discharged", "Still Hospitalised", "In Isolation MOH report", "Cumulative Deaths"]] #use only these columns
    cv_droprows = covid_df.drop(covid_df.index[1:5]) #drop rows or [1,2,3,4]
    #print(covid_df.head(10)) #debug printing first 10 lines
    #print(cv_dataset2.head(5))
    #print(cv_droprows.head(10))

    dfT = cv_dataset2.T
    output = dfT.to_json()
    print(output)
    sys.stdout.flush()

test()
