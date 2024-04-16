import git
import pandas as pd
import os
import json
import requests
import pymysql
import plotly_express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


#Function to fetch data details from the database and convert to dataframe
myconnection = pymysql.connect(host='127.0.0.1',user='root',passwd='Tspjgoge@5',database='phonepe')
cur = myconnection.cursor()
#Aggregate_Trans
cur.execute("SELECT * from agg_trans")
myconnection.commit()
table1=cur.fetchall()

Agg_Transaction=pd.DataFrame(table1,columns=["State","Year","Quarter","Trans_type","Trans_count","Trans_amount"])


#Aggregate_User
cur.execute("SELECT * from agg_user")
myconnection.commit()
table2=cur.fetchall()

Agg_User=pd.DataFrame(table2,columns=["State","Year","Quarter","User_brand","User_count","User_percentage"])


#Map_Transaction
cur.execute("SELECT * from map_trans")
myconnection.commit()
table3=cur.fetchall()

Map_Transaction=pd.DataFrame(table3,columns=["State","Year","Quarter","Districts","Trans_type","Trans_count","Trans_amount"])


#Map_User
cur.execute("SELECT * from map_user")
myconnection.commit()
table4=cur.fetchall()

Map_User=pd.DataFrame(table4,columns=["State","Year","Quarter","Districts","RegisteredUsers","AppOpens"])


#Top_Trans_States
cur.execute("SELECT * from top_trans_states")
myconnection.commit()
table5=cur.fetchall()

Top_Trans_States=pd.DataFrame(table5,columns=["Year","Quarter","States","Trans_type","Trans_count","Trans_amount"])


#Top_Trans_Districts
cur.execute("SELECT * from top_trans_districts")
myconnection.commit()
table6=cur.fetchall()

Top_Trans_Districts=pd.DataFrame(table6,columns=["Year","Quarter","Districts","Trans_type","Trans_count","Trans_amount"])

#Top_Trans_Pincodes
cur.execute("SELECT * from top_trans_pincodes")
myconnection.commit()
table7=cur.fetchall()

Top_Trans_Pincodes=pd.DataFrame(table7,columns=["Year","Quarter","Pincodes","Trans_type","Trans_count","Trans_amount"])

#Top_User_States
cur.execute("SELECT * from top_user_states")
myconnection.commit()
table8=cur.fetchall()

Top_User_States=pd.DataFrame(table8,columns=["Year","Quarter","States","Registeredusers"])


#Top_User_Districts
cur.execute("SELECT * from top_user_districts")
myconnection.commit()
table9=cur.fetchall()

Top_User_Districts=pd.DataFrame(table9,columns=["Year","Quarter","Districts","Registeredusers"])


#Top_User_Pincodes
cur.execute("SELECT * from top_user_pincodes")
myconnection.commit()
table10=cur.fetchall()

Top_User_pincodes=pd.DataFrame(table10,columns=["Year","Quarter","Pincodes","Registeredusers"])

def aggre_trans_y(df,years,quarter):
    A_Trans = df[(df["Year"]==years) & (df["Quarter"]==quarter)]
    A_Trans.reset_index(drop=True,inplace=True)

    A_Trans_G = A_Trans.groupby("Trans_type")[["Trans_count","Trans_amount"]].sum()
    A_Trans_G.reset_index(inplace=True)

    fig_pie_count = px.pie(A_Trans_G,values="Trans_count",names="Trans_type",title=f"{years} Q{quarter} Aggregate Transaction Count",color_discrete_sequence=px.colors.sequential.haline)
    st.plotly_chart(fig_pie_count)
    
    fig_pie_amount = px.pie(A_Trans_G,values="Trans_amount",names="Trans_type",title=f"{years} Q{quarter} Aggregate Transaction Amount",color_discrete_sequence=px.colors.sequential.Pinkyl_r)
    st.plotly_chart(fig_pie_amount)


def aggre_trans_s(df,year):
    A_Trans_S = df[df["Year"]==year]
    A_Trans_S.reset_index(drop=True,inplace=True)

    A_Trans_SG = A_Trans_S.groupby("State")[["Trans_count","Trans_amount"]].sum()
    A_Trans_SG.reset_index(inplace=True)

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    data1=json.loads(response.content)
    states_name = []
    for feature in data1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()
        
    fig_map_state = px.choropleth(A_Trans_SG,geojson = data1,locations ="State",featureidkey= "properties.ST_NM",
                                    color = "Trans_count", color_continuous_scale="Ylgnbu",hover_name = "State",
                                    title = f"{year} TRANSACTION COUNT",fitbounds = "locations")
    fig_map_state.update_geos(visible = False)
    st.plotly_chart(fig_map_state)

    fig_map_state = px.choropleth(A_Trans_SG,geojson = data1,locations ="State",featureidkey= "properties.ST_NM",
                                    color = "Trans_amount", color_continuous_scale="Tealrose",hover_name = "State",
                                    title = f"{year} TRANSACTION AMOUNT",fitbounds = "locations")
    fig_map_state.update_geos(visible = False)
    st.plotly_chart(fig_map_state)

