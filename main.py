import yfinance as yf 
import streamlit as st
import yahoo_fin as fin
from yahoo_fin.stock_info import *
from patterns import Company_Name
from datetime import datetime as dt,date,timedelta
import pandas as pd
import time
 

st.set_page_config(page_title="Stock Analiysis" , page_icon=":bar_chart:", layout="wide")


company = list(Company_Name.keys())
with st.sidebar:
    st.header("**Stock Analysis**")

    select_company = st.selectbox("Select Stock",company)

select = Company_Name.get(select_company)
# st.write(select)
# # st.write(type(stock_info.get))
# # n= get_company_info("aapl")[0]
# # n = get_company_info_multi(["aapl", "goog"])[0]["Symbol"]
# ticker= yf.Ticker(select)
# d=st.json(ticker.info)
# # st.write(d['symbol'])
# st.write(d.maxAge)
# st.json(ticker.get_info())
# # d=list(d)
# d = pd.DataFrame(d)
# st.write(d)
# # df= pd.DataFrame(ticker.get_info())
# # st.write(d['currentPrice'])
# print(type(d))
# for dt in d:
#     st.write(d[dt])
# st.write(df["overallRisk"].values[0])
# for d in df.columns :
#         if d=='currentPrice':
#              st.write(d)
#         else:
#             try:
#                     st.write(f":green[{d} ]"+" : "+ str(df[d].values[0]))
#             except Exception as e:
#                 st.warning(d)

# st.write("currentPrice : "+str(df["currentPrice"].values[0]))
# st.write("city : "+df["city"].values[0])
# st.write("website : "+df["website"].values[0])
# st.write("industry : "+df["industry"].values[0])
# st.write("sector : "+df["sector"].values[0])
# st.info("longBusinessSummary : "+df["longBusinessSummary"].values[0])
# st.write("shareHolderRightsRisk : "+str(df["shareHolderRightsRisk"].values[0]))

# # name= stock_info.get_quote_data(select)
# # d=pd.DataFrame(stock_info)
# st.table(df)


# st.write(name)
# long_name = name["longName"]

# st.header(long_name)
start_date = date.today()
end_date = date.today() + timedelta(days=1)

def data(symbol,period,timeframe,start_date, end_date):
    tickerData = yf.Ticker(symbol)
    tickerDf= tickerData.history(period=period,interval=timeframe,start=start_date,end=end_date)
    first_val = tickerDf['Open'].values[:1]
    return first_val

# Data = data(select,'1d','1m',start_date,end_date)
# st.write(Data)


def News(symbol):
    get_Data = yf.Ticker(symbol)
    # msft.news

    #news section 
    try:
        NEWS = get_Data.news
        # st.write(NEWS)
        st.header(f"News of {select_company} :")
        for i in range(len(NEWS)):
            st.write("\n********************************\n")
            st.write(f"{i+1}.   {NEWS[i]['title']}\n")
            st.write(f"Publisher : {NEWS[i]['publisher']}\n")
            st.write(f"Link : {NEWS[i]['link']}\n")
            st.write(f"News type : {NEWS[i]['type']}\n\n\n")
            try:
                
                resolutions = NEWS[i]['thumbnail']['resolutions']
                img = resolutions[0]['url']
                st.image(img)

            except:
                pass
    except Exception as e:
        st.write(e)
        st.warning("No news available")
News(select)

# def live_data():
#         # data = stock_info.get_live_price(select)
        
#         information= stock_info.get_quote_data(select)
        
#         # informations

#         exchange = information["exchange"]
#         quotetype= information["quoteType"]
#         previous_close = information["regularMarketPreviousClose"]
#         change = information["regularMarketChange"]
#         change_percentage= information["regularMarketChangePercent"]
#         regular_price= information["regularMarketPrice"]
#         day_high = information["regularMarketDayHigh"]
#         day_range = information["regularMarketDayRange"]
#         day_low = information["regularMarketDayLow"]
#         fifty2_week_low = information["fiftyTwoWeekLow"]
#         fifty2_week_high = information["fiftyTwoWeekHigh"]
#         fifty2_week_range = information["fiftyTwoWeekRange"]

#         valu_change = (Data * change_percentage)/100
        
#         with placeholder.container() :
            
#             # st.metric(label="LIVE COUNT", value=i)

#             col1,col2,col3 = st.columns(3)
#             with col1:
                
#                 st.metric(label="Live Price", value=regular_price)
#                 st.metric(label="Exchange", value=exchange)
#                 st.metric(label="Previous DAy High", value=day_high)
#                 st.metric(label="52 Week High", value =fifty2_week_high)

#             with col2:
            
#                 st.metric(label="Change", value=valu_change)
#                 st.metric(label="Type", value=quotetype)
#                 st.metric(label="Previous Low", value=day_low)            
#                 st.metric(label="52 Week Low", value =fifty2_week_low)



#             with col3:
                
#                 st.metric(label="% Change", value=change_percentage)
#                 st.metric(label="Previous Close", value=previous_close)
#                 st.metric(label="Day Range", value=day_range)
#                 st.metric(label="52 Week Range", value =fifty2_week_range)
#             # with col4:


# i=0

# placeholder = st.empty()
# # for i in range(200): 




# current_time = time.strftime("%H:%M:%S", time.localtime())
# market_start_time = '9:15:00'
# market_close_time = '15:15:00'
# # st.write(current_time)
# # live_data()
# # st.stop()
# if current_time<market_close_time and current_time > market_start_time:
# # if current_time>market_close_time:
#     while True:
        
#         i += 1
#         # live_data()
            
#         if i == 1:
            
#             # data = stock_info.get_live_price(select)


#             # st.header(long_name)

#             # basic_info = st.container()
#             stock_holder= st.container()



#             holders = stock_info.get_holders(select)
#             # st.write(holders)

#             with stock_holder:
#                 hold1,hold2 = st.columns(2)
                
#                 try :
#                     majer_hold = st.container()
#                     with majer_hold:
                            
#                         majer_holders = holders["Major Holders"]
#                         # holst1 = majer_holders[0][0]
#                         # st.write( holst1)
#                         with hold1:
#                             st.header("Majer Holders")
#                             st.write(majer_holders)

#                 except:
#                     pass

#                 try:
#                     direct_holders = holders["Direct Holders (Forms 3 and 4)"]
#                     with hold2:
#                             st.header("Direct Holders")
#                             st.write(direct_holders)

#                 except:
#                     pass

# else:
#     st.header("Market is Closed")
#     # live_data()



