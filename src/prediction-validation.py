# Importing Pandas library
import pandas as pd
import numpy as np

# Making Dataframes for the prediction, actual
actual_price = pd.read_csv('./input/actual.txt', sep='|', header=None)
predicted_price = pd.read_csv('./input/predicted.txt', sep='|', header=None)

# storing window value in integer
window = open('./input/window.txt','r')
window = int(window.read())

length_actual = len(actual_price)
last_hour = predicted_price.iloc[- 1, 0]

# Function takes dictionary and predicted dataframe as input and calculates error between the predicted 
# and actual and return error
def error_by_hour(dictionary, predicted):
    error = predicted.apply(lambda x: abs(dictionary[x[1]]-x[2]), axis=1)
    return error

# Dictionary to store key, value pairs for the stock data
start_hour = 1
stock_dictionary= {} # Currently empty
dataframe = pd.DataFrame({'Hr':[] ,'Error':[]}) # Final dataframe to store all error by hour for each stock

# loop through the actual length of the file. Actual file contains all the stock names.
# If predicted price is no present for a particular stock name then we set the hour to null else we calculate the difference 
# of actual and predicted price.
for i in range(0, length_actual):
    if actual_price.loc[i,0] != start_hour:
        if predicted_price[predicted_price[0] == start_hour].empty:
            error_append_df = pd.DataFrame({'Hr':[start_hour],'Error': [np.nan]}) # setting to NaN of Numpy
        else:
            error = error_by_hour(stock_dictionary, predicted_price[predicted_price[0] == start_hour])
            error_append_df = pd.DataFrame({'Hr':[start_hour]*len(predicted_price[predicted_price[0] == start_hour]),'Error':error})
        dataframe = pd.concat([dataframe,error_append_df]) # adding the error data frame each time 
        start_hour = actual_price.loc[i, 0]
        stock_dictionary = {}    # clearing the dictionary very time for a new hour
    stock_dictionary[actual_price.loc[i,1]] = actual_price.loc[i,2]
if predicted_price[predicted_price[0] == start_hour].empty:
    error_append_df = pd.DataFrame({'Hr':[start_hour],'Error': [np.nan]})
else:
    error = error_by_hour(stock_dictionary, predicted_price[predicted_price[0] == start_hour])
    error_append_df = pd.DataFrame({'Hr':[start_hour]*len(predicted_price[predicted_price[0] == start_hour]),'Error':error})
dataframe = pd.concat([dataframe,error_append_df])
start_hour = actual_price.loc[i, 0]
stock_dictionary = {}


flag = 0
# Writing comparison.txt file
file = open("./output/comparison.txt","w")
for i in range(1, last_hour - (window)+2):
    flag = 0
    for value in dataframe[(dataframe['Hr']>=i) & (dataframe['Hr'] <=(i+window-1))]['Error'].isnull():
        if value == False:
            error_by_window = round(dataframe[(dataframe['Hr']>=i) & (dataframe['Hr'] <=(i+window-1))]['Error'].mean(), 2)
            file.write("" + str(i) + "|" + str(i+window-1) + "|" + str(error_by_window) + "\n")
            flag = 1
            break
    if flag == 0:
        error_by_window = 'NA'
        file.write("" + str(i) + "|" + str(i+window-1) + "|" + str(error_by_window) + "\n")
file.close()