def aggre_user_y(df,years,quarter):
    A_User = df[(df["Year"]==years) & (df["Quarter"]==quarter)]
    A_User.reset_index(drop=True,inplace=True)

    A_User_G = A_User.groupby("User_count")[["User_amount","User_percentage"]].sum()
    A_User_G.reset_index(inplace=True)

    fig_bar_count = px.bar(A_User_G,x="User_count",y="User_amount",title=f"{years} Q{quarter} Aggregate User Amount",color_discrete_sequence=px.colors.sequential.Blackbody)
    st.plotly_chart(fig_bar_count)

    fig_bar_amount = px.bar(A_User_G,x="User_count",y="User_percentage",title=f"{years} Q{quarter} Aggregate User Percaentage",color_discrete_sequence=px.colors.sequential.Plotly3_r)
    st.plotly_chart(fig_bar_amount)


def map_trans_y(df,years,quarter):
    M_Trans = df[(df["Year"]==years) & (df["Quarter"]==quarter)]
    M_Trans.reset_index(drop=True,inplace=True)

    M_Trans_G = M_Trans.groupby("Districts")[["Trans_count","Trans_amount"]].sum()
    M_Trans_G.reset_index(inplace=True)

    fig_scatter_chart = px.scatter(M_Trans_G, x="Trans_count", y="Trans_amount", color="Districts",size='Trans_count', hover_data=['Trans_amount'])
    st.plotly_chart(fig_scatter_chart)


def map_user_q(df,year,quarter):
    M_User = df[(df["Year"]==year) & (df["Quarter"]==quarter)]
    M_User.reset_index(drop=True,inplace=True)

    M_User_GQ= M_User.groupby("Districts")[["RegisteredUsers","AppOpens"]].sum()
    M_User_GQ.reset_index(inplace=True)
    
    fig_line_chart = px.line(M_User_GQ, x='Districts', y=["RegisteredUsers","AppOpens"],title='Map User Analysis')
    st.plotly_chart(fig_line_chart)

def top_trans_p(df,year,quarter):
    T_Trans = df[(df["Year"]==year) & (df["Quarter"]==quarter)]
    T_Trans.reset_index(drop=True,inplace=True)

    T_Trans_G = T_Trans.groupby("Pincodes")[["Trans_count","Trans_amount"]].sum().reset_index()

    fig_top_plot_1= px.line(T_Trans_G, x= "Pincodes", y= ["Trans_count","Trans_amount"], markers= True,
                                title= "Top Pincode Count and Amount in Transaction wise",color_discrete_sequence= px.colors.sequential.Rainbow_r)
    st.plotly_chart(fig_top_plot_1)

def top_user_p(df,year,quarter):
    T_User = df[(df["Year"]==year) & (df["Quarter"]==quarter)]
    T_User.reset_index(drop=True,inplace=True)

    T_Trans_G = T_User.groupby("Pincodes")[["Registeredusers"]].sum().reset_index()

    fig_top_pin = px.scatter(T_Trans_G, x="Pincodes", y="Registeredusers", color="Pincodes",size='Registeredusers')
    fig_top_pin.update_traces(visible=True)
    st.plotly_chart(fig_top_pin)

#QUESTIONS LIST

def ques1():
    state=Agg_Transaction[["State","Trans_amount"]]
    state1=state.groupby("State")["Trans_amount"].sum().sort_values(ascending=False)
    state_df=pd.DataFrame(state1).reset_index()

    fig_1=px.bar(state_df,x='State',y='Trans_amount',color='State',pattern_shape='Trans_amount',height=900,width=1000)
    st.plotly_chart(fig_1)

def ques2():
    brand= Agg_User[["User_brand","User_count"]]
    brand_g= brand.groupby("User_brand")["User_count"].sum().sort_values(ascending=False)
    brand_df= pd.DataFrame(brand_g).reset_index()

    fig_2= px.pie(brand_df, values= "User_count", names= "User_brand", color_discrete_sequence=px.colors.sequential.dense_r,
                       title= "Top Mobile Brands of Transaction_count")
    st.plotly_chart(fig_2)

def ques3():
    Map_D= Map_Transaction[["Districts", "Trans_amount"]]
    Map_G= Map_D.groupby("Districts")["Trans_amount"].sum().sort_values(ascending=False)
    Map_df= pd.DataFrame(Map_G).head(10).reset_index()

    fig_3= px.box(Map_df, x= "Districts", y= "Trans_amount", title="TOP 10 DISTRICTS OF HIGHEST TRANSACTION AMOUNT",color="Districts",hover_data="Districts",labels={"Districts","Transaction amount"},height=600,width=1000)
    st.plotly_chart(fig_3)

