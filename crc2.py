import streamlit as st
import pandas as pd 

st.title("Myntra")
d={
    "mobile":50000,
    "laptop":500000,
    "speaker":4000,
    "pendrive":5000
    }


st.subheader("cart")
product=st.selectbox("choose an item",list(d.keys()))
if "cart" not in st.session_state:
    st.session_state.cart=[]

if st.button("add to cart"):
    st.success(f"{product} is added")
    #st.write(product)
    st.session_state.cart.append(product)

#st.write(st.session_state.cart)   





st.subheader("items in cart")

if len(st.session_state.cart)>0:
    total=0
    st.subheader("items in cart")
    for i in st.session_state.cart:

        st.write(i,d[i])
        total+=d[product]

    st.write(f"total amount is :{total}")

st.subheader("remove item")

rem=st.selectbox("remove item",st.session_state.cart)
if st.button("remove item"):
    st.session_state.cart.remove(rem)
    st.success(f"{rem} has been removed")

if st.button("clear cart"):
    st.session_state.cart=[]
    st.success("cart is empty")



