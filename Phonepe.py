import git
import pandas as pd
import os
import json
import pymysql
import plotly_express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.stoggle import stoggle
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

Agg_User=pd.DataFrame(table2,columns=["State","Year","Quarter","User_count","User_amount","User_percentage"])


#Map_Transaction
cur.execute("SELECT * from map_trans")
myconnection.commit()
table3=cur.fetchall()

Map_Transaction=pd.DataFrame(table3,columns=["State","Year","Quarter","Trans_type","Trans_count","Trans_amount"])


#Map_User
cur.execute("SELECT * from map_user")
myconnection.commit()
table4=cur.fetchall()

Map_User=pd.DataFrame(table4,columns=["State","Year","Quarter","Trans_type","Trans_count","Trans_amount"])


#Top_Trans_States
cur.execute("SELECT * from top_trans_states")
myconnection.commit()
table5=cur.fetchall()

Top_Trans_States=pd.DataFrame(table5,columns=["Year","Quarter","States","States_Trans_Type","States_Trans_Count","States_Trans_Amount"])


#Top_Trans_Districts
cur.execute("SELECT * from top_trans_districts")
myconnection.commit()
table6=cur.fetchall()

Top_Trans_Districts=pd.DataFrame(table6,columns=["Year","Quarter","Districts","Districts_Trans_Type","Districts_Trans_Count","Districts_Trans_Amount"])


#Top_Trans_Pincodes
cur.execute("SELECT * from top_trans_pincodes")
myconnection.commit()
table7=cur.fetchall()

Top_Trans_Pincodes=pd.DataFrame(table7,columns=["Year","Quarter","Pincodes","Pincodes_Trans_Type","Pincodes_Trans_Count","Pincodes_Trans_Amount"])


#Top_User_States
cur.execute("SELECT * from top_user_states")
myconnection.commit()
table8=cur.fetchall()

Top_User_States=pd.DataFrame(table8,columns=["Year","Quarter","States","States_Registeredusers"])


#Top_User_Districts
cur.execute("SELECT * from top_user_districts")
myconnection.commit()
table9=cur.fetchall()

Top_User_Districts=pd.DataFrame(table9,columns=["Year","Quarter","Districts","Districts_Registeredusers"])


#Top_User_Pincodes
cur.execute("SELECT * from top_user_pincodes")
myconnection.commit()
table10=cur.fetchall()

Top_User_pincodes=pd.DataFrame(table10,columns=["Year","Quarter","Pincodes","Pincodes_Registeredusers"])

def aggre_trans_y(df,years):
    A_Trans = df[df["Year"]==years]
    A_Trans.reset_index(drop=True,inplace=True)

    A_Trans_G = A_Trans.groupby("Trans_type")[["Trans_count","Trans_amount"]].sum()
    A_Trans_G.reset_index(inplace=True)

    col1,col2=st.columns(2)
    with col1:
        fig_pie_count = px.pie(A_Trans_G,values="Trans_count",names="Trans_type",title=f"{years}Aggregate Transaction Count",color_discrete_sequence=px.colors.sequential.haline,height=400,width=380)
        st.plotly_chart(fig_pie_count)
    
    with col2:
        fig_pie_amount = px.pie(A_Trans_G,values="Trans_amount",names="Trans_type",title=f"{years}Aggregate Transaction Amount",color_discrete_sequence=px.colors.sequential.Pinkyl_r,height=400,width=380)
        st.plotly_chart(fig_pie_amount)

def aggre_trans_q(df,quarter):
    A_Trans_Q = Agg_Transaction[Agg_Transaction["Quarter"]==quarter]
    A_Trans_Q.reset_index(drop=True,inplace=True)

    A_Trans_QG = A_Trans_Q.groupby("Trans_type")[["Trans_count","Trans_amount"]].sum()
    A_Trans_QG.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_bar_count = px.bar(A_Trans_QG,x="Trans_type",y="Trans_count",title=f"Q{quarter} Aggregate Transaction Count",color_discrete_sequence=px.colors.sequential.Magma_r,height=500,width=400)
        st.plotly_chart(fig_bar_count)

    with col2:
        fig_bar_amount = px.bar(A_Trans_QG,x="Trans_type",y="Trans_amount",title=f"Q{quarter} Aggregate Transaction Count",color_discrete_sequence=px.colors.sequential.Bluyl_r,height=500,width=400)
        st.plotly_chart(fig_bar_amount)

