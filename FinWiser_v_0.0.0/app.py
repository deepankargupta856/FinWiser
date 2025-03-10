import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout='wide',page_title='FinWiser')
df = pd.read_csv('export.csv')
def load_most_active_data():
    st.markdown("<h1 style='text-align: center;'>Most Active Stocks Analysis</h1>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Today's most active:")
        st.dataframe(df.sort_values(by='volume',ascending=False).head()[['name','current_market_price','change']].rename(columns={'current_market_price':'CMP','name':'company'}),hide_index=True)
    with col2:
        st.subheader('Blue chip compounders')
        blue_chips = df.sort_values(by='market_cap', ascending=False).head()[['name', 'market_cap']]
        fig, ax = plt.subplots(figsize=(3, 6))
        ax.pie(blue_chips['market_cap'], labels=blue_chips['name'], autopct='%1.1f%%')
        st.pyplot(fig)

    colA,colB = st.columns(2)
    with colA:
        st.subheader("High velocity stocks ")
        high_velo = df.sort_values(by='avg_volume', ascending=False).head(7)[['name', 'avg_volume']]
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(high_velo['avg_volume'], labels=high_velo['name'], autopct="%1.1f%%")
        st.pyplot(fig)
    with colB:
        st.subheader('Liquid as water')
        liquids = df.sort_values(by='liquidty_score', ascending=False).head(7)[['name', 'liquidty_score']]
        fig,ax=plt.subplots(figsize=(3,6))
        ax.pie(liquids['liquidty_score'],labels=liquids['name'],autopct='%1.1f%%')
        st.pyplot(fig)
    col3,col4 = st.columns(2)
    with col3:
        st.subheader('Potentially Undervalued')
        def avg_earning_yeild(earnings_yield):
            total = 0
            for i in earnings_yield.values:
                if (i == -1):
                    continue
                total += i
            return total / len(earnings_yield)

        yield_constraint = avg_earning_yeild(df['earnings_yield'])
        potentially_undervalued = df.sort_values(by='earnings_yield', ascending=False)[df['earnings_yield'] > yield_constraint].head(10)[['name', 'current_market_price', 'percent_change']]
        potentially_undervalued['percent_change'] = potentially_undervalued['percent_change'].apply(lambda x: str(x) + '%')
        potentially_undervalued.rename(columns={'current_market_price':'CMP','percent_change':'% change','name':'company'},inplace=True)
        st.dataframe(potentially_undervalued,hide_index=True)
    with col4:
        st.subheader('Gaining attraction')
        lookout = df.sort_values(by='volume_acceleration', ascending=False).head(10)[['name', 'current_market_price', 'volume']]
        lookout.rename(columns={'current_market_price':'CMP','name':'company'},inplace=True)
        st.dataframe(lookout,hide_index=True)

def company_specific_analysis(company):
    st.markdown(f"<h1 style='text-align: center;'>{company} Analysis</h1>", unsafe_allow_html=True)
    details = df[df['name']==company]
    cmp = str(details['current_market_price'].iloc[0]) + '$'
    symbol = details['symbol'].iloc[0]
    today_change = str(details['change'].iloc[0])+'$'
    percent_change = str(details['percent_change'].iloc[0]) + '%'

    def numTostr(num):
        num = round(num)
        abs_num = abs(num)

        if abs_num >= 1e12:
            return f"{num / 1e12:.1f} T"
        elif abs_num >= 1e9:
            return f"{num / 1e9:.1f} B"
        elif abs_num >= 1e6:
            return f"{num / 1e6:.1f} M"
        else:
            return str(num)
    pe = str(details['pe_ratio'].iloc[0]) if details['pe_ratio'].iloc[0] != -1 else 'No profits'
    avg_volume = numTostr(details['avg_volume'].iloc[0])
    volume = numTostr(details['volume'].iloc[0])
    marketCap = numTostr(details['market_cap'].iloc[0])

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Symbol',symbol)
    with col2:
        st.metric('Current Share Price',cmp)
    with col3:
        st.metric('Today change in price',today_change)
    with col4:
        st.metric('% change',percent_change)

    colA,colB,colC,colD = st.columns(4)

    with colA:
        st.metric('PE ratio',pe)
    with colB:
        st.metric('Average volume',avg_volume)
    with colC:
        st.metric('Current volume',volume)
    with colD:
        st.metric('Market Capitalization',marketCap)

st.sidebar.title('Options')
choice = st.sidebar.selectbox('What to View',['Most Active stocks Analysis','Company Specific Analysis'])

if choice == 'Most Active stocks Analysis':
    load_most_active_data()
elif choice == 'Company Specific Analysis':
    company = st.sidebar.selectbox('Select Company',df['name'])
    btn = st.sidebar.button('Analyze company')
    if btn :
        company_specific_analysis(company)