import streamlit as st
import pandas as pd
import webbrowser

# Theme
theme = {
    "primaryColor": "#FF69B4",
    "backgroundColor": "#1E1E1E",
    "secondaryBackgroundColor": "#212121",
    "textColor": "#FFFFFF",
    "font": "sans-serif"
}

#Page configuration

st.set_page_config(page_icon=":shopping_bags:", layout="wide", initial_sidebar_state="collapsed")


def shopping():
    #Main title

    st.markdown("""
<style>
    .title {
        text-align: center;
        color: #FFFFFF;
        font-family: 'Georgia', serif;
        font-size: 80px;
        font-weight: bold;
        border: 5px solid #FF0000;
        padding: 20px;
        border-radius: 30px;
        background: linear-gradient(to right, #0A192F, #1C3456);
        box-shadow: 0 8px 32px rgba(255, 0, 0, 0.2);
        text-shadow: 2px 2px 8px rgba(255, 0, 0, 0.5);
    }
    .divider {
        height: 2px;
        background-color: #fff;
        border: none;
        box-shadow: 0px 0px 10px #fff;
        margin-bottom: 20px;
    }
</style>
<h1 class="title">SMART SALES</h1>
<hr class="divider">
""", unsafe_allow_html=True)

    cont1, cont2 ,cont3 = st.columns(3)
    
    with cont1:
        st.image('https://perfectsourcing.net/wp-content/uploads/2019/02/4.gif' , width = 460)
        
    with cont2:
        st.image('https://www.oakyweb.com/images/dc6df7e28e51cb7dcec3bdda8b502f7e.gif' , width = 460)
    
    with cont3:
        st.image('https://inbase.in/img/eco1.gif' , width = 460)    
  
    product_company = st.text_input('Enter Product Company:')
    product_name = st.text_input('Enter Product Name:')

    st.markdown("<p style='text-align: center; color : #FF00FF; font-size:30px; text-shadow: 0px 0px 10px #FF00FF;'><a href='https://www.amazon.in/' target='_blank' style='color:#FF00FF;text-decoration:none;'>AMAZON</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ------♤☮♤----- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href='https://www.flipkart.com/' target='_blank' style='color:#FF00FF;text-decoration:none;'>FLIPKART</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ------♤☮♤------ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href='https://www.google.com/' target='_blank' style='color:#FF00FF;text-decoration:none;'>GOOGLE</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </p>", unsafe_allow_html=True)
        
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
     
    #names
    st.markdown("<p style = 'text-align: center; color: #A4C400; font-family: serif; font-size: 30px; text-shadow: 0 0 3px #FF0000, 0 0 5px #FF0000, 0 0 8px #FF0000, 0 0 10px #FF0000;'> Team Members :</p>", unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; color: #A4C400; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #FF0000, 0 0 3px #FF0000, 0 0 5px #FF0000, 0 0 7px #FF0000;'>🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹⇨⇨⇨ 1) <a href = 'https://www.linkedin.com/in/nithish-rajavel-009804218/' target='_blank' style = 'color:#A4C400 ; text-decoration : none ;'> Nithish . R (21pd23) </a>🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹</p>", unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; color: #A4C400; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #FF0000, 0 0 3px #FF0000, 0 0 5px #FF0000, 0 0 7px #FF0000;'>🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹⇨⇨⇨ 2) <a href = 'https://www.linkedin.com/in/dhikshitha-6847a2221/' target='_blank' style = 'color:#A4C400 ; text-decoration : none ;'> R . Dhikshitha (21pd26) </a>🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹</p>", unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; color: #A4C400; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #FF0000, 0 0 3px #FF0000, 0 0 5px #FF0000, 0 0 7px #FF0000;'>🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹⇨⇨⇨ 3) <a href = 'https://www.linkedin.com/in/vamsi-krishna-2b377b25b/' target='_blank' style = 'color:#A4C400 ; text-decoration : none ;'> Vamsi Krishna . U (21pd38) </a>🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹</p>", unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; color: #ADD8E6; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #00008B, 0 0 3px #00008B, 0 0 5px #00008B, 0 0 7px #00008B;'> (Click at student's name to get their linked-in profile)</p>", unsafe_allow_html=True)
    
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    
    
    # Create variables to store the index of the products
    if ('i1' not in st.session_state and 'i2' not in st.session_state) :
      st.session_state.i1 = 0
      st.session_state.i2 = 0
      st.session_state.i3 = 0
      st.session_state.df1 = pd.read_csv("amazon.csv")
      st.session_state.df2 = pd.read_csv("flipkart.csv")
      st.session_state.df3 = pd.read_csv("google.csv")
        
    # Main page
    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'></h1>", unsafe_allow_html=True)
    
    # Two containers
    container1, container2 ,container3 = st.columns(3)
    container1.subheader('AMAZON')
    container2.subheader('FLIPKART')
    container3.subheader('GOOGLE')
    
    # Border between containers
    container1.markdown("<style> .css-1g8bxcc {border-right: 2px solid #ff00ff; height: 100%;} </style>", unsafe_allow_html=True)
    
    with container1:
        st.image('https://w7.pngwing.com/pngs/426/70/png-transparent-amazon-com-gift-card-discounts-and-allowances-coupon-credit-card-ebay-text-logo-internet.png' , width=300)
        st.write('              ')
        st.write('              ')
        
    with container2:
        st.image('https://tse3.mm.bing.net/th?id=OIP.Zbwq8CMb4CD6oaapV2vgSgHaEK&pid=Api&P=0' , width = 300)
        st.write('              ')
        st.write('              ')
        
    with container3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6hOu2C1fS66PbGbcLGCEKMw69whO_-FWonG26_a1zKMtvPF4usooCrGDrmjWu1jNWSp8&usqp=CAU')
        st.write('              ')
        st.write('              ')
    
        
    # Create buttons to navigate through the products in container 1
    if st.session_state.i1+3 <= len(st.session_state.df1)-1:
        if container1.button("Next1"):
            st.session_state.i1 = st.session_state.i1 +  3
    elif st.session_state.i1 < len(st.session_state.df1)-1:
        if container1.button("Next1"):
            st.session_state.i1 = len(st.session_state.df1)-1
    else:
        pass
    
    if st.session_state.i1 > 0:
        if container1.button("Previous1"):
            st.session_state.i1 = st.session_state.i1 -  3
    else:
        pass
    
    # Create buttons to navigate through the products in container 2
    if st.session_state.i2+3 <= len(st.session_state.df2)-1:
        if container2.button("Next2"):
            st.session_state.i2 = st.session_state.i2 + 3
    elif st.session_state.i2 < len(st.session_state.df2)-1:
        if container2.button("Next2"):
            st.session_state.i2 = len(st.session_state.df2)-1
    else:
        pass
    
    if st.session_state.i2 > 0:
        if container2.button("Previous2"):
            st.session_state.i2 = st.session_state.i2 - 3
    else:
        pass
    
    # Create buttons to navigate through the products in container 3
    if st.session_state.i3+3 <= len(st.session_state.df3)-1:
        if container3.button("Next3"):
            st.session_state.i3 = st.session_state.i3 + 3
    elif st.session_state.i3 < len(st.session_state.df3)-1:
        if container3.button("Next3"):
            st.session_state.i3 = len(st.session_state.df3)-1
    else:
        pass
    
    if st.session_state.i3 > 0:
        if container3.button("Previous3"):
            st.session_state.i3 = st.session_state.i3 - 3
    else:
        pass
    
    
        
    # Create the product information for container 1
    with container1:    
        for i in range(st.session_state.i1, min(st.session_state.i1+3, len(st.session_state.df1))):
            st.markdown("**"+st.session_state.df1.iloc[i]["Name"]+"**")
            st.image(st.session_state.df1.iloc[i]["Image URL"], width = 200)
            st.markdown("Price : "+str(st.session_state.df1.iloc[i]["Price"]))
            st.markdown("Average Rating : "+str(st.session_state.df1.iloc[i]["Average Rating"]))
            st.markdown("No of Ratings : "+str(st.session_state.df1.iloc[i]["No of Ratings"]))
            st.button("Purchase x" + str(i+1), key=f"purchase_x_{i}", on_click=lambda i=i: webbrowser.open_new_tab(st.session_state.df1.iloc[i]["Product URL"]))
            st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    
            
    # Create the product information for container 2
    with container2:
        for i in range(st.session_state.i2, min(st.session_state.i2+3, len(st.session_state.df2))):
            st.markdown("**"+st.session_state.df2.iloc[i]["Name"]+"**")
            st.image(st.session_state.df2.iloc[i]["Image URL"], width = 200)
            st.markdown("Price : "+str(st.session_state.df2.iloc[i]["Price"]))
            st.markdown("Average Rating : "+str(st.session_state.df2.iloc[i]["Average Rating"]))
            st.button("Purchase y" + str(i+1), key=f"purchase_y_{i}", on_click=lambda i=i: webbrowser.open_new_tab(st.session_state.df2.iloc[i]["Product URL"]))
            st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    
    # Create the product information for container 3
    with container3:
        for i in range(st.session_state.i3, min(st.session_state.i3+3, len(st.session_state.df3))):
            st.markdown("**"+st.session_state.df3.iloc[i]["Name"]+"**")
            st.image(st.session_state.df3.iloc[i]["ImageURL"], width = 200)
            st.markdown("Price : "+str(st.session_state.df3.iloc[i]["Price"]))
            st.markdown("Average Rating : "+str(st.session_state.df3.iloc[i]["Average Rating"]))
            st.button("Purchase z" + str(i+1), key=f"purchase_z_{i}", on_click=lambda i=i: webbrowser.open_new_tab(st.session_state.df3.iloc[i]["Product URL"]))
            st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)