def ques4():
    Map_S= Map_User[["State", "AppOpens"]]
    Map_SG= Map_S.groupby("State")["AppOpens"].sum().sort_values(ascending=False)
    Map_df= pd.DataFrame(Map_SG).reset_index().head(10)

    fig_4= px.area(Map_df, x= "State", y= "AppOpens", title="Top 10 States With AppOpens",color="State",labels={"STATES","APPOPENS"})
    st.plotly_chart(fig_4)

def ques5():
    Agg_S= Agg_Transaction[["State", "Trans_count"]]
    Agg_G= Agg_S.groupby("States")["Trans_count"].sum().sort_values(ascending=False)
    Agg_df= pd.DataFrame(Agg_G).reset_index()

    fig_5= px.bar(Agg_df, x= "States", y= "Trans_count", title= "STATES WITH HIGHEST TRANSACTION COUNT",
                    color="States",animation_frame="Trans_count")
    st.plotly_chart(fig_5)

def ques6():
    Map_D= Map_Transaction[["Districts", "Trans_amount"]]
    Map_G= Map_D.groupby("Districts")["Trans_amount"].sum().sort_values(ascending=True)
    Map_df= pd.DataFrame(Map_G).reset_index().head(50)

    fig_6= px.bar(Map_df, x= "Districts", y= "Trans_amount", title= "DISTRICTS WITH LOWEST TRANSACTION AMOUNT",
                color_discrete_sequence= px.colors.sequential.Mint_r)
    st.plotly_chart(fig_6)

def ques7():
    Top_S=Top_User_States[["States","Registeredusers"]]
    Top_G=Top_S.groupby("States")["Registeredusers"].sum().sort_values(ascending=False)
    Top_df=pd.DataFrame(Top_G).reset_index().head(10)

    fig_7=px.line(Top_df,x="States",y="Registeredusers",color="States",symbol="States",line_shape="hvh",title="STATES WITH HIGHEST REGISTEREDUSERS",height=700,width=1000)
    st.plotly_chart(fig_7)

def ques8():
    Top_D=Top_User_Districts[["Districts","Registeredusers"]]
    Top_G=Top_D.groupby("Districts")["Registeredusers"].sum().sort_values(ascending=True)
    Top_df=pd.DataFrame(Top_G).reset_index()

    fig_8=px.violin(Top_df,x="Districts",y="Registeredusers",color="Districts",violinmode="overlay",title="DISTRICT WITH LOWEST REGISTEREDUSERS",height=800,width=900,animation_group="Districts")
    st.plotly_chart(fig_8)

def ques9():
    Top_P=Top_User_pincodes[["Pincodes","Registeredusers"]]
    Top_G=Top_P.groupby("Pincodes")["Registeredusers"].sum().sort_values(ascending=False)
    Top_df=pd.DataFrame(Top_G).reset_index()

    fig_9=px.pie(Top_df,names="Pincodes",values="Registeredusers",color="Pincodes",title="PINCODES WITH HIGHEST REGISTEREDUSERS",)
    st.plotly_chart(fig_9)

def ques10():
    Top_P=Top_Trans_Pincodes[["Pincodes","Trans_amount"]]
    Top_G=Top_P.groupby("Pincodes")["Trans_amount"].sum().sort_values(ascending=False)
    Top_df=pd.DataFrame(Top_G).reset_index().head(10)

    fig_10=px.scatter(Top_df,x='Pincodes',y='Trans_amount',color='Pincodes',opacity=0.7, width=800,height=400)
    st.plotly_chart(fig_10)


#STREAMLIT PAGE
icon=Image.open("Phonepe_logo.png")
image=Image.open("Phonepe.gif")
st.set_page_config(page_title="Phonepe Pulse Data Visualization and Exploration",
                   page_icon=icon,
                   layout="wide",
                   initial_sidebar_state="auto")


