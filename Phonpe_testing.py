import git
import pandas as pd
import os
import json
import pymysql
import plotly_express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#Agg_tras
path = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)

clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
#Adding states list to the path
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    
    #Adding year list to the path
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        
        #Adding file to the path
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            A=json.load(Data)
            
            #Extracted data from the file
            for z in A['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)

Agg_Trans["State"]=Agg_Trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Trans["State"]=Agg_Trans["State"].str.replace("-"," ")
Agg_Trans["State"]=Agg_Trans["State"].str.title()
Agg_Trans["State"]=Agg_Trans["State"].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Agg_user
path1 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path1)

clm={'State':[], 'Year':[],'Quarter':[],'User_count':[], 'User_amount':[], 'User_percentage':[]}

for i in Agg_state_list:
    p_i=path1+i+"/"
    Agg_yr=os.listdir(p_i)
    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            B=json.load(Data)
            try:
                for z in B['data']['usersByDevice']:
                    count=z['brand']
                    amount=z['count']
                    percentage=z['percentage']
                    clm['User_count'].append(count)
                    clm['User_amount'].append(amount)
                    clm['User_percentage'].append(percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Succesfully created a dataframe
Agg_User=pd.DataFrame(clm)

Agg_User["State"]=Agg_User["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_User["State"]=Agg_User["State"].str.replace("-"," ")
Agg_User["State"]=Agg_User["State"].str.title()
Agg_User["State"]=Agg_User["State"].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Map_trans
path2 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/map/transaction/hover/country/india/state/"
Map_state_list=os.listdir(path2)

clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Map_state_list:
    p_i=path2+i+"/"
    Map_yr=os.listdir(p_i)
    
    for j in Map_yr:
        p_j=p_i+j+"/"
        Map_yr_list=os.listdir(p_j)
        
        for k in Map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            C=json.load(Data)
            
            for z in C['data']['hoverDataList']:
              Name=z['name']
              Type=z['metric'][0]['type']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Map_Trans=pd.DataFrame(clm)

Map_Trans["State"]=Map_Trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_Trans["State"]=Map_Trans["State"].str.replace("-"," ")
Map_Trans["State"]=Map_Trans["State"].str.title()
Map_Trans["State"]=Map_Trans["State"].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Map_user
path3 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/map/user/hover/country/india/state/"
Map_state_list=os.listdir(path3)

clm={'State':[], 'Year':[],'Quarter':[],'Districts':[], 'RegisteredUser':[], 'AppOpens':[]}

for i in Map_state_list:
    p_i=path3+i+"/"
    Map_yr=os.listdir(p_i)
    
    for j in Map_yr:
        p_j=p_i+j+"/"
        Map_yr_list=os.listdir(p_j)
        
        for k in Map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            
            for z in D['data']['hoverData'].items():
                district=z[0]
                registeredusers=z[1]['registeredUsers']
                appopens=z[1]['appOpens']
                clm['Districts'].append(district)
                clm['RegisteredUser'].append(registeredusers)
                clm['AppOpens'].append(appopens)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Map_User=pd.DataFrame(clm)

Map_User["State"]=Map_User["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_User["State"]=Map_User["State"].str.replace("-"," ")
Map_User["State"]=Map_User["State"].str.title()
Map_User["State"]=Map_User["State"].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Top_trans_states
path4 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/top/transaction/country/india/"
Top_years = ['2018', '2019', '2020', '2021', '2022', '2023']
Top_trans=os.listdir(path4)

clm={'Year':[],'Quarter':[],'States':[], 'States_Trans_Type':[], 'States_Trans_Count':[],'States_Trans_Amount':[]}
                            
for j in Top_years:
    p_j=path4+j+"/"
    Top_yr_list=os.listdir(p_j)

    for k in Top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)
            
            for z in F["data"]["states"]:
                entityname=z['entityName']
                type=z['metric']['type']
                count=z['metric']['count']
                amount=z['metric']['amount']
                clm['States'].append(entityname)
                clm['States_Trans_Type'].append(type)
                clm['States_Trans_Count'].append(count)
                clm['States_Trans_Amount'].append(amount)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_Trans_States=pd.DataFrame(clm)

Top_Trans_States["States"]=Top_Trans_States["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_Trans_States["States"]=Top_Trans_States["States"].str.replace("-"," ")
Top_Trans_States["States"]=Top_Trans_States["States"].str.title()
Top_Trans_States["States"]=Top_Trans_States["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Top_trans_districts
path4 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/top/transaction/country/india/"
Top_years = ['2018', '2019', '2020', '2021', '2022', '2023']
Top_trans=os.listdir(path4)

clm={'Year':[],'Quarter':[],'Districts':[],'Districts_Trans_Type':[],'Districts_Trans_Count':[],'Districts_Trans_Amount':[]}

for j in Top_years:
    p_j=path4+j+"/"
    Top_yr_list=os.listdir(p_j)

    for k in Top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)

            for z in F["data"]["districts"]:
                entityname=z['entityName']
                type=z['metric']['type']
                count=z['metric']['count']
                amount=z['metric']['amount']
                clm['Districts'].append(entityname)
                clm['Districts_Trans_Type'].append(type)
                clm['Districts_Trans_Count'].append(count)
                clm['Districts_Trans_Amount'].append(amount)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_Trans_Districts=pd.DataFrame(clm)

Top_Trans_Districts["Districts"]=Top_Trans_Districts["Districts"].str.title()

#Top_trans_pincodes
path4 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/top/transaction/country/india/"
Top_years = ['2018', '2019', '2020', '2021', '2022', '2023']
Top_trans=os.listdir(path4)

clm={'Year':[],'Quarter':[],'Pincodes':[],'Pincodes_Trans_Type':[],'Pincodes_Trans_Count':[],'Pincodes_Trans_Amount':[]}

for j in Top_years:
    p_j=path4+j+"/"
    Top_yr_list=os.listdir(p_j)

    for k in Top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)
            
            for z in F["data"]["pincodes"]:
                entityname=z['entityName']
                type=z['metric']['type']
                count=z['metric']['count']
                amount=z['metric']['amount']
                clm['Pincodes'].append(entityname)
                clm['Pincodes_Trans_Type'].append(type)
                clm['Pincodes_Trans_Count'].append(count)
                clm['Pincodes_Trans_Amount'].append(amount)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))


