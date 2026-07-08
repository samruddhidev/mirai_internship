import streamlit as st

st.set_page_config(page_title="Smart Calculator", page_icon="🧮")

st.title("🧮 Smart Calculator")
st.write("Perform simple arithmetic operations.")

first_num = st.number_input("Enter the first number", value=0.0)
second_num = st.number_input("Enter the second number", value=0.0)

operation = st.radio(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate Result"):

    if operation == "Addition":
        answer = first_num + second_num

    elif operation == "Subtraction":
        answer = first_num - second_num

    elif operation == "Multiplication":
        answer = first_num * second_num

    else:
        if second_num == 0:
            st.error("Division by zero is not allowed.")
            st.stop()
        answer = first_num / second_num

    st.success(f"Result: {answer}")

st.caption("Developed using Streamlit")