def home_page():
    st.title("Phonepe Pulse Data Visualization and Exploration")
    st.image(image,use_column_width=False,output_format='GIF')
    st.write("*PhonePe is an Indian digital payments and financial services company.*")
    st.write("*The PhonePe app, based on the Unified Payments Interface (UPI).*")
    st.write("*The PhonePe app is accessible in 11 Indian languages.*")
    st.divider()
    st.subheader("***BENEFITS OF PHONEPE***")
    
    with st.expander("**DIGITAL PAYMENTS**"):
        st.write("PhonePe is India’s most trusted digital payment partner.It helps seamlessly process 100% online payments from your customers and is absolutely secure. It also equipped to handle large-scale transactions with best-in-class success rates.")

    with st.expander("**MERCHANT PAYMENTS**"):
        st.write("Business persons can easily get money from customer's, by just scanning the QR code.")

    with st.expander("**EXPLORE VARIOUS CASHBACK**"):
        st.write("Various cashback offers are available in Phonepe")

    with st.expander("**INVESTMENTS**"):
        st.write("Using, phonepe user can also easily invest in stocks easily")

    with st.expander("**LENDING**"):
        st.write("Phonepe app can also available lending options like home loan,vehicle loan with no paper documents and in digitally.")

    with st.expander("**SAFE TO USE**"):
        st.write("Phonepe is essential to bear in mind that in order to be safe, as each user can generate a unique password.")

    url="https://play.google.com/store/apps/details?id=com.phonepe.app&hl=en_IN&shortlink=2kk1w03o&c=consumer_app_icon&pid=PPWeb_app_download_page&af_xp=custom&source_caller=ui&pli=1"
    st.download_button(
    label="***Click on the button to download the app***",
    data=url,
    file_name='Phonepe App',
    mime='text/csv',
)

with st.sidebar:
    selected=option_menu("Sub-Categories",["Home","Data_Exploration","Data_Visualisation"],
                         icons=None,    
                         orientation="vertical"
                         )
    
if selected == "Home":
    home_page()

elif selected == "Data_Exploration":
    st.title("Phonepe Pulse Data Visualization and Exploration")
    tab1,tab2,tab3 = st.tabs(["Aggregate","Map","Top"])

    with tab1:
        method_1= st.selectbox("Select the Analysis Method",["Transaction","User"])
        
        if method_1 == "Transaction":
            year_at = st.selectbox("Select the years",Agg_Transaction["Year"].unique())
            quarter_at = st.selectbox("Select the quarters",Agg_Transaction["Quarter"].unique())
            aggre_trans_y(Agg_Transaction,year_at,quarter_at)
            aggre_trans_s(Agg_Transaction,year_at)
        
        elif method_1 == "User":
            year_au = st.selectbox("Select the years",Agg_User["Year"].unique())
            quarter_au = st.selectbox("Select the quarters",Agg_User["Quarter"].unique())
            aggre_user_y(Agg_User,year_au,quarter_au)

    with tab2:
        method_2 = st.selectbox("Select method_2",["Transaction","User"])
        
        if method_2 == "Transaction":
            year_mt = st.selectbox("Select the map_trans years",Map_Transaction["Year"].unique())
            quarter_mt = st.selectbox("Select the map_trans quarter",Map_Transaction["Quarter"].unique())
            map_trans_y(Map_Transaction,year_mt,quarter_mt)

        elif method_2 == "User":
            year_mu = st.selectbox("Select the map_user years",Map_User["Year"].unique())
            quarter_mu = st.selectbox("Select the map_user quarter",Map_User["Quarter"].unique())
            map_user_q(Map_User,year_mu,quarter_mu)


    with tab3:
        method_3 = st.selectbox("Select method_3",["Transaction","User"])
        
        if method_3 == "Transaction":
            year_tt = st.selectbox("Select the top years",Top_Trans_Pincodes["Year"].unique())
            quarter_tt = st.selectbox("Select the top_trans quarter",Top_Trans_Pincodes["Quarter"].unique())
            top_trans_p(Top_Trans_Pincodes,year_tt,quarter_tt)

        elif method_3 == "User":
            year_tu = st.selectbox("Select the top_user years",Top_User_pincodes["Year"].unique())
            quarter_tu = st.selectbox("Select the top_user quarter",Top_User_pincodes["Quarter"].unique())
            top_user_p(Top_User_pincodes,year_tu,quarter_tu)


elif selected == "Data_Visualisation":
    ques = st.selectbox("**Select the Question**",('States with highest transaction amount',
                                                    'Top mobile brands of user count',
                                                    'Top 10 districts with highest transaction count',
                                                    'Top 10 states with highest appopens',
                                                    'States with highest transaction count',
                                                    'Districts with lowest transaction amount',
                                                    'States with highest registeredusers',
                                                    'Districts with lowest registeredusers',
                                                    'Pincodes with highest registeredusers',
                                                    'Top 10 Pincodes with highest Transaction amount'))
    
    if ques=='States with highest transaction amount':
        ques1()

    elif ques=='Top mobile brands of user count':
        ques2()
    
    elif ques=='Top 10 districts with highest transaction count':
        ques3()

    elif ques=='Top 10 states with highest appopens':
        ques4()

    elif ques=='States with highest transaction count':
        ques5()

    elif ques=='Districts with lowest transaction amount':
        ques6()

    elif ques=='States with highest registeredusers':
        ques7()

    elif ques=='Districts with lowest registeredusers':
        ques8()

    elif ques=='Pincodes with highest registeredusers':
        ques9()

    elif ques=='Top 10 Pincodes with highest Transaction amount':
        ques10()