def aggre_user_y(df,years):
    A_User = df[df["Year"]==years]
    A_User.reset_index(drop=True,inplace=True)

    A_User_G = A_User.groupby("User_count")[["User_amount","User_percentage"]].sum()
    A_User_G.reset_index(inplace=True)

    col1,col2=st.columns(2)
    with col1:
        fig_pie_count = px.pie(A_User_G,values="User_amount",names="User_count",title=f"{years}Aggregate User Amount",color_discrete_sequence=px.colors.sequential.haline,height=700,width=300)
        st.plotly_chart(fig_pie_count)
    
    with col2:
        fig_pie_amount = px.pie(A_User_G,values="User_percentage",names="User_count",title=f"{years}Aggregate User Percentage",color_discrete_sequence=px.colors.sequential.Pinkyl_r,height=700,width=300)
        st.plotly_chart(fig_pie_amount)

def aggre_user_q(df,quarter):
    A_User_Q = Agg_User[Agg_User["Quarter"]==quarter]    
    A_User_Q.reset_index(drop=True,inplace=True)

    A_User_QG = A_User_Q.groupby("User_count")[["User_amount","User_percentage"]].sum()
    A_User_QG.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_bar_count = px.bar(A_User_QG,x="User_count",y="User_amount",title=f"Q{quarter} Aggregate User Amount",color_discrete_sequence=px.colors.sequential.Blackbody)
        st.plotly_chart(fig_bar_count)

    with col2:
        fig_bar_amount = px.bar(A_User_QG,x="User_count",y="User_percentage",title=f"Q{quarter} Aggregate User Percaentage",color_discrete_sequence=px.colors.sequential.Plotly3_r)
        st.plotly_chart(fig_bar_amount)


#STREAMLIT PAGE

icon=Image.open("Phonepe_logo.png")
image=Image.open("PhonePe-Logo.wine.png")
st.set_page_config(page_title="Phonepe Pulse Data Visualization and Exploration",
                   page_icon=icon,
                   layout="centered",
                   initial_sidebar_state="auto")


def home_page():
    st.title("Phonepe Pulse Data Visualization and Exploration")
    st.image(image,use_column_width=True,output_format='PNG')
    st.write("PhonePe is an Indian digital payments and financial services company")
    st.write(" The PhonePe app, based on the Unified Payments Interface (UPI)")
    st.write("The PhonePe app is accessible in 11 Indian languages.")
    st.divider()
    st.subheader("***BENEFITS OF PHONEPE***")
    
    with st.expander("DIGITAL PAYMENTS"):
        st.write("PhonePe is India’s most trusted digital payment partner.It helps seamlessly process 100% online payments from your customers and is absolutely secure. It also equipped to handle large-scale transactions with best-in-class success rates.")

    with st.expander("MERCHANT PAYMENTS"):
        st.write("Business persons can easily get money from customer's, by just scanning the QR code.")

    with st.expander("EXPLORE VARIOUS CASHBACK"):
        st.write("Various cashback offers are available in Phonepe")

    with st.expander("INVESTMENTS"):
        st.write("Using, phonepe user can also easily invest in stocks easily")

    with st.expander("LENDING"):
        st.write("Phonepe app can also available lending options like home loan,vehicle loan with no paper documents and in digitally.")

    with st.expander("SAFE TO USE"):
        st.write("Phonepe is essential to bear in mind that in order to be safe, as each user can generate a unique password.")

    url="https://play.google.com/store/apps/details?id=com.phonepe.app&hl=en_IN&shortlink=2kk1w03o&c=consumer_app_icon&pid=PPWeb_app_download_page&af_xp=custom&source_caller=ui&pli=1"
    st.download_button(
    label="Click on the button to download",
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
            aggre_trans_y(Agg_Transaction,year_at)

            quarter_at = st.selectbox("Select the quarters",Agg_Transaction["Quarter"].unique())
            aggre_trans_q(Agg_Transaction,quarter_at)

            state_at = st.selectbox("Select the states",Agg_Transaction["State"].unique())
        
        elif method_1 == "User":
            year_au = st.selectbox("Select the years",Agg_User["Year"].unique())
            aggre_user_y(Agg_User,year_au)

            quarter_au = st.selectbox("Select the quarters",Agg_User["Quarter"].unique())
            aggre_user_q(Agg_User,quarter_au)
            
            state_at = st.selectbox("Select the states",Agg_User["State"].unique())
            
    
    with tab2:
        method_2 = st.selectbox("Select method_2",["Transaction","User"])
        
        if method_2 == "Transaction":
            year_mt = st.selectbox("Select the years",Map_Transaction["Year"].unique())

            quarter_mt = st.selectbox("Select the quarter",Map_Transaction["Quarter"].unique())

            state_mt = st.selectbox("Select the states",Map_Transaction["State"].unique())
        elif method_2 == "User":
            year_mu = st.selectbox("Select the years",Map_User["Year"].unique())

            quarter_mu = st.selectbox("Select the quarter",Map_User["Quarter"].unique())

            state_mu = st.selectbox("Select the states",Map_User["State"].unique())


    with tab3:
        method_3 = st.selectbox("Select method_3",["Transaction","User"])


elif selected == "Data_Visualisation":
    pass

