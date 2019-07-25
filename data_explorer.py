# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:49:13 2019

@author: EduCM
"""
import pandas as pd
import matplotlib.pyplot as plt

def quality_report(data):

    """This method will do a basic data quality report for a data frame"""
        
    if (type(data) != pd.core.frame.DataFrame):
        raise TypeError("Data must be pandas.core.frame.DataFrame")
    else: 
        columns = list(data.columns.values)
        data_type = pd.DataFrame(data.dtypes, columns=['Data type'])
        missing_data = pd.DataFrame(
        data.isnull().sum(), columns=['missing values'])
        present_data = pd.DataFrame(data.count(), columns=['present values'])
        unique_values = pd.DataFrame(columns=['unique values'])
        minimum_values = pd.DataFrame(columns=['minimum values'])
        max_values = pd.DataFrame(columns=['maximun values'])
        
        for i in columns:
            unique_values.loc[i] = [data[i].nunique()]
            try:
                minimum_values.loc[i] = [data[i].min()]
                max_values.loc[i] = [data[i].max()]
            except:
                pass
        
        DQ_report = data_type.join(missing_data).join(present_data).join(
        unique_values).join(minimum_values).join(max_values)
    
    return DQ_report

def get_histogram(data,column,bins):
    
    """This method will return a matplotlib.pyplot object Histogram from a passed
    column of a pandas Dataframe"""
    
        
    if (type(data) != pd.core.frame.DataFrame):
        raise TypeError("Data must be pandas.core.frame.DataFrame")
    
    elif (type(column) != str):
        raise TypeError("Column must be srt type")
    
    elif (data[column].dtype != int and data[column].dtype != float):
        raise TypeError("dtype of the column must be numeric type")
        
    else:
        d_limit,u_limit= min(data[column]),max(data[column])
        plt.hist(data[column],bins=bins,facecolor='blue',range=[d_limit, u_limit])
        plt.title('Histogram of column:' + column)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        return plt

def get_correlation_plot(data,columns_index,plot_size):
    """this method will return a matplotlib.pyplot object with the correlation for the columns_index list of
    a pandas DataFrame"""
        
    if (type(data) !=pd.core.frame.DataFrame):
        raise TypeError("Data must be pandas.core.frame.DataFrame")
    
    elif( type(columns_index) != list):
        raise iipeError("columns_index must be a list")
    
    elif(all(isinstance(n, int) for n in columns_index) == False):
        raise TypeError("elements of columns_index must be int type")
    
    elif( type(plot_size) != int):
        raise TypeError("plot_size must be a int")
    
    elif( plot_size <= 0 ):
        raise ValueError("plot_size must be greater than 0")
    
    else: 
        corr = data.iloc[:,columns_index].corr()
        fig,ax = plt.subplots(figsize=(plot_size, plot_size))
        ax.matshow(corr)
        plt.xticks(range(len(corr.columns)), corr.columns,fontsize=20)
        plt.yticks(range(len(corr.columns)), corr.columns,fontsize=20)
        return plt
