import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


st.header("WELCOME TO MY DASHBOARD")
st.title("MT CARS DASHBOARD")

mtcars = pd.read_csv('mtcars.csv')
st.dataframe(mtcars)

plots = ['Scatterplot', 'Barplot', 'Boxplot']
features = ['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# Sidebar
st.sidebar.header('Choose plot type')
plot_type = st.sidebar.selectbox('', plots)

if plot_type == 'Scatterplot':
    st.sidebar.header('Choose x and y features')
    x_feature = st.sidebar.selectbox('X-axis', features)
    y_feature = st.sidebar.selectbox('Y-axis', features, index=1)
    
    # Scatterplot
    st.subheader('Scatterplot')
    fig, ax = plt.subplots()
    ax.scatter(mtcars[x_feature], mtcars[y_feature])
    ax.set_xlabel(x_feature)
    ax.set_ylabel(y_feature)
    st.pyplot(fig)
    
elif plot_type == 'Barplot':
    st.sidebar.header('Choose feature')
    feature = st.sidebar.selectbox('Feature', features)
    
    # Barplot
    st.subheader('Barplot')
    fig, ax = plt.subplots()
    ax.bar(mtcars.index, mtcars[feature])
    ax.set_xticks(mtcars.index)
    ax.set_xticklabels(mtcars['model'], rotation=90)
    ax.set_xlabel('Model')
    ax.set_ylabel(feature)
    st.pyplot(fig)
    
else:
    st.sidebar.header('Choose feature')
    feature = st.sidebar.selectbox('Feature', features)
    
    # Boxplot
    st.subheader('Boxplot')
    fig, ax = plt.subplots()
    ax.boxplot(mtcars[feature], vert=False)
    ax.set_xlabel(feature)
    st.pyplot(fig)
    
# Histogram
st.subheader('Histogram')
hist_feature = st.selectbox('Select feature', features, index=0)
fig, ax = plt.subplots()
ax.hist(mtcars[hist_feature], bins=10)
ax.set_xlabel(hist_feature)
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Heatmap
st.subheader('Heatmap')
corr = mtcars.corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm')
st.pyplot(fig)