#Dashboard

import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

def analytics():
    # Load the data
    amazon_df = pd.read_csv('amazon.csv')
    flipkart_df = pd.read_csv('flipkart.csv')
    google_df = pd.read_csv('google.csv')
    
    st.markdown("<p style = 'text-align: center; color: #ADD8E6; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #00008B, 0 0 3px #00008B, 0 0 5px #00008B, 0 0 7px #00008B;'> SCATTER PLOTS </p>", unsafe_allow_html=True)
    
    scatter_plot1 = alt.Chart(amazon_df).mark_circle().encode(x = 'Price' , y = 'Average Rating' , color = 'Name')
    
    st.altair_chart(scatter_plot1, use_container_width=True)
    
    scatter_plot2 = alt.Chart(flipkart_df).mark_circle().encode(x = 'Price' , y = 'Average Rating' , color = 'Name')
    
    st.altair_chart(scatter_plot2, use_container_width=True)
    
    scatter_plot3 = alt.Chart(google_df).mark_circle().encode(x = 'Price' , y = 'Average Rating' , color = 'Name')
    
    st.altair_chart(scatter_plot3, use_container_width=True)
    
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
        
    # Plot the bar charts for each dataset
    st.subheader('Price Comparison')
    
    bar1 , bar2 , bar3 = st.columns(3)
    
    with bar1:
        df4 = pd.read_csv("amazon.csv")
        st.subheader("AMAZON PRICES")
        bar_chart1 = alt.Chart(df4).mark_bar().encode(x = 'Name' , y = 'Price')
        
        st.altair_chart(bar_chart1, use_container_width=True)
    
    with bar2:
        df5 = pd.read_csv("flipkart.csv")
        st.subheader("FLIPKART PRICES")
        bar_chart2 = alt.Chart(df5).mark_bar().encode(x = 'Name', y = 'Price')
        
        st.altair_chart(bar_chart2, use_container_width=True)
    
    with bar3:
        df6 = pd.read_csv("google.csv")
        st.subheader("GOOGLE PRICES")
        bar_chart3 = alt.Chart(df6).mark_bar().encode(x = 'Name' , y = 'Price')
        
        st.altair_chart(bar_chart3, use_container_width=True)
        
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    
    amazon=pd.read_csv('amazon.csv')
    amazonlowtohigh=amazon.sort_values(by=['Price'])
    amazonhightolow=amazon.sort_values(by=['Price'],ascending=False)
    amazonavgrating=amazon.sort_values(by=['No of Ratings'],ascending=False)

    df=pd.read_csv('flipkart.csv')

    df.head()

    a=df.groupby(by='Average Rating')['Price'].mean()
    b=df.groupby(by='Average Rating')['Average Rating']

    c=[]
    for i in a.index:
        c.append(str(i))

    plt.bar(c,a)
    plt.xlabel('Average rating')
    plt.ylabel('Average Price')


    import squarify
    plt.rcParams['figure.figsize']=20,20
    sns.set_style(style="whitegrid")
    sizes= df["No of Ratings"]
    label=df["Name"]
    label1=[ str(i)+'\nCount='+str(sizes[i]) for i in range(len(label))]
    squarify.plot(sizes=sizes, label=label, alpha=0.6).set(title='Treemap with Squarify')
    plt.legend(['first', 'second','third'])
    plt.axis('off')
    import matplotlib.patches as mpatches
    legend=[]
    color=['']
    red_patch = mpatches.Patch('1', label='The red data')
    blue_patch = mpatches.Patch(color='blue', label='The blue data')

    plt.legend(handles=[red_patch, blue_patch])
    plt.show()

    import squarify

    a=df.groupby(by='Average Rating')['Price'].mean()

