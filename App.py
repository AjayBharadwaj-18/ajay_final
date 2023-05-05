import streamlit as st 
import pickle 
import datetime 
import pandas as pd

def extract_week(df): 
    Date='Date' 
    df[Date] = pd.to_datetime(df[Date], infer_datetime_format=True) 
    df['week'] = pd.DatetimeIndex(df[Date]).week 
    df['month'] = pd.DatetimeIndex(df[Date]).month 
    df['year'] = pd.DatetimeIndex(df[Date]).year
    
    return df
def maping_type(df):
    df['Type'] = df['Type'].map({'A':'1','B':'2','C':'3'})
    
    return df


def convert_to_int(df):
    df['Type']=df['Type'].astype(int)
    df['IsHoliday']=df['IsHoliday'].astype(int)
    return df

def input_col_sel(df): 
    input_col = ['Store', 'IsHoliday', 'Type', 'Size', 'week','Dept','year']
    return df[input_col]

pipe = pickle.load(open('pipe.pkl','rb')) 
df = pickle.load(open('train.pkl','rb'))

st.title("Product demand Forecasting")

store = st.selectbox('Store',df['Store'].unique())
Dept = st.selectbox('Dept',df['Dept'].unique())
Date =st.date_input( "When to predict", datetime.date(2011,11,11), datetime.date(2010,2,5), datetime.date(2012,10,26) )
IsHoliday = st.selectbox('IsHoliday',[True,False])
Type = st.selectbox('Type',["A","B","C"])

Size = st.number_input("Size" )

if st.button("Predict Sales Amount"): 
    query = pd.DataFrame({"Store":store,'Dept':Dept,'Date':Date,'IsHoliday':IsHoliday,'Type':Type,'Size':Size}, index=[0]) 
    st.title(pipe.predict(query))
    











