import streamlit as st
import test2
from PIL import Image
import base64
t = test2.result()
st.title("# Welcome to Food Recommendation System! :cake: " " :pizza:")
foods = t.food()

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('foodr1234.jpg')    




food_choice = st.selectbox("PICK A FOOD ", foods)
st.write("------------------")

c1, c2, c3 = st.columns(3)

m1, m2, m3 = t.query(food_choice)

with c1:
    st.subheader("Simple Content Based Filtering")
    st.write("Recommends food based on similar foods")
    st.write("------------------")
    for index, ele in enumerate(m1):
        st.write(index,ele.title())
    st.write("------------------")

with c2:
    st.subheader("Collaborative Based Filtering")
    st.write("Recommends food based on similar users")
    st.write("------------------")
    if m3 == None:
        st.write("**Less user ratings for this food item !!!**")
        st.write("So, the recommender cannot pull any recommendations ")
    else:
        for index, ele in enumerate(m3):
            st.write(index, ele.title())
    st.write("------------------")

with c3:
    st.subheader("Advanced Content Based Filtering")
    st.write("Recommends food based on similar foods and its features")
    st.write("------------------")
    for index, ele in enumerate(m2):
        st.write(index, ele.title())
    st.write("------------------")