def datasets():    
    amazon_df = pd.read_csv('amazon.csv')
    flipkart_df = pd.read_csv('flipkart.csv')
    google_df = pd.read_csv('google.csv')
    # Show the datasets
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    st.title('Product Data Visualizations')
    
    # Show the Amazon data
    st.markdown("<p style = 'text-align: center; color: #ADD8E6; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #00008B, 0 0 3px #00008B, 0 0 5px #00008B, 0 0 7px #00008B;'> AMAZON DATA </p>", unsafe_allow_html=True)
    st.dataframe(amazon_df)
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    
    # Show the Flipkart data
    st.markdown("<p style = 'text-align: center; color: #ADD8E6; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #00008B, 0 0 3px #00008B, 0 0 5px #00008B, 0 0 7px #00008B;'> FLIPKART DATA </p>", unsafe_allow_html=True)
    st.dataframe(flipkart_df)
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)
    
    # Show the Google data
    st.markdown("<p style = 'text-align: center; color: #ADD8E6; font-family: serif; font-size: 25px; text-shadow: 0 0 2px #00008B, 0 0 3px #00008B, 0 0 5px #00008B, 0 0 7px #00008B;'> GOOGLE DATA </p>", unsafe_allow_html=True)
    st.dataframe(google_df)
    st.markdown("<hr style='height: 2px; background-color: #fff; border: none; box-shadow: 0px 0px 10px #fff;'>", unsafe_allow_html=True)


tabs = ["SHOPPING", "ANALYSIS" , "DATASETS"]

page = st.sidebar.selectbox("GO TO : ", tabs)

if page == "SHOPPING":
    shopping()
elif page == "ANALYSIS":
    analytics()
elif page == "DATASETS":
    datasets()