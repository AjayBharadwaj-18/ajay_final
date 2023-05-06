import streamlit as st 
import pickle 
import datetime 
import pandas as pd
from PIL import Image

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

st.title("Product demand Prediction")
st.sidebar.header('Demand data')
row1_c1, row2_c2 = st.columns([2,1])
img_file = "1.png"
##c1.image(Image.open(img_file))
with row1_c1:
    st.image(img_file, width= 800)

st.write("Product demand forecasting is the process of estimating the future demand for a particular product or service. It is a critical business function that helps organizations make informed decisions related to production planning, inventory management, and pricing strategies.")
st.write("Demand forecasting can be done at different levels, such as at the individual product level, at the category level, or for the entire market. Typically, forecasting is based on historical data, such as sales data, customer data, or market data. However, other factors such as economic trends, seasonal variations, and external events can also influence the demand for a product.")
st.write("There are different methods for product demand forecasting, such as qualitative methods and quantitative methods. Qualitative methods rely on expert judgment, market research, and other non-statistical techniques. Quantitative methods, on the other hand, use statistical models to analyze historical data and make predictions about future demand.")
st.write("Some common quantitative forecasting methods include time-series analysis, which uses historical data to identify trends and patterns, and regression analysis, which identifies the relationship between demand and other factors such as price, advertising, and promotions. Machine learning algorithms such as neural networks and decision trees are also used in demand forecasting to improve accuracy and automate the process.")
st.write("Overall, product demand forecasting is a critical business function that helps organizations optimize their operations and make better-informed decisions to meet customer demand and stay competitive in the marketplace.")


store = st.sidebar.selectbox('Store',df['Store'].unique())
Dept = st.sidebar.selectbox('Dept',df['Dept'].unique())
Date =st.sidebar.date_input( "When to predict", datetime.date(2011,11,11), datetime.date(2010,2,5), datetime.date(2012,10,26) )
IsHoliday = st.sidebar.selectbox('IsHoliday',[True,False])
Type = st.sidebar.selectbox('Type',["A","B","C"])

Size = st.sidebar.number_input("Size" )

query = pd.DataFrame({"Store":store,'Dept':Dept,'Date':Date,'IsHoliday':IsHoliday,'Type':Type,'Size':Size}, index=[0])
st.header('Historicall data')
st.write(query)
if st.button("Predict Demand"): 
     st.subheader('Final sales demand value')
     st.title(pipe.predict(query))
    











