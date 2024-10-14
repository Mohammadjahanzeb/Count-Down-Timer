import streamlit as st

# Simple calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# Streamlit app UI
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Create buttons for each operation
if st.button("Add"):
    result = add(num1, num2)
    st.write(f"The result is: {result}")

if st.button("Subtract"):
    result = subtract(num1, num2)
    st.write(f"The result is: {result}")

if st.button("Multiply"):
    result = multiply(num1, num2)
    st.write(f"The result is: {result}")

if st.button("Divide"):
    result = divide(num1, num2)
    st.write(f"The result is: {result}")