#Succesfully created a dataframe
Top_Trans_Pincodes=pd.DataFrame(clm)

#Top_user_state
path5 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/top/user/country/india/"
Top_years = ['2018', '2019', '2020', '2021', '2022', '2023']
Top_user=os.listdir(path5)

clm={'Year':[],'Quarter':[], 'States':[], 'States_Registeredusers':[]}
                            
for j in Top_years:
    p_j=path5+j+"/"
    Top_yr_list=os.listdir(p_j)
        
    for k in Top_yr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        F=json.load(Data)
            
        for z in F["data"]["states"]:
            name=z['name']
            registeredUsers=z['registeredUsers']
            clm['States'].append(name)
            clm['States_Registeredusers'].append(registeredUsers)
            clm['Year'].append(j)
            clm['Quarter'].append(int(k.strip('.json')))
    
#Succesfully created a dataframe
Top_User_States=pd.DataFrame(clm)

Top_User_States["States"]=Top_User_States["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_User_States["States"]=Top_User_States["States"].str.replace("-"," ")
Top_User_States["States"]=Top_User_States["States"].str.title()
Top_User_States["States"]=Top_User_States["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Top_user_districts
path5 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/top/user/country/india/"
Top_years = ['2018', '2019', '2020', '2021', '2022', '2023']
Top_user=os.listdir(path5)

clm={'Year':[],'Quarter':[],'Districts':[],'Districts_Registeredusers':[]}
                            
for j in Top_years:
    p_j=path5+j+"/"
    Top_yr_list=os.listdir(p_j)
        
    for k in Top_yr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        F=json.load(Data)


        for z in F["data"]["districts"]:
            name=z['name']
            registeredUsers=z['registeredUsers']
            clm['Districts'].append(name)
            clm['Districts_Registeredusers'].append(registeredUsers)
            clm['Year'].append(j)
            clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_User_Districts=pd.DataFrame(clm)

Top_User_Districts["Districts"]=Top_User_Districts["Districts"].str.title()

#Top_user_pincodes
path5 = "C:/Users/Padma Jothi/Desktop/Capstone/pulse/data/top/user/country/india/"
Top_years = ['2018', '2019', '2020', '2021', '2022', '2023']
Top_user=os.listdir(path5)

clm={'Year':[],'Quarter':[],'Pincodes':[],'Pincodes_Registeredusers':[]}
                            
for j in Top_years:
    p_j=path5+j+"/"
    Top_yr_list=os.listdir(p_j)
        
    for k in Top_yr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        F=json.load(Data)

    for z in F["data"]["pincodes"]:
            name=z['name']
            registeredUsers=z['registeredUsers']
            clm['Pincodes'].append(name)
            clm['Pincodes_Registeredusers'].append(registeredUsers)
            clm['Year'].append(j)
            clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_User_Pincodes=pd.DataFrame(clm)

#Inserting the collected DataFrame to Mysql database
myconnection = pymysql.connect(host='127.0.0.1',user='root',passwd='Tspjgoge@5',database='phonepe')
cur = myconnection.cursor()

#Aggregate Transaction
def aggregate_transaction():
    create_query1 = '''create table if not exists agg_trans (State varchar(50),
                                                                Year int,
                                                                Quarter int,
                                                                Transaction_type varchar(50), 
                                                                Transaction_count int, 
                                                                Transaction_amount float)'''
    cur.execute(create_query1)
    myconnection.commit()

    for index,row in Agg_Trans.iterrows():
        insert_query1 = '''INSERT INTO agg_trans (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["State"],
                row["Year"],
                row["Quarter"],
                row["Transaction_type"],
                row["Transaction_count"],
                row["Transaction_amount"]
                )
        cur.execute(insert_query1,values)
        myconnection.commit()
aggregate_transaction()

#Aggregate User
def aggregate_user():
    create_query2 = '''create table if not exists agg_user (State varchar(50),
                                                            Year int,
                                                            Quarter int,
                                                            User_count varchar(50), 
                                                            User_amount int, 
                                                            User_percentage float)'''
    cur.execute(create_query2)
    myconnection.commit()

    for index,row in Agg_User.iterrows():
        insert_query2 = '''INSERT INTO agg_user (State, Year, Quarter, User_count, User_amount, User_percentage)
                                                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["State"],
                row["Year"],
                row["Quarter"],
                row["User_count"],
                row["User_amount"],
                row["User_percentage"]
                )
        cur.execute(insert_query2,values)
        myconnection.commit()
aggregate_user()

#Map Transaction
def map_transaction():
    create_query3 = '''create table if not exists map_trans (State varchar(50),
                                                            Year int,
                                                            Quarter int,
                                                            Transaction_type varchar(50), 
                                                            Transaction_count varchar(50), 
                                                            Transaction_amount varchar(50))'''
    cur.execute(create_query3)
    myconnection.commit()

    for index,row in Map_Trans.iterrows():
        insert_query3 = '''INSERT INTO map_trans (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["State"],
                row["Year"],
                row["Quarter"],
                row["Transaction_type"],
                row["Transaction_count"],
                row["Transaction_amount"]
                )
        cur.execute(insert_query3,values)
        myconnection.commit()
map_transaction()

#Map User
def map_user():
    create_query4 = '''create table if not exists map_user (State varchar(50),
                                                            Year int,
                                                            Quarter int,
                                                            Districts varchar(50), 
                                                            RegisteredUser varchar(50), 
                                                            AppOpens varchar(50))'''
    cur.execute(create_query4)
    myconnection.commit()

    for index,row in Map_User.iterrows():
        insert_query4 = '''INSERT INTO map_user (State, Year, Quarter, Districts, RegisteredUser, AppOpens)
                                                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["State"],
                row["Year"],
                row["Quarter"],
                row["Districts"],
                row["RegisteredUser"],
                row["AppOpens"]
                )
        cur.execute(insert_query4,values)
        myconnection.commit()
