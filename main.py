import yfinance as yf 
import streamlit as st
import yahoo_fin as fin
from yahoo_fin import stock_info
from patterns import Company_Name




st.set_page_config(page_title="Stock Analiysis" , page_icon=":bar_chart:", layout="wide")




def News(symbol):
    get_Data = yf.Ticker(symbol)

    #news section 
    NEWS = get_Data.news
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


company = list(Company_Name.keys())

with st.sidebar:
    st.header("**Stock Analysis**")
    select_company = st.selectbox("Select Comapany",company)

select = Company_Name.get(select_company)

information= stock_info.get_quote_data(select)
data = stock_info.get_live_price(select)


long_name = information["longName"]
st.header(long_name)

basic_info = st.container()
stock_holder= st.container()

with basic_info:

   
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        exchange = information["exchange"]
        quotetype= information["quoteType"]
        previous_close = information["regularMarketPreviousClose"]



        st.metric(label="Exchange", value=exchange)
        st.metric(label="Type", value=quotetype)
        st.metric(label="Previous Close", value=previous_close)
    with col2:
        change = information["regularMarketChange"]
        change_percentage= information["regularMarketChangePercent"]
        regular_price= information["regularMarketPrice"]
        
        st.metric(label="Regular Price", value=regular_price)
        st.metric(label="Regular Market Change", value=regular_price)
        st.metric(label="Percent Change", value=change_percentage)


    with col3:
        
        day_high = information["regularMarketDayHigh"]
        day_range = information["regularMarketDayRange"]
        day_low = information["regularMarketDayLow"]
        st.metric(label="Day High", value=day_high)
        st.metric(label="Day Low", value=day_low)
        st.metric(label="Day Range", value=day_range)
    with col4:
        
        fifty2_week_low = information["fiftyTwoWeekLow"]
        fifty2_week_high = information["fiftyTwoWeekHigh"]
        fifty2_week_range = information["fiftyTwoWeekRange"]
        st.metric(label="52 Week High", value =fifty2_week_high)
        st.metric(label="52 Week Low", value =fifty2_week_low)
        st.metric(label="52 Week Range", value =fifty2_week_range)






holders = stock_info.get_holders(select)
# st.write(holders)

with stock_holder:
    hold1,hold2 = st.columns(2)
    
    try :
        majer_hold = st.container()
        with majer_hold:
                
            majer_holders = holders["Major Holders"]
            # holst1 = majer_holders[0][0]
            # st.write( holst1)
            with hold1:
                st.header("Majer Holders")
                st.write(majer_holders)

    except:
        pass

    try:
        direct_holders = holders["Direct Holders (Forms 3 and 4)"]
        with hold2:
                st.header("Direct Holders")
                st.write(direct_holders)

    except:
        pass

News(select)



