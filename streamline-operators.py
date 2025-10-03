import streamlit as st
st.title("This Is a Webapp")
st.write("Hello, this is created with the help of streamlit")
st.subheader("Try performing some operations!!!")
st.divider()
num1 = st.number_input("please enter a number=", value=0)
num2 = st.number_input("please enter another number=", value=0)
if st.button("add"):
    add = num1 + num2
    st.success(f'the result of these two numbers is {add}')

if st.button("subtract"):
    subtract = num1 - num2
    st.success(f'the result of these two numbers is {subtract}')

if st.button("divide"):
    divide = num1 / num2
    st.success(f'the result of these two numbers is {divide}')

if st.button("multiply"):
    multi = num1 * num2
    st.success(f'the result of these two numbers is {multi}')