map_user()

#Top_Trans_states
def top_trans_states():
    create_query5 = '''create table if not exists top_trans_states (Year int,
                                                            Quarter int,
                                                            States varchar(50), 
                                                            States_Trans_Type varchar(50), 
                                                            States_Trans_Count varchar(50),
                                                            States_Trans_Amount varchar(50))'''
    cur.execute(create_query5)
    myconnection.commit()

    for index,row in Top_Trans_States.iterrows():
        insert_query5 = '''INSERT INTO top_trans_states (Year, Quarter, States, States_Trans_Type, States_Trans_Count,States_Trans_Amount)
                                                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["Year"],
                row["Quarter"],
                row["States"],
                row["States_Trans_Type"],
                row["States_Trans_Count"],
                row["States_Trans_Amount"]
                )
        cur.execute(insert_query5,values)
        myconnection.commit()

top_trans_states()

#Top_Trans_districts
def top_trans_districts():
    create_query6 = '''create table if not exists top_trans_districts (Year int,
                                                            Quarter int,
                                                            Districts varchar(50), 
                                                            Districts_Trans_Type varchar(50), 
                                                            Districts_Trans_Count varchar(50),
                                                            Districts_Trans_Amount varchar(50))'''
    cur.execute(create_query6)
    myconnection.commit()

    for index,row in Top_Trans_Districts.iterrows():
        insert_query6 ='''INSERT INTO top_trans_districts(Year,Quarter,Districts,Districts_Trans_Type,Districts_Trans_Count,Districts_Trans_Amount)
                                                        VALUES(%s,%s,%s,%s,%s,%s)'''
        values = (row["Year"],
                  row["Quarter"],
                  row["Districts"],
                  row["Districts_Trans_Type"],
                  row["Districts_Trans_Count"],
                  row["Districts_Trans_Amount"],
                  )
        cur.execute(insert_query6,values)
        myconnection.commit

top_trans_districts()

#Top_Trans_pincodes
def top_trans_pincodes():
    create_query7 = '''create table if not exists top_trans_pincodes (Year int,
                                                            Quarter int,
                                                            Pincodes varchar(50), 
                                                            Pincodes_Trans_Type varchar(50), 
                                                            Pincodes_Trans_Count varchar(50),
                                                            Pincodes_Trans_Amount varchar(50))'''
    cur.execute(create_query7)
    myconnection.commit()

    for index,row in Top_Trans_Pincodes.iterrows():
        insert_query7='''INSERT INTO top_trans_pincodes(Year,Quarter,Pincodes,Pincodes_Trans_Type,Pincodes_Trans_Count,Pincodes_Trans_Amount)
                                                        VALUES(%s,%s,%s,%s,%s,%s)'''
        values = (row["Year"],
                  row["Quarter"],
                  row["Pincodes"],
                  row["Pincodes_Trans_Type"],
                  row["Pincodes_Trans_Count"],
                  row["Pincodes_Trans_Amount"]
                  )
        cur.execute(insert_query7,values)
        myconnection.commit

top_trans_pincodes()

#Top_User_States
def top_user_states():
    create_query8 = '''create table if not exists top_user_states(Year int,
                                                                Quarter int,
                                                                States varchar(50),
                                                                States_Registeredusers varchar(50))'''
    cur.execute(create_query8)
    myconnection.commit()

    for index,row in Top_User_States.iterrows():
        insert_query8='''INSERT INTO top_user_states(Year,Quarter,States,States_Registeredusers)
                                                        values(%s,%s,%s,%s)'''
        values = (row['Year'],
                  row['Quarter'],
                  row['States'],
                  row['States_Registeredusers']
        )
        cur.execute(insert_query8,values)
        myconnection.commit()

top_user_states()

#Top_User_Districts
def top_user_districts():
    create_query9 = '''create table if not exists top_user_districts(Year int,
                                                                Quarter int,
                                                                Districts varchar(50),
                                                                Districts_Registeredusers varchar(50))'''
    cur.execute(create_query9)
    myconnection.commit()

    for index,row in Top_User_Districts.iterrows():
        insert_query9='''INSERT INTO top_user_districts(Year,Quarter,Districts,Districts_Registeredusers)
                                                            values(%s,%s,%s,%s)'''
        values = (row['Year'],
                  row['Quarter'],
                  row['Districts'],
                  row['Districts_Registeredusers']
        )
        cur.execute(insert_query9,values)
        myconnection.commit()

top_user_districts()

#Top_Users_Pincodes
def top_users_pincodes():
    create_query10 = '''create table if not exists top_user_pincodes(Year int,
                                                                    Quarter int,
                                                                    Pincodes varchar(50),
                                                                    Pincodes_Registeredusers varchar(50))'''
    cur.execute(create_query10)
    myconnection.commit()

    for index,row in Top_User_Pincodes.iterrows():
        insert_query10='''INSERT INTO top_user_pincodes(Year,Quarter,Pincodes,Pincodes_Registeredusers)
                                                        values(%s,%s,%s,%s)'''
        values = (row['Year'],
                  row['Quarter'],
                  row['Pincodes'],
                  row['Pincodes_Registeredusers']
        )
        cur.execute(insert_query10,values)
        myconnection.commit()
        
top_users_pincodes()


#Function to fetch data details from the database and convert to dataframe

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



#STREAMLIT PAGE

icon=Image.open("Phonepe_logo.png")
image=Image.open("download.jpeg")
st.set_page_config(page_title="Phonepe Pulse Data Visualization and Exploration",
                   page_icon=icon,
                   layout="centered",
                   initial_sidebar_state="auto")


def home_page():
    st.title("Phonepe Pulse Data Visualization and Exploration")
    st.image(image,use_column_width=False)
    st.write("PhonePe is an Indian digital payments and financial services company")
    st.write(" The PhonePe app, based on the Unified Payments Interface (UPI)")
    st.write("The PhonePe app is accessible in 11 Indian languages.")
    st.write("*****BENEFITS OF PHNOEPE USAGES*****")
    st.write("*****DIGITAL PAYMENTS*****")
    st.write("*****MERCHANT PAYMENTS*****")
    st.write("*****EXPLORE VARIOUS CASHBACK*****")
    st.write("*****SAFE TO USE*****")

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
            year_at = st.selectbox("Select the years",Agg_Transaction["Year"])

            quarter_at = st.selectbox("Select the quarters",Agg_Transaction["Quarter"].unique())

            state_at = st.selectbox("Select the states",Agg_Transaction["State"].unique())
        
        elif method_1 == "User":
            year_au = st.selectbox("Select the years",Agg_User["Year"])

            quarter_at = st.selectbox("Select the quarters",Agg_User["Quarter"].unique())

            state_at = st.selectbox("Select the states",Agg_User["State"].unique())
            
    with tab2:
        method_2 = st.selectbox("Select method_2",["Transaction","User"])
    with tab3:
        method_3 = st.selectbox("Select method_3",["Transaction","User"])


elif selected == "Data_Visualisation":
    pass

