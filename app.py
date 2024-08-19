import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image,ImageEnhance,ImageFilter

#Title
st.title("IRIS EDA App")
st.write("Build with Streamlit"+"❤️")

#EDA
my_dataset='iris.csv'

#to save the data as Cache
@st.cache_data

#function to load Dataset
def explore_data(dataset):
    df=pd.read_csv(os.path.join(dataset))
    return df
data=explore_data(my_dataset)
if st.checkbox("Preview Dataset"):
  
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())
    else:
        st.write(data.head(2))
        

#Show entire DataSet
if st.checkbox("Show All Dataset"):
   
    st.write(data)

#Show Column Name
if st.checkbox("Show Column Names"):
    st.write(data.columns)

#Show Dimensions
data_dim = st.radio("what Dimension DO you Want to See?",("Columns","Rows","All"))
if data_dim=="Rows":
    st.text("Showing Rows")
    st.write(data.shape[0])

elif data_dim=="Columns":
    st.text("Showing Columns")
    st.write(data.shape[1])
else:
    st.text("Showing shape of Dataset")
    st.write(data.shape)

#Show Summary
if st.checkbox("Show Summary of Dataset"):
    st.write(data.describe())

#Select A colums
col_option=st.selectbox("Select Column",("sepal_length","sepal_width","petal_length","petal_width","species"))
if col_option =="sepal_width":
    st.write(data['sepal_width'])
elif col_option =="sepal_length":
    st.write(data['sepal_length'])
elif col_option =="petal_width":
    st.write(data['petal_width'])
elif col_option =="petal_length":
    st.write(data['petal_length'])
elif col_option =="species":
    st.write(data['species'])
else:
    st.write("Select Column")


#Plot 
#Show Summary
if st.checkbox("Show Bar Plot with Matplotlib"):
    fig, ax = plt.subplots()
    data['species'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)


if st.checkbox("Show Correlation Plot with Matplotlib"):
    # Select only numeric columns and drop rows with missing values
    numeric_data = data.select_dtypes(include=['number']).dropna()
    
    # Compute the correlation matrix
    corr_matrix = numeric_data.corr()
    
    # Plot the correlation matrix
    fig, ax = plt.subplots()
    cax = ax.matshow(corr_matrix)
    fig.colorbar(cax)
    st.pyplot(fig)

    #Correlation
if st.checkbox("Show Correlation Plot"):
    # Select only numeric columns and drop rows with missing values
    numeric_data = data.select_dtypes(include=['number']).dropna()
    
    # Generate the heatmap
    fig, ax = plt.subplots()
    corr_plot = sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", ax=ax)

    # Use st.pyplot() to display the plot
    st.pyplot(fig)


# Group
if st.checkbox("Show Bar Chart Plot"):
    # Group the data by 'species' and aggregate (e.g., sum, mean, etc.)
    v_group = data.groupby('species').size()

    # Convert the aggregated group to a DataFrame or Series if needed
    st.bar_chart(v_group)

#Group
if st.checkbox("Show line Chart Plot"):
    st.line_chart(data)

# Group
if st.checkbox("Show Area Chart Plot"):
    
    v_group = data.groupby('species').size()

    st.area_chart(v_group)

# alternative code for above function can be
# if st.checkbox("Show Area Chart Plot"):
#     # Group the data by 'species' and count the occurrences
#     v_group = data.groupby('species').size().reset_index(name='count')

#     # Set 'species' as the index, if necessary
#     v_group = v_group.set_index('species')

#     # Plot the area chart
#     st.area_chart(v_group)

#Images
@st.cache_data
def load_image(img):
    im=Image.open(os.path.join(img))
    return im
species_type =st.radio("Select Species Type",("Setosa","virginica","versicolor"))
if species_type =="Setosa":
    st.text("Showing Setosa Species")
    st.image(load_image('imgs/iris_setosa.jpg'))

if species_type =="virginica":
    st.text("Showing Virginica Species")
    st.image(load_image('imgs/iris_virginica.jpg'))
if species_type =="versicolor":
    st.text("Showing Versicolor Species")
    st.image(load_image('imgs/iris_versicolor.jpg'))

#Show Image
if st.checkbox("Setosa Image"):
    my_image =load_image("iris_setosa.jpg")
    enh =ImageEnhance.Contrast(my_image)
    num=st.slider("Set Image Contrast",1.0,4.0)
    img_width=st.slider("SetImage Width",300,500)
    st.image(enh.enhance(num),width=img_width)

if st.checkbox("Virginica Image"):
    my_image =load_image("imgs/iris_virginica.jpg")
    enh =ImageEnhance.Contrast(my_image)
    num=st.slider("Set Image Contrast",1.0,4.0)
    img_width=st.slider("SetImage Width",300,500)
    st.image(enh.enhance(num),width=img_width)
    
if st.checkbox("Versicolor Image"):
    my_image =load_image("imgs/iris_versicolor.jpg")
    enh =ImageEnhance.Contrast(my_image)
    num=st.slider("Set Image Contrast",1.0,4.0)
    img_width=st.slider("SetImage Width",300,500)
    st.image(enh.enhance(num),width=img_width)
#About
if st.button("About App"):
    st.text("Iris EDA APP")
    st.text("Build with Streamlit")
